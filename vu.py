import os
import sys,re
import datetime
from datetime import datetime, timedelta
import json
import random
import platform
try:
  import requests
except ImportError:
  os.system('pip install requests')
  import requests
try:
  from colorama import Back, Fore, Fore, Style, init
except ImportError:
  os.system('pip install colorama')
  from colorama import Back, Fore, Fore, Style, init
try:
  from bs4 import BeautifulSoup
except ImportError:
  os.system('pip3 install beautifulsoup4')
  from bs4 import BeautifulSoup

import time
from time import sleep
import json,ast
os.system('clear')

init(autoreset=True)



def pr3(text):
  lines = text.split('\n')
  for line in lines:
      sys.stdout.write(line+'\n')
      sys.stdout.flush()
      sleep(0.1)
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.01)
  print()

def time():
  current_time = datetime.now()

  time = current_time.strftime("%M:%S")
  return time

def cint(number):
  while True:
    try:
      numbers = int(input(number))
      return numbers
    except ValueError:
      print(f'{red}Vui lòng chỉ nhập số')



def changetoken(red,green,white):
  if os.path.exists("cache_golike_auth.txt"):
    text=f'''{green}DÙNG AUTH CŨ HAY ĐỔI AUTH
{red}[{white}1{red}] ĐỔI AUTH
{red}[{white}2{red}] DÙNG AUTH CŨ'''
    pr3(text)
    changetoken=cint(f'{red}NHẬP LỰA CHỌN: {green}')
    print('--------------------------------------------------------------------')
    if changetoken==1:
      file_name = 'cache_golike_auth.txt'
      if os.path.exists(file_name):
          os.remove(file_name)
    else:
      pass


banner=f'''
\033[1;91m
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀  ⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
     ⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
     ⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
     ⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀     ⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀     ⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀     ⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀     ⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀     ⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                                                                                                                                                   
                                                                                                                                                         
\033[1;32m                                                            
██╗          ██╗   ██╗    ██╗    █████████╗  ██████╗    ██████╗  ███╗    
 ██╗        ██╔╝   ██║    ██║    ╚══███╔══╝███╔═══███╗███╔═══███╗███║                                    
  ██╗      ██╔╝    ██║    ██║       ███║   ███║   ███║███║   ███║███║
   ██╗    ██╔╝     ██║    ██║       ███║   ███║   ███║███║   ███║███║
    ██╗  ██╔╝      ██║    ██║       ███║   ███║   ███║███║   ███║███║
      ████╔╝        ╚██████╔╝       ███║    ╚██████╔╝  ╚██████╔╝ ████████╗
      ╚═══╝          ╚═════╝        ╚══╝     ╚═════╝    ╚═════╝  ╚═══════╝
 
             
\033[1;39m                 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m                 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
\033[1;39m┌────────────────── NGỌC VŨ LẬP TRÌNH VIÊN ────────────────┐
\033[1;32m \033[1;32mPHP \033[1;39mCODE\033[1;32m 3.0                                        \033[1;32m
\033[1;32m                CHÀO MỪNG BẠN ĐÃ NƠI KIẾM TIỀN

\033[1;35m  FACEBOOK:     https://www.facebook.com/profile.php?id=100070678453308
\033[1;32m  ZALO:         0353994142               
\033[1;35m  NGÂN HÀNG:    MB Bank : 0353994142
\033[1;32m  MOMO:         0353994142
\033[1;39m└──────────────────────────────────────────────────────────┘
\033[1;97m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬                                                              


'''

def bes4(url):
  html_source = requests.get(url).text
  soup = BeautifulSoup(html_source, 'html.parser')
  og_description = soup.find('meta', {'property': 'og:description'})
  if og_description:
      text =og_description['content']
      return text
  else:
      print("Không tìm thấy thẻ meta với thuộc tính property='og:description'")





def checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
 while True :
  while True :
    if not os.path.exists("cache_golike_auth.txt"):
      auth=str(input(f'~[😈]{red}Nhập auth:{green} '))
      headers ={
    'Authorization'     :auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
 }
      check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)
      if check['status']==200:
        name=check['data'][0]['username']
        hea={
'Authorization':auth,
't':    'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}
# Chuỗi JSON đầu vào
        data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text
        try:
          data=json.loads(data)
        except :
          break
        # Tính tổng pending coin
        total_pending_coin = 0
        for key, value in data.items():
            if isinstance(value, dict) and 'pending_coin' in value:
                total_pending_coin += value['pending_coin']
        xht=data['current_coin']
        text=f'~😈[]{red}THÀNH CÔNG'
        text=f'{red}TÊN TÀI KHOẢN: {green} {name}'
        pr(text)
        text=f'{green}${red} SỐ TIỀN TRONG TÀI KHOẢN :{green}{xht}đ'
        pr(text)
        # In tổng pending coin
        text=f'{green}${red} ĐANG DUYỆT TIỀN:{green}{total_pending_coin}đ'
        pr(text)
        print('--------------------------------------------------------------------')
        text=f'~[😈]{red}HÃY {green}CHỌN TÀI KHOẢN KIẾM TIỀN '
        pr(text)
        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
        for i, nickname in enumerate(nicknames, start=1):
            globals()[f'{i}'] = nickname
        # In giá trị của các biến
        for i, nickname in enumerate(nicknames, start=1):
            text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
            pr(text)
        with open("cache_golike_auth.txt", "w") as state_file:
          state_file.write(auth)
        return auth,check
      else:
        text=f'~[😈]{red}SAI AUTH>>{green}NHẬP LẠI'
        continue
    else:
     with open('cache_golike_auth.txt') as f:
        lines = f.readlines()
        auth=lines[0]
        headers ={
      'Authorization'   :auth,
      't':      'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
      'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
      }
        check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)
        if check['status']==200:
          name =check['data'][0]['username']
          hea={
                'Authorization':auth,
                't':    'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                  }


          data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text
          try:
            data=json.loads(data)
          except :
            break
          # Tính tổng pending coin
          total_pending_coin = 0
          for key, value in data.items():
              if isinstance(value, dict) and 'pending_coin' in value:
                  total_pending_coin += value['pending_coin']
          xht=data['current_coin']
          text=f'{red}TÊN TÀI KHOẢN: {green} {name}'
          pr(text)
          text=f'{green}${red} SỐ TIỀN TRONG TÀI KHOẢN :{green}{xht}đ'
          pr(text)
          # In tổng pending coin
          text=f'{green}${red} ĐANG DUYỆT TIỀN:{green}{total_pending_coin}đ'
          pr(text)
          nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
          for i, nickname in enumerate(nicknames, start=1):
              globals()[f'{i}'] = nickname
          print('--------------------------------------------------------------------')
          text=f'~[😈]{red}HÃY {green}CHỌN TÀI KHOẢN KIẾM TIỀN '
          pr(text)
          # In giá trị của các biến
          for i, nickname in enumerate(nicknames, start=1):
              text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
              pr(text)

        return auth, check




def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :

    user_input=input(f'~[😈]{random.choice(ranmau)}>{random.choice(ranmau)}>{random.choice(ranmau)}> {green}BẠN HÃY CHỌN TÀI KHOẢN KIẾM TIỀN:{green} ')
    try:
      n = int(user_input)
      if 'data' in check and len(check['data']) >= n:
          idtiktok = check['data'][n-1]['id']
          if idtiktok :
              text=f"{red}ID SỐ {n} LÀ: {green}{idtiktok}"
              pr(text)
              print('--------------------------------------------------------------------')
              return idtiktok
          else:
              text=f"{red}KHÔNG THẤY TÀI KHOẢN TƯƠNG ỨNG."
              pr(text)
      else:
          continue
    except ValueError:
          pr(f"{red}VUI LÒNG CHỈ NHẬP SỐ.")
          continue

def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  job_success=0
  while True :
    while True :
      hea={
      'Authorization':  auth,
     't':       'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

      try:
        a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
      except :
        break
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        os.system(f'termux-open-url {link}')
      except :
        break
      for k in range(delay,-1,-1):
        mau=random.choice(ranmau)
        print(f'{green}NGỌC VŨ:{red}[{job_success}/{startmaxjob-1}]{random.choice(ranmau)}LOADING  {random.choice(ranmau)}>> {yellow}NHIỆM VỤ MỚI  {random.choice(ranmau)}>>> {random.choice(ranmau)}{k}s ',end='\r')
        sleep(1)
      headers = {
          'authorization': auth,
     't':       'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

      json_data = {
          'ads_id': id,
          'account_id': idtiktok ,
          'async': True,
          'data': None,
      }

      g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
      try:
        g=json.loads(g)
      except :
        break
      if g['status']==200:
        job_success+=1
        print(f'{green}NGỌC VŨ:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}THÀNH CÔNG | {green}FOLLOW | +{g["data"]["prices"]}')
        startmaxjob+=1
        if startmaxjob == maxjob+1:
          print(f'~[+]{pink}Đã bị nhả ,vui lòng đổi acc khác. ')
          return
      else:
        print(f'{green}Đang nhận tiền       ',end="\r")
        sleep(1)
        g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
        try:
          g=json.loads(g)
        except :
          break
        if g['status']==200:
          job_success+=1
          print(f'{green}NGỌC VŨ:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}THÀNH CÔNG | {green}FOLLOW | +{g["data"]["prices"]}đ')
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'~[😈]{pink}Đã bị nhả ,vui lòng đổi acc khác. ')
            return
        if g['status'] !=200:
          print(f'{red}BỎ QUA NHIỆM VỤ                   ',end='\r')
          headers = {
              'authorization': auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

          json_data = {
              'description': 'Lỗi rồi',
              'users_advertising_id': id,
              'type': 'ads',
              'provider': 'tiktok',
              'fb_id': idtiktok ,
              'error_type': 3,
          }

          requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)


          headers = {
              'authorization': auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

          json_data = {
              'ads_id': id,
              'object_id': object_id,
              'account_id': idtiktok ,
              'type': 'follow',
          }
          skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
              headers=headers,
              json=json_data,
          )
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'~[😈]{green}Đã bị nhả ,vui lòng đổi acc khác')
            return

def getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  job_success=0
  while True :
    while True :
      hea={
      'Authorization':  auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

      try:
        a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
      except :
        break
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        if 'video' in link:
          print(f"{red}ĐANG XÓA JOB LIKE                             ",end='\r')
          headers = {
              'authorization': auth,
    't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}

          json_data = {
    'description': 'Tôi đéo làm Job này',
    'users_advertising_id': id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': idtiktok,
    'error_type': 0,
}

          response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)


          json_data = {
    'ads_id': id,
    'object_id': object_id,
    'account_id': idtiktok,
    'type': 'like',
}
          response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
)
        else:
          os.system(f'termux-open-url {link}')
          for k in range(delay,-1,-1):
            mau=random.choice(ranmau)
            print(f'{green}Thành công:{red}[{job_success}/{startmaxjob-1}]{random.choice(ranmau)}LOADING  {random.choice(ranmau)}>>> {yellow}Nhiệm vụ mới {random.choice(ranmau)}>>> {random.choice(ranmau)}{k}s',end='\r')
            sleep(1)
          print(f'{red}Đang nhận tiền                 ',end='\r')
          headers = {
              'authorization': auth,
        't':    'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
    }

          json_data = {
              'ads_id': id,
              'account_id': idtiktok ,
              'async': True,
              'data': None,
          }
          try:

            g =requests.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
            if g['status']==200:
              job_success+=1
              print(f'{green}NGỌC VŨ:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}THÀNH CÔNG | {green}FOLLOW | +{g["data"]["prices"]}đ')
              startmaxjob+=1
              if startmaxjob == maxjob+1:
                print(f'~[😈]{pink}Đã bị nhả ,vui lòng đổi acc khác. ')
                return

            else:
              print(f'{green}Đang nhận tiền                     ',end="\r")
              sleep(1)

              try:
                g = requests.post(
                'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
                headers=headers,
                json=json_data,
            ).json()
                if g['status']==200:
                  job_success+=1
                  print(f'{green}NGỌC VŨ:{red}[{job_success}/{startmaxjob-1}] {cyan}[{time()}] | {random.choice(ranmau)}THÀNH CÔNG | {green}FOLLOW | +{g["data"]["prices"]}đ')
                  startmaxjob+=1
                  if startmaxjob == maxjob+1:
                    print(f'~[😈]{pink}Đã bị nhả ,vui lòng đổi acc khác. ')
                    return
                else:
                  print(f'{red}BỎ QUA NHIỆM VỤ                   ',end='\r')
                  headers = {
                      'authorization': auth,
            't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        }

                  json_data = {
                      'description': 'Lỗi rồi',
                      'users_advertising_id': id,
                      'type': 'ads',
                      'provider': 'tiktok',
                      'fb_id': idtiktok ,
                      'error_type': 3,
                  }

                  requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)


                  headers = {
                      'authorization': auth,
            't':        'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        }

                  json_data = {
                      'ads_id': id,
                      'object_id': object_id,
                      'account_id': idtiktok ,
                      'type': 'follow',
                  }
                  skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
                      headers=headers,
                      json=json_data,
                  )
                  startmaxjob+=1
                  if startmaxjob == maxjob+1:
                    print(f'~[😈]{green}Đã bị nhả ,vui lòng đổi acc khác')
                    return
              except :
                print('Đang thử lại......')
                sleep(1)
          except :
            break
      except:
         break

#biến
#green='\033[38;5;10m'
blue='\033[1;39m'
cyan='\033[1;39m'
white='\033[1;39m'
magenta='\033[1;39m'
orange='\033[1;39m'
xanhnhat = "\033[1;39m"
red = "\033[1;39m"
green = "\033[1;39m"
yellow = "\033[1;39m"
xduong = "\033[1;39m"
pink = "\033[1;39m"
pin = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
redb="\033[1;39m"
end='\033[1;39m'
ranmau=(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
print(banner)
print(f'{pink}            XIN CHÀO, BẠN ĐÃ ĐẾN NƠI KIẾM TIỀN')






changetoken(red,green,white)
auth,check =checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
while True:
      if not os.path.exists("setting_golike.txt"):
        idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
        print(f'''~[😈]{red}MUỐN LỌC JOB LIKE KHÔNG:
{red}[1]:{green}CÓ
{red}[2]:{green}KHÔNG''')
        select_job=cint(f'{red}NHẬP:{green}')
        delay =cint(f'~[😈]{red}Nhập delay: {green}')
        maxjob= cint(f'~[😈]{red}Nhập max: {green}')
        setting={
          "loaijob":select_job,
          "delay":delay,
          "maxjob":maxjob
        }
        with open("setting_golike.txt", "w") as file:
    # Ghi dữ liệu vào tệp tin
              file.write(json.dumps(setting))
        print(f'{cyan}BẮT ĐẦU CHẠY ',end='\r')
        print('--------------------------------------------------------------------')
        sleep(1)
        if select_job==1:
          getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
        else:
          getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
      else:
          idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
          select_setting=input(f'{green}BẠN có muốn sử dụng cài đặt cũ không?[y/n]{cyan}:' )
          if select_setting == 'n':
             os.remove('setting_golike.txt')
             os.system('clear')
             break

          try:
              with open("setting_golike.txt", "r") as file:
                data_txt=file.read()
                data_json = json.loads(data_txt)
              select_job = int(data_json.get('loaijob'))
              delay = int(data_json.get('delay'))
              maxjob= int(data_json.get('maxjob'))
              print(f'{cyan}BẮT ĐẦU CHẠY',end='\r')
              print('--------------------------------------------------------------------')
              sleep(1)
              if select_job==1:
                getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
              else:
                getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
          except json.JSONDecodeError:
              print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại định dạng JSON trong tệp.")

