from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import random
from colorama import Fore, Style, Back

Lucky = """

█▀▄▀█ ▄▀█ █▀ ▀█▀ █▀▀ █▀█  
█░▀░█ █▀█ ▄█ ░█░ ██▄ █▀▄  

▄▀█ ▀█▀  
█▀█ ░█░  

█▀▄ ▄▀█ █▀█ █▄▀ █▄▄ █▀█ ▀█▀
█▄▀ █▀█ █▀▄ █░█ █▄█ █▄█ ░█░
"""

logo = """


▒█▀▀▄ ░█▀▀█ ▒█▀▀█ ▒█░▄▀ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 
▒█░▒█ ▒█▄▄█ ▒█▄▄▀ ▒█▀▄░ ▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
▒█▄▄▀ ▒█░▒█ ▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░
"""
Lucky_hu_bc = """
⚡ 𝙼𝙰𝚂𝚃𝙴𝚁 𝙰𝚃 ᴇʟʟɪᴘᴘsʙᴏᴛ 🔥        


"""
print("")
print(Style.BRIGHT + Fore.MAGENTA + LUCKY)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.CYAN + logo)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.RED + Back.BLUE + Lucky_hu_bc)
print("""𝙼𝙰𝙳𝙴 𝙱𝚈 ʟᴜᴄᴋʏ 𝚆𝙸𝚃𝙷 𝙼𝙸𝙽𝙳""")
print(Style.RESET_ALL)
print("""Welcome To EllipsBot String Session Generator By @sarcasticlucky\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @DARK_Bot_Support For Any Help!\n\n",
            )

            print(
                "Thanks for Choosing EllipsBot Have A Good Time....Note That When You Terminate the old Session then Come Back And Generate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +918925534834! Kindly Retry"
        )
        print("")
        continue
    break
