import discord
import random
import time
import requests
from discord.ext import commands
def gmail(receiver_email,message) :
    password = 'h2o29h2o12'
    import smtplib, ssl
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "h2odiscordbot@gmail.com"  # Enter your address
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
def pewds():
    r = requests.get("https://bastet.socialblade.com/youtube/lookup?query=" + "UC-lHJZR3Gqxm24_Vd_AJ5Yw")
    r = r.content
    if r[0] == 'b' :
        r = r[1:]
    return int(r)
def meme():
    r = requests.get("https://some-random-api.ml/meme")
    r = r.content
    r = str(r)
    if r[0] == 'b' :
        r = r[1:]
    r = r[18:]
    rl = ''
    for i in r :
        if i == '"' :
            break
        rl+=i
    return(rl)
def tseries():
    r = requests.get("https://bastet.socialblade.com/youtube/lookup?query=" + "UCq-Fj5jknLsUf-MWSy4_brA")
    r = r.content
    if r[0] == 'b' :
        r = r[1:]
    return int(r)
kits = ['triggerman','hunter','rocket launcher','spray and pray','semi auto','run and gun','vince','detective','agent','runner']
client = commands.Bot(command_prefix = '*')
def getresponse(talk) :
    r = requests.get("https://some-random-api.ml/chatbot/?message="+talk)
    r = r.content
    print(r)
    if r[0] == 'b' :
        r = r[1:]
    resp = str(r)
    print(resp)
    resp = resp[15:-3]
    return(resp)
@client.event
async def on_ready() :
    print('Bot is ready')

@client.event
async def on_message(message) :
    sent = message.content
    id = client.get_guild(544099615268667402)
    if message.content.find('*random') != -1:
        await message.channel.send(random.choice(kits))
    if message.content.find('*pewds') != -1 :
        print('Pewds : '+str(pewds())+'      T-series : '+str(tseries())+'       Subgap : '+str(int(str(pewds()))-int(str(tseries()))))
        await message.channel.send('Pewds : '+str(pewds())+'      T-series : '+str(tseries())+'       Subgap : '+str(int(str(pewds()))-int(str(tseries()))))
    if message.content.find('*meme') != -1 :
        em = discord.Embed()
        em.set_image(url=str(meme()))
        await message.channel.send(embed=em)
    if message.content.find('*test') != -1:
        print(message)
    if message.content.find('*talk') != -1 :
        talk = ''
        print(sent)
        start = False
        for i in sent :
            if i == 'k' and start == False :
                start = True
            elif start == True :
                talk+=i
        talk = talk[1:]
        print(talk)
        rep = getresponse(talk)
        print(rep)
        await message.channel.send(rep)
    if message.content.find('*gay') != -1 :
        st = False
        gid = ''
        for i in str(message.mentions) :
            if st == True and i == ' ' :
                break
            if i == '=' :
                st = True
            elif st == True:
                gid+=i
        print(gid)
        em = discord.Embed()
        em.set_image(url=gid)
        await message.channel.send(embed=em)
    if message.content.find('*gmail') != -1:
        to = ''
        cou = 0
        for i in sent[12:] :
            cou+=1
            if i != ' ' :
                to+=i
            else :
                break
        gmail(to,sent[17+cou:])
        await message.channel.send('gmail '+ str(sent[17+cou:]) + ' sent to '+str(to))
    if message.content.find('*help') != -1:
        await message.channel.send(''' ```Commands :
                                           
        random- says a random kit 
        
        pewds- displays pewdiepie and tseries subcount + subgap
                  
        meme- random meme
        
        talk- you can talk to the bot.
              note: this is still BETA which means
              he is highly autistic although he says he isn't.
              While talking you have to be carfull about writing and watch
              out about question marks.
              
              EXAMPLE: *talk Hello!
        
        gmail- sends gmail to someone. Can be used for trolls.
                Do *gmail send:EMAIL RECIEVER text:YOUR TEXT HERE
                
        MORE COMING SOON    ``` ''')
client.run('NTY4NzQyNTQzNDg3OTI2Mjcy.XLmhZQ.vFGf7eZjxdlO_k-OVXG7cOEJeIE')
