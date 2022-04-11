from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
from telethon.tl.functions.channels import JoinChannelRequest
import csv
import time
import keyboard
import random
import pyfiglet
from colorama import init, Fore
import os
import pickle
import traceback
'''
try:
    import beepy
except ImportError:
    if os.name == 'nt':
        os.system('pip install beepy')
    else:
        pass
'''
init()

r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '(' + w + 'i' + lg + ')' + rs
error = lg + '(' + r + '!' + lg + ')' + rs
success = w + '(' + lg + '*' + w + ')' + rs
INPUT = lg + '(' + cy + '~' + lg + ')' + rs
plus = lg + '(' + w + '+' + lg + ')' + rs
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('Telegram')
    print(random.choice(colors) + logo + rs)
    print(f'{r}   Versiyon: {w}4.1 {r}| Yapımcı: {w}ArdaBarut{rs}')


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
global scraped_grp
with open('zhedef.txt', 'r') as f:
    scraped_grp = f.readline()
f.close()

clr()
banner()
users = []
input_file = 'members\\members.csv'
with open(input_file, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f, delimiter=',', lineterminator='\n')
    next(reader, None)
    for row in reader:
        user = {}
        user['username'] = row[0]
        user['user_id'] = row[1]
        user['access_hash'] = row[2]
        user['group'] = row[3]
        user['group_id'] = row[4]
        users.append(user)
accounts = []
f = open('zhesap.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break
print('\n' + info + lg + ' Tüm hesaplar için oturumlar oluşturuluyor...' + rs)
for a in accounts:
    iD = int(a[0])
    Hash = str(a[1])
    phn = str(a[2])
    clnt = TelegramClient(f'sessions\\{phn}', iD, Hash)
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            code = input(f'{INPUT}{lg} için kod girin {w}{phn}{cy}["s" bas il]:{r}')
            if 's' in code:
                accounts.remove(a)
            else:
                clnt.sign_in(phn, code)
        except PhoneNumberBannedError:
            print(f'{error}{w}{phn} {r}banlanmış!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print('\n'+info+lg+'Banlanmış hesap kaldırıldı'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' Oturum oluşturuldu!')
time.sleep(2)
print(f'{plus}{lg} Herkese açık grubun tam kullanıcı adını girin{w}[@ olmadan]')
g = input(f'{INPUT}{lg} Kullanıcı adı[Örn: deneme01]: {r}')
group = 't.me/' + str(g)
#print('\n')
print(f'{info}{lg} Tüm hesaplardan katılım sağlanıyor...{rs}')
for account in accounts:
    api_id = int(account[0])
    api_hash = str(account[1])
    phone = str(account[2])
    client = TelegramClient(f'sessions\\{phone}', api_id, api_hash)
    client.connect()
    try:
        username = client.get_entity(group)
        client(JoinChannelRequest(username))
        print(f'{success}{lg} Giriliyor {phone}')
    except:
        print(f'{error}{r} Girilirken Hata Oluştu {phone}')
        accounts.remove(account)
    client.disconnect()
time.sleep(2)
clr()
number = len(accounts)
print(f'{info}{lg} Toplam Hesaplar: {w}{number}')
print(f'{info}{lg} 10 dan fazla hesabınız varsa, bir seferde 10 kullanmanız önerilir.')
a = int(input(f'{plus}{lg} Kullanılacak hesap sayısını girin: {r}'))
to_use = []
print(f'\n{info}{lg} CSV dosyaları dağıtılıyor...{rs}')
time.sleep(2)
for i in accounts[:a]:
    done = []
    to_use.append(i)
    file = 'members\\members' + str(accounts.index(i)) + '.csv'
    with open(file, 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
        for user in users[:60]:
            writer.writerow([user['username'], user['user_id'], user['access_hash'], user['group'], user['group_id']])
            done.append(user)
    f.close()
    del_count = 0
    while del_count != len(done):
        del users[0]
        del_count += 1
    if len(users) == 0:
        break
if not len(users) == 0:
    with open('members\\members.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
        for user in users:
            writer.writerow([user['username'], user['user_id'], user['access_hash'], user['group'], user['group_id']])
    f.close()
    m = str(len(users))
    print(f'{info}{lg} Remaining {m} users stored in {w}members.csv')
for acc in to_use:
    accounts.remove(acc)
with open('zhesap.txt', 'wb') as f:
    for acc in accounts:
        pickle.dump(acc, f)
    for k in to_use:
        pickle.dump(k, f)
    f.close()

#with open('resume.txt', 'w') as f:
#    f.write(scraped_grp)
#    f.close()

print(f'{info}{lg} CSV dosyası dağıtımı tamamlandı{rs}')
time.sleep(2)
clr()
if not os.name == 'nt':
    print(f'{error}{r}Otomasyon yalnızca Windows sistemlerini destekler')
    sys.exit()

program = 'usradder.py'
o = str(len(to_use))
print(f'\n{info}{r} Bu tamamen otomatik olacaktır.')
print(f'{info}{r} Program Açılırken CMD den baska yere girmeyin.')
input(f'\n{plus}{lg} Devam etmek için enter a basın...{rs}')
print(f'\n{info}{lg} Başlatılıyor {o} hesap ile...{rs}\n')
for i in range(5, 0, -1):
    print(random.choice(colors) + str(i) + rs)
    time.sleep(1)
for account in to_use:
    api_id = str(account[0])
    api_hash = str(account[1])
    phone = str(account[2])
    file = 'members\\members' + str(to_use.index(account)) + '.csv'
    os.system('start cmd')
    time.sleep(1.5)
    keyboard.write('python' + ' ' + program + ' ' + api_id + ' ' + api_hash + ' ' + phone + ' ' + file + ' ' + group + ' ' + str(scraped_grp))
    keyboard.press_and_release('Enter')
    print(f'{plus}{lg} Başlatıldı {phone}')
#beepy.beep(sound='ping')
