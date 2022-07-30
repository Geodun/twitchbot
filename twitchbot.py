import socket
import random
import time
from datetime import date
import config
import requests
import json
import fortuneteller
from howlongtobeatpy import HowLongToBeat

#connect to server
connection_data = ('irc.chat.twitch.tv', 6667)
token = config.TWITCH_TOKEN
user = config.USER
channel = "#brucewinless"
server = socket.socket()
server.connect(connection_data)
server.send(f"PASS {token}\n".encode('utf-8'))
server.send(f"NICK {user}\n".encode('utf-8'))
server.send(f"JOIN {channel}\n".encode('utf-8'))

#play count to marbles
play = 0

#allow list for triggers
allowlist = ["geodun","dondums","captainclaire_","mimibunnymoon","missmaryTV"]

while True:

    #recieve message
    message = (server.recv(2048).decode('utf-8'))
    print(message)

    #extract user and message data in an ineficient way
    chatter_placement = message.find("!")
    chatter = message[1:chatter_placement].strip().lower()
    content_placement = message.find(":",1)
    content = message[content_placement+1:].strip().lower()

    #check for twitch timeout response
    if "PING" in message:
        server.send(bytes("PONG\r\n", "UTF-8"))

    if ("time to beat:" in content) and (chatter in allowlist):
        time.sleep(5)
        answer_placement = content.find(":")
        answer = content[answer_placement+1:].strip()
        
        results_list = HowLongToBeat().search(answer)
        try:
            server.send(bytes("PRIVMSG " + channel + " :" + "To beat "+results_list[0].game_name+" it takes "+results_list[0].gameplay_main+" hours for the main game, "+results_list[0].gameplay_main_extra+" hours for main + extra, and "+results_list[0].gameplay_completionist+" hours for a completionsist playthrough.\r\n", "UTF-8"))
        except IndexError as err:
            server.send(bytes("PRIVMSG " + channel + " :" + "game not found\r\n", "UTF-8"))

    if ("oh magic conch shell" in content) and (chatter in allowlist):
        answer = fortuneteller.magicConchShell()
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "Magic Conch: "+ answer +"\r\n", "UTF-8"))

    if ("can i get a tarot reading" in content) and (chatter in allowlist):
        answer = fortuneteller.draw(3)
        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" + "Yes, let's see. The first card: "+answer[0].description()+". This card represents what you can do to surrender to the change in your life. Your second card: "+answer[1].description()+". This card offers direction on caring for yourself during this process.  May you find guidance in this final card: "+answer[2].description()+". I wish you well in your journey ahead.\r\n", "UTF-8"))

    if ("what is today's horoscope for: " in content) and (chatter in allowlist):
        sign_placement = content.find(":")
        sign = content[sign_placement+1:].strip()

        querystring = {"sign":sign,"day":"today"}

        headers = {
	        "X-RapidAPI-Key": config.RAPIDAPI_KEY,
	        "X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
        }

        response = requests.request("POST", "https://sameer-kumar-aztro-v1.p.rapidapi.com/", headers=headers, params=querystring)
        #convert response to dictionary
        response = json.loads(response.text)

        time.sleep(5)
        server.send(bytes("PRIVMSG " + channel + " :" +"The horoscope for "+sign+" on "+response['current_date']+" is: "+response['description']+" Your luck number is "+response['lucky_number']+".\r\n", "UTF-8"))

    if "fortune for" in message and (chatter in allowlist):

        if "fortune for bruce" in message:
            time.sleep(5)
            server.send(bytes("PRIVMSG " + channel + " :" +"bruce ded\r\n", "UTF-8"))
        else:
            fortune = fortuneteller.getFortune()
            time.sleep(5)
            server.send(bytes("PRIVMSG " + channel + " :" + fortune +"\r\n", "UTF-8"))

    #marbles check
    if "!play" in content:
        play = play + 1
        if play > 10:
            time.sleep(random.randint(3,10))
            server.send(bytes("PRIVMSG " + channel + " :" + "!play\r\n", "UTF-8"))
            play = 0
            time.sleep(120)

    
