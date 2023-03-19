import aiohttp, asyncio, os, sys, time
import requests, threading, json, hashlib
from colorama import Fore, Back, Style


with open('config.json') as config_file:
    config = json.load(config_file)
    
token = config["token"]
hook = config["webhook"]
guild = config["guild"]
message = config["message"]
list = config["url"]

delay = 0
os.system("cls" if os.name == "nt" else "clear")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


print01(Fore.GREEN + "Updated by Team-77" + Fore.RESET + "\n")
time.sleep(0.5)
print01(Fore.GREEN + """
[-] Hey dir;\n[-] You are now using snipe Vanity URL(s) sniping.\n[!] It Made by "Team-77"\n[!] And developed by "Team-77"\n\n""")
time.sleep(0.05)


async def notify(session, url, jsonxd):
    async with session.post(url, json=jsonxd) as response: #اذا مش = حط ناقص
        return response.status

async def claim(session, url, jsonxd):
    async with session.patch(url, json=jsonxd) as response: #اذا مش = حط ناقص
        return response.status

async def fetch(session, url):
    async with session.get(url) as response:
        return response.status, response.text, response.json()

async def main():
    os.system("cls" if os.name == "nt" else "clear")
    async with aiohttp.ClientSession(headers={"Authorization": token, "X-Audit-Log-Reason": "By Team-77"}, connector=None) as session:
        async with session.get("https://canary.discord.com/api/v9/users/@me") as response:
          if response.status in (200, 201, 204):
            user = await response.json() #اذا مش = حط ناقص
            id = user["id"]
            username = user["username"]
            print("Logged in as () | {}".format (username, id))
          elif response.status == 429:
            print("[-] Connection failed to discord websocket, this ip rate limited")
            sys.exit()
          else:
            await notify(session, hook, {"content": "**failed to connect to discord websocket.**\n\n"})
            print("Bad Auth")
            sys.exit()
        await notify(session, hook, {"content": "**Sniping in progess : `%s`\n\n: `Developer: Team-77`**" % str(list)})
        for x in range(50):
            for vanity in list:
                idk, text, jsonxd = await fetch(session, 'https://canary.discord.com/api/v9/invites/%s' % vanity)
                if idk == 404:
                    idk2 = await claim(session, 'https://canary.discord.com/api/v9/guilds/%s/vanity-url' % (guild), {"code": vanity})
                    if idk2 in (200, 201, 204):
                        await notify(session, hook, {"content": message % vanity})
                        sys.exit()
                    else:
                        await notify(session, hook, {"content": "**failed to claim %s **\n\n" % (vanity)})
                        sys.exit()
                elif idk == 200:
                    print(Fore.GREEN + "By Team-77 Sniping: {%s}" % (vanity))
                    await asyncio.sleep(delay)
                    continue
                elif idk == 429:
                    #print()
                    await notify(session, hook, {"content": "**Rate limited sleeping...**"})
                    print("[-] Rate Limited")
                    if 'retry_after' in text:
                      time.sleep(int(jsonxd['retry_after']))
                    else:
                      sys.exit()
                else:
                    print("[-] Unknown Error")
                    sys.exit()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
