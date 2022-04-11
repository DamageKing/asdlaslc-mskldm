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

lg = Fore.LIGHTGREEN_EX
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
r = Fore.RED
ns = Fore.RESET
colors = [lg, r, w, cy, ye]

n = open("names.txt", "r", encoding="utf-8").readlines()
for i in listdir("sessions"):
    client  = TelegramClient("sessions/" + i, "2462520", "e073b57a2a0541608c3f1373bf22ea09")
    client.connect()

    r = client(UpdateProfileRequest(first_name=n.pop(0).replace("\n", ""), last_name=""))
        
    print(lg+f"[+] Hesap İsmi Değiştirildi"+ns)
    #print(r.stringify())
