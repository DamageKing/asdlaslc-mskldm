import asyncio
import os
import sys
import random
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PasswordHashInvalidError, PhoneNumberInvalidError
from telethon.network import ConnectionTcpAbridged
from telethon.utils import get_display_name
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon import functions, types
import requests
import bs4
from telethon import sessions
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetDiscussionMessageRequest
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
from telethon.tl.functions.account import UpdateProfileRequest
import pickle, pyfiglet
from colorama import init, Fore
import os, random
from time import sleep
from os import listdir
from random import choice
import time
init()

lg = Fore.LIGHTGREEN_EX
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
r = Fore.RED
n = Fore.RESET
colors = [lg, r, w, cy, ye]

def banner():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('TELEGRAM')
    print(f'{random.choice(colors)}{banner}{n}')
    print(r+'  Versiyon: 4.1 | Yapımcı: ArdaBarut'+n+'\n')


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    #print(r)
    banner()
    #print(n)
    print(cy+'[1] Yeni Hesap Ekle'+n)
    print(cy+"[2] Toplu Hesap Ekleyici")
    print(cy+'[3] Banlı Hesapları Filtrele'+n)
    print(cy+'[4] Tüm Hesapları Listele'+n)
    print(cy+'[5] Spesifik Hesapları Sil'+n)
    print(cy+'[6] Yorum Botu'+n)
    print(cy+"[7] Otomatik Api Al")
    print(cy+'[8] Çık')
    a = int(input(lg+f'\nSeçiniz: {r}'))
    if a == 1:
        with open('zhesap.txt', 'ab') as g:
            newly_added = []
            while True:
                a = input(f"\n{lg}Giriniz API ID (Varsayılan için w bas): {r}")
                if (a=='w'):
                    a = ("12553173")
                b = str(input(f'{lg}Giriniz API Hash (Varsayılan için w bas): {r}'))
                if (b=="w"):
                    b = str("98528f7b9b50a90535c736120a46e073")
                c = str(input(f'{lg}Telefon numarası girin: {r}'))
                p = ''.join(c.split())
                pickle.dump([a, b, p], g)
                newly_added.append([a, b, p])
                ab = input(f'\nYeni hesap eklemek istermisiniz?[y/n]: ')
                if 'y' in ab:
                    pass
                else:
                    clr()
                    print('\n'+lg+'[i] Hesaplar kaydediliyor'+n)
                    g.close()
                    sleep(3)
                    clr()
                    print(lg + '[i] Hesaplara giriş yapılıyor...\n')
                    print()
                    print(ye+'Api ID: ',a)
                    print(ye+'Api Hash: ',b)
                    print(lg)
                    for added in newly_added:
                        c = TelegramClient(f'sessions/{added[2]}', added[0], added[1])
                        try:
                            c.start()
                            print(f'n\n{lg}[+] Giriş Yapıldı - {added[2]}')
                            c.disconnect()
                        except PhoneNumberBannedError:
                            print(f'{r}[!] {added[2]} banlanmış! Seçenek 2 yi kullanarak filtreleyin')
                            continue
                        print('\n')
                    input(f'\n{lg}Ana menüye gitmek için enter a basın...')
                    break
        g.close()
    elif a==2:
        with open('zhesap.txt', 'ab') as g:
            newly_added = []
            while True:
                a = ("12553173")
                b = str("98528f7b9b50a90535c736120a46e073")
                c = str(input(f'{lg}Telefon numarası girin: {r}'))
                p = ''.join(c.split())
                pickle.dump([a, b, p], g)
                newly_added.append([a, b, p])
                ab = input(f'\nYeni hesap eklemek istermisiniz?[y/n]: ')
                if 'y' in ab:
                    pass
                else:
                    clr()
                    print('\n'+lg+'[i] Hesaplar kaydediliyor'+n)
                    g.close()
                    sleep(3)
                    clr()
                    print(lg + '[i] Hesaplara giriş yapılıyor...\n')
                    print()
                    print(lg)
                    for added in newly_added:
                        c = TelegramClient(f'sessions/{added[2]}', added[0], added[1])
                        try:
                            c.start()
                            print(f'n\n{lg}[+] Giriş Yapıldı - {added[2]}')
                            c.disconnect()
                        except PhoneNumberBannedError:
                            print(f'{r}[!] {added[2]} banlanmış! Seçenek 2 yi kullanarak filtreleyin')
                            continue
                        print('\n')
                    input(f'\n{lg}Ana menüye gitmek için enter a basın...')
                    break    
    elif a == 3:
        accounts = []
        banned_accs = []
        h = open('zhesap.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Hesap yok! Ekleyin ve tekrar deneyin')
            sleep(3)
        else:
            for account in accounts:
                api_id = int(account[0])
                api_hash = str(account[1])
                phone = str(account[2])
                client = TelegramClient(f'sessions\\{phone}', api_id, api_hash)
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        client.sign_in(phone, input('[+] Kodu Giriniz: '))
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' banlanmış!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Tebrikler! Yasaklanmış hesap yok')
                input('\nAna menüye gitmek için enter a basın')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('zhesap.txt', 'wb') as k:
                    for a in accounts:
                        Id = a[0]
                        Hash = a[1]
                        Phone = a[2]
                        pickle.dump([Id, Hash, Phone], k)
                k.close()
                print(lg+'[i] Banlanmış hesaplar kaldırıldı'+n)
                input('\nAna menüye gitmek için enter a basın')
    elif a == 4:
        display = []
        j = open('zhesap.txt', 'rb')
        while True:
            try:
                display.append(pickle.load(j))
            except EOFError:
                break
        j.close()
        print(f'\n{lg}')
        print(f'API ID  |            API Hash              |    Numara')
        print(f'==========================================================')
        i = 0
        for z in display:
            print(f'{z[0]} | {z[1]} | {z[2]}')
            i += 1
        print(f'==========================================================')
        input('\nAna menüye gitmek için entera basın')

    elif a == 5:
        accs = []
        f = open('zhesap.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Silmek için bir hesap seçin\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[2]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Bir seçim giriniz: {n}'))
        phone = str(accs[index][2])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('zhesap.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Hesap Silindi! {n}')
        input(f'{lg}Ana menuye donmek icin enter a basın{n}')
        f.close()
    elif a == 6:
        nick = input("@ olmadan grup giriniz örn:[deneme01]: ")
        def sendo_m(session, message, msgid):
            try:
                client  = TelegramClient("sessions/" + session, "2462520", "e073b57a2a0541608c3f1373bf22ea09")
                client.connect()

                result = client(GetDiscussionMessageRequest(
                        peer= (nick),
                        msg_id=int(msgid)
                    ))

            
                a = result.messages[0]
                print(f"{session} - {message}")
                client.send_message(a.peer_id, message=message, reply_to=a)
        
            except Exception as e:
                print(f"HATA: {e}")
                time.sleep(3)
                return sendo_m(session, message, msgid)


        def send_messages(messages: list, accounts: str, count: int):
            msgid = input("Mesaj id           : ")
            sure =  input("kaç saniye beklensin: ")

            for i in range(count):

                session = choice(accounts)
                message = choice(messages)

                messages.remove(message)
                accounts.remove(session)

                sendo_m(session, message, msgid)
                time.sleep(int(sure))


        cmts   = input("Yorum dosyası      : ")
        yorum  = input("Kaç adet yollansın : ")

        sess = []
        for i in listdir("sessions"):
            if i.endswith(".session"):
                sess.append(i)

        send_messages([i.replace("\n", "") for i in open(cmts, "r", encoding="utf-8").readlines()], sess, int(yorum))



        """ n = open("names.txt", "r", encoding="utf-8").readlines()
        for i in listdir("sessions"):
            client  = TelegramClient("sessions/" + i, "2462520", "e073b57a2a0541608c3f1373bf22ea09")
            client.connect()

            r = client(UpdateProfileRequest(first_name=n.pop(0).replace("\n", ""), last_name=""))

            print(r.stringify())
        """

    elif a==7:
        numara = input("[?] Telefon Numaranız: ")
        try:
            rastgele = requests.post("https://my.telegram.org/auth/send_password", data={"phone": numara}).json()["random_hash"]
        except:
            print("[!] Kod Gönderilemedi. Telefon Numaranızı Kontrol Ediniz.")
            exit(1)
        
        sifre = input("[?] Telegram'dan Gelen Kodu Yazınız: ")
        try:
            cookie = requests.post("https://my.telegram.org/auth/login", data={"phone": numara, "random_hash": rastgele, "password": sifre}).cookies.get_dict()
        except:
            print("[!] Büyük İhtimal Kodu Yanlış Yazdınız. Lütfen Yazılımı Yeniden Başlatın.")
            exit(1)
        app = requests.post("https://my.telegram.org/apps", cookies=cookie).text
        soup = bs4.BeautifulSoup(app, features="html.parser")

        if soup.title.string == "Create new application":
            print("[i] Uygulamanız Yok. Oluşturuluyor...")
            hashh = soup.find("input", {"name": "hash"}).get("value")
            AppInfo = {
                "hash": hashh,
                "app_title":"Telegram Yazılımı",
                "app_shortname": "tgyazilim" + str(random.randint(9, 99)) + str(time.time()).replace(".", ""),
                "app_url": "",
                "app_platform": "android",
                "app_desc": ""
            }
            app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text
            print(app)
            print("[i] Uygulama başarıyla oluşturuldu!")
            print("[i] API ID/HASH alınıyor...")
            newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
            newsoup = bs4.BeautifulSoup(newapp, features="html.parser")

            g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
            app_id = g_inputs[0].string
            api_hash = g_inputs[1].string
            print()
            print(lg+"[i] Bilgiler Getirildi! Lütfen Bunları Not Ediniz.\n\n")
            print(ye+f"[i] API ID: {app_id}")
            print(ye+f"[i] API HASH: {api_hash}")
            try:
                stringonay = int(input("[?] String Almak İster Misiniz? [Evet için 1 Yazınız]: "))
            except:
                print("[!] Lütfen Sadece Sayı Yazınız!")

            if stringonay == 1:
                client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
                print("[i] String Keyiniz Aşağıdadır!\n\n\n" + client.session.save())
            else:
                print("[i] Script Durduruluyor...")
                exit(1)
        elif  soup.title.string == "App configuration":
            print("[i] Halihazır da Uygulama Oluşturmuşsunuz. API ID/HASH Çekiliyor...")
            g_inputs = soup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
            app_id = g_inputs[0].string
            api_hash = g_inputs[1].string
            print(lg+"[i] Bilgiler Getirildi! Lütfen Bunları Not Ediniz.\n\n")
            print(ye+f"[i] API ID: {app_id}")
            print(ye+f"[i] API HASH: {api_hash}")
            sleep(300)
        else:
            print("[!] Bir Hata Oluştu.")
            exit(1)

    if a == 8:
        clr()
        banner()
        quit()