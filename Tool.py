import aiohttp, asyncio, os, sys, time ##By Team-77
import requests, threading, json, hashlib ##By Team-77
from colorama import Fore, Back, Style ##By Team-77
 ##By Team-77
 ##By Team-77
with open('config.json') as config_file: ##By Team-77
    config = json.load(config_file) ##By Team-77
     ##By Team-77
token = config["token"] ##By Team-77
hook = config["webhook"] ##By Team-77
guild = config["guild"] ##By Team-77
message = config["message"] ##By Team-77
list = config["url"] ##By Team-77
 ##By Team-77
delay = 0 ##By Team-77
os.system("cls" if os.name == "nt" else "clear") ##By Team-77
 ##By Team-77
def print01(text): ##By Team-77
    for c in text: ##By Team-77 ##By Team-77
        sys.stdout.write(c) ##By Team-77
        sys.stdout.flush() ##By Team-77
        time.sleep(0.015) ##By Team-77
 ##By Team-77
 ##By Team-77
print01(Fore.GREEN + "Updated by Team-77" + Fore.RESET + "\n") ##By Team-77
time.sleep(0.5) ##By Team-77
print01(Fore.GREEN + """ 
[-] Hey dir;\n[-] You are now using snipe Vanity URL(s) sniping.\n[!] It Made by "Team-77"\n[!] And developed by "Team-77"\n\n""") ##By Team-77
time.sleep(0.05) ##By Team-77
 ##By Team-77
 ##By Team-77
async def notify(session, url, jsonxd): ##By Team-77
    async with session.post(url, json=jsonxd) as response: #اذا مش = حط ناقص
        return response.status ##By Team-77
 ##By Team-77 ##By Team-77
async def claim(session, url, jsonxd): ##By Team-77
    async with session.patch(url, json=jsonxd) as response: #اذا مش = حط ناقص
        return response.status ##By Team-77
 ##By Team-77
async def fetch(session, url): ##By Team-77
    async with session.get(url) as response: ##By Team-77
        return response.status, response.text, response.json() ##By Team-77
 ##By Team-77
async def main(): ##By Team-77
    os.system("cls" if os.name == "nt" else "clear") ##By Team-77
    async with aiohttp.ClientSession(headers={"Authorization": token, "X-Audit-Log-Reason": "By Team-77"}, connector=None) as session: ##By Team-77
        async with session.get("https://canary.discord.com/api/v9/users/@me") as response: ##By Team-77
          if response.status in (200, 201, 204): ##By Team-77
            user = await response.json() #اذا مش = حط ناقص
            id = user["id"] ##By Team-77
            username = user["username"] ##By Team-77
            print("Logged in as () | {}".format (username, id)) ##By Team-77
          elif response.status == 429: ##By Team-77
            print("[-] Connection fai ##By Team-77ed to discord websocket, this ip rate limited") ##By Team-77
            sys.exit() ##By Team-77
          else: ##By Team-77
            await notify(session, hook, {"content": "**failed to connect to discord websocket.**\n\n"}) ##By Team-77
            print("Bad Auth") ##By Team-77
            sys.exit() ##By Team-77
        await notify(session, hook, {"content": "**Sniping in progess : `%s`\n\n: `Developer: Team-77`**" % str(list)}) ##By Team-77
        for x in range(50): ##By Team-77
            for vanity in list: ##By Team-77
                idk, text, jsonxd = await fetch(session, 'https://canary.discord.com/api/v9/invites/%s' % vanity) ##By Team-77
                if idk == 404: ##By Team-77
                    idk2 = await claim(session, 'https://canary.discord.com/api/v9/guilds/%s/vanity-url' % (guild), {"code": vanity}) ##By Team-77
                    if idk2 in (200, 201, 204): ##By Team-77
                        await notify(session, hook, {"content": message % vanity}) ##By Team-77
                        sys.exit() ##By Team-77
                    else: ##By Team-77
                        await notify(session, hook, {"content": "**failed to claim %s **\n\n" % (vanity)}) ##By Team-77
                        sys.exit() ##By Team-77
                elif idk == 200: ##By Team-77
                    print(Fore.GREEN + "By Team-77 Sniping: {%s}" % (vanity)) ##By Team-77
                    await asyncio.sleep(delay) ##By Team-77
                    continue ##By Team-77
                elif idk == 429: ##By Team-77
                    #print()
                    await notify(session, hook, {"content": "**Rate limited sleeping...**"}) ##By Team-77
                    print("[-] Rate Limited") ##By Team-77
                    if 'retry_after' in text: ##By Team-77
                      time.sleep(int(jsonxd['retry_after'])) ##By Team-77
                    else: ##By Team-77
                      sys.exit() ##By Team-77
                else: ##By Team-77
                    print("[-] Unknown Error") ##By Team-77
                    sys.exit() ##By Team-77
 ##By Team-77
 ##By Team-77
loop = asyncio.get_event_loop() ##By Team-77
loop.run_until_complete(main()) ##By Team-77
