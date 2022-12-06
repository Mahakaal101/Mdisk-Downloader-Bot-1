import os
import threading
import subprocess
import time

import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.errors import FloodWait
import asyncio
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from upgrade import upgrade
import mdisk
import extras
import mediainfo
import split
from split import TG_SPLIT_SIZE
import datetime
from datetime import timedelta, date ,datetime
from datetime import date as date_
from helper.progress import humanbytes
from helper.date import add_date ,check_expi
from pyrogram.file_id import FileId
from helper.database import daily as daily_ ,uploadlimit,usertype,addpre,find_one,used_limit,getid,delete,insert,find_one,usertype,addpredata
ADMIN = int(os.environ.get("ADMIN", 1864861524))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


# app
bot_token = os.environ.get("TOKEN", "5953337678:AAF_thoIHSNewztUnvA--rs95At2BCs-wq8") 
api_hash = os.environ.get("HASH", "ad762fe0516f367115ba651d929cf429") 
api_id = os.environ.get("ID", "17737898")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)


# optionals
auth = os.environ.get("AUTH", "623741973,1864861524,5076949930,5215205205,1787835645,306027849,683684279,1406840926,1667559069,597718002,1843393081,5316294458,721234444,5290630238,839291568,598394386,1606667548,1740456929,5634994558,1764976688,1051220816,915679851,5410723702,1335978271,1845343032,1252277288,5226656959,507644392,1198027788,981149750,5058416849,5016754348,904971137,1911731554,1838349598,631028443,1740456929,5674356680,2083663200,5515158923,1057959919,941092630,5397438805,809970451,859879486,1303200779,1324651168,240296058,1252277288,635819536,5490092364,1726415542,5104293442")
ban = os.environ.get("BAN", "")


# start command
@app.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	try:
	    id = message.text.split(' ')[1]
	except:
	    await message.reply_text(text =f"""
Hi {message.from_user.first_name } 👋
I'm Paid Mdisk Uploader Bot 🚀\nPermanent Thumbnail Support💯\n
Send me a Mdisk link and \nI will upload it to telegram as a file/video.\n
Please /upgrade Your Subscription
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", url='https://t.me/Aaajats')
           ],[
           InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/anumitultrabots'),
           InlineKeyboardButton('🍂 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/anumitultrabots')
           ],[
           InlineKeyboardButton('🍃 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
           InlineKeyboardButton('ℹ️ Subscribe 🧐', url='https://youtube.com/@anumitultrabots')
           ]]
          )
       )

# upgrade command
@app.on_message(filters.private & filters.command(["upgrade"]))
async def start(client,message):
	await message.reply_text(text =f"""
	Hello \n
	🛡️ PLAN 🛡️\n
	🌸Daily  Upload  limit Unlimited\n
	🌸Price Rs 40 🇮🇳/🌎 1$  per Month__
	
	💸Pay Using Upi I'd \nultrabots.famc@idfcbank\n
	💸Pay Using qr code send /qr command\n
	💸After Payment Send Screenshots Of\nPayment To Admin
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Aaajats")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/ajak4406")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
       )
    
#plans command
@app.on_message(filters.private & filters.command(["plans"]))
async def start(client,message):
	await message.reply_text("""
	PAID PLANS AVAILABLE\n
	🛡️ PLAN 🛡️\n
	🌸Daily  Upload  limit Unlimited
	🌸Price Rs 40 🇮🇳/🌎 1$  per Month__
	🌸No Timeout\n
Please /upgrade your subscription
	""")
	
# qr code
@app.on_message(filters.private & filters.command(["qr"]))
async def start(client,message):
	await message.reply_photo("https://telegra.ph/file/fddcc0ebfc76cb9d05a5f.jpg"),


#total user
@app.on_message(filters.private & filters.command('total'))
async def sts(c, m):
    ids = getid()
    tot = len(ids)
    await m.reply_text(text=f"Total user(s) {tot}", quote=True)

#addpremium user

@app.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("VIP 1",callback_data = "vip1"), 
        			InlineKeyboardButton("VIP 2",callback_data = "vip2") ]]))
        			

@app.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 21474836480
	uploadlimit(int(user_id),21474836480)
	usertype(int(user_id),"VIP1")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 20 GB")
	await bot.send_message(user_id,"Hey Ur Upgraded To VIP 1 check your plan here /myplan")

@app.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 107374182400
	uploadlimit(int(user_id),107374182400)
	usertype(int(user_id),"VIP2")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 100 GB")
	await bot.send_message(user_id,"Hey Ur Upgraded To VIP 2 check your plan here /myplan")

	
#broadcast
@app.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   success = 0 
   failed = 0 
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	time.sleep(1)
     	await message.reply_to_message.copy(id)
     	success += 1 
     except:
     	failed += 1
     	delete({"_id":id})     	 
     	pass
     try:
     	await ms.edit( f"Message sent to {success} chat(s). {failed} chat(s) failed on receiving message. \nTotal - {tot}" )
     except FloodWait as e:
     	await asyncio.sleep(t.x)


# my plan

@app.on_message(filters.private & filters.command(["myplan"]))
async def start(client,message):
	used_ = find_one(message.from_user.id)	
	daily = used_["daily"]
	expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
	if expi != 0:
	     today = date_.today()
	     pattern = '%Y-%m-%d'
	     epcho = int(time.mktime(time.strptime(str(today), pattern)))
	     daily_(message.from_user.id,epcho)
	     used_limit(message.from_user.id,0)
	_newus = find_one(message.from_user.id)
	used = _newus["used_limit"]
	limit = _newus["uploadlimit"]
	remain = int(limit)- int(used)
	user =  _newus["usertype"]
	ends = _newus["prexdate"]
	if ends == None:
	    text = f"User ID:- ```{message.from_user.id}```\nPlan :- {user}\nDaly Upload Limit :- {humanbytes(limit)}\nToday Used :- {humanbytes(used)}\nRemain:- {humanbytes(remain)}"
	else:
	    normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
	    text = f"User ID:- ```{message.from_user.id}```\nPlan :- {user}\nDaly Upload Limit :- {humanbytes(limit)}\nToday Used :- {humanbytes(used)}\nRemain:- {humanbytes(remain)}\n\n```Your Plan Ends On :- {normal_date}"
	    
	if user == "Free":
	    await message.reply(text,quote = True,reply_markup = InlineKeyboardMarkup([[       			InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade"), InlineKeyboardButton("Cancel ✖️ ",callback_data = "cancel") ]]))
	else:
	    await message.reply(text,quote=True)

			 
# check for user access
def checkuser(message):
    if auth != "" or ban != "":
        valid = 1
        if auth != "":
            authusers = auth.split(",")
            if str(message.from_user.id) not in authusers:
                valid = 0
        if ban != "":
            bannedusers = ban.split(",")
            if str(message.from_user.id) in bannedusers:
                valid = 0
        return valid        
    else:
        return 1


# download status
def status(folder,message,fsize):
    fsize = fsize / pow(2,20)
    length = len(folder)
    # wait for the folder to create
    while True:
        if os.path.exists(folder + "/vid.mp4.part-Frag0") or os.path.exists(folder + "/vid.mp4.part"):
            break
    
    time.sleep(3)
    while os.path.exists(folder + "/" ):
        result = subprocess.run(["du", "-hs", f"{folder}/"], capture_output=True, text=True)
        size = result.stdout[:-(length+2)]
        try:
            app.edit_message_text(message.chat.id, message.id, f"__Downloaded__ : **{size} **__of__**  {fsize:.1f}M**")
            time.sleep(10)
        except:
            time.sleep(5)
#about

@app.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("📛 My Name : @renamerprov2_bot\n\n👨‍💻Creater :- @ajak4405\n\n🧿 Language :Python 3.10.8\n\n📢 Framework :Pyrogram 2.0.63\n\n🤖 Bot Server : VPS")

# upload status
def upstatus(statusfile,message):
    while True:
        if os.path.exists(statusfile):
            break

    time.sleep(3)      
    while os.path.exists(statusfile):
        with open(statusfile,"r") as upread:
            txt = upread.read()
        try:
            app.edit_message_text(message.chat.id, message.id, f"__Uploaded__ : **{txt}**")
            time.sleep(10)
        except:
            time.sleep(5)


# progress writter
def progress(current, total, message):
    with open(f'{message.id}upstatus.txt',"w") as fileup:
        fileup.write(f"{current * 100 / total:.1f}%")


# download and upload
def down(message,link):

    # checking link and download with progress thread
    msg = app.send_message(message.chat.id, '__Downloading__', reply_to_message_id=message.id)
    size = mdisk.getsize(link)
    if size == 0:
        app.edit_message_text(message.chat.id, msg.id,"__**Invalid Link**__")
        return
    sta = threading.Thread(target=lambda:status(str(message.id),msg,size),daemon=True)
    sta.start()

    # checking link and download and merge
    file,check,filename = mdisk.mdow(link,message)
    if file == None:
        app.edit_message_text(message.chat.id, msg.id,"__**Invalid Link**__")
        return

    # checking if its a link returned
    if check == -1:
        app.edit_message_text(message.chat.id, msg.id,f"__**Can't Download File but here is the Download Link : {file}**__")
        os.rmdir(str(message.id))
        return

    # checking size
    size = split.get_path_size(file)
    if(size > TG_SPLIT_SIZE):
        app.edit_message_text(message.chat.id, msg.id, "__Splitting__")
        flist = split.split_file(file,size,file,".", TG_SPLIT_SIZE)
        os.remove(file) 
    else:
        flist = [file]
    app.edit_message_text(message.chat.id, msg.id, "__Uploading__")
    i = 1

    # checking thumbline
    if not os.path.exists(f'{message.from_user.id}-thumb.jpg'):
        thumbfile = None
    else:
        thumbfile = f'{message.from_user.id}-thumb.jpg'

    # upload thread
    upsta = threading.Thread(target=lambda:upstatus(f'{message.id}upstatus.txt',msg),daemon=True)
    upsta.start()
    info = extras.getdata(str(message.from_user.id))

    # uploading
    for ele in flist:

        # checking file existence
        if not os.path.exists(ele):
            app.send_message(message.chat.id,"**Error in Merging File**",reply_to_message_id=message.id)
            return
            
        # check if it's multi part
        if len(flist) == 1:
            partt = ""
        else:
            partt = f"__**part {i}**__\n"
            i = i + 1

        # actuall upload
        if info == "V":
                thumb,duration,width,height = mediainfo.allinfo(ele,thumbfile)
                app.send_video(message.chat.id, video=ele, caption=f"{partt}**{filename}**", thumb=thumb, duration=duration, height=height, width=width, reply_to_message_id=message.id, progress=progress, progress_args=[message])
                if "-thumb.jpg" not in thumb:
                    os.remove(thumb)
        else:
                app.send_document(message.chat.id, document=ele, caption=f"{partt}**{filename}**", thumb=thumbfile, force_document=True, reply_to_message_id=message.id, progress=progress, progress_args=[message])
        
        # deleting uploaded file
        os.remove(ele)
        
    # checking if restriction is removed    
    if check == 0:
        app.send_message(message.chat.id,"__Can't remove the **restriction**, you have to use **MX player** to play this **video**\n\nThis happens because either the **file** length is **too small** or **video** doesn't have separate **audio layer**__",reply_to_message_id=message.id)
    if os.path.exists(f'{message.id}upstatus.txt'):
        os.remove(f'{message.id}upstatus.txt')
    app.delete_messages(message.chat.id,message_ids=[msg.id])


# mdisk command
@app.on_message(filters.private & filters.command(["start"]))
def mdiskdown(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return

    try:
        link = message.text.split("mdisk ")[1]
        if "https://mdisk.me/" in link:
            d = threading.Thread(target=lambda:down(message,link),daemon=True)
            d.start()
            return 
    except:
        pass

    app.send_message(message.chat.id, '**Send only __MDisk Link__ with command followed by the link**',reply_to_message_id=message.id)


# thumb command
@app.on_message(filters.private & filters.command(["thumb"]))
def thumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return

    try:
        if int(message.reply_to_message.document.file_size) > 200000:
            app.send_message(message.chat.id, '**Thumbline size allowed is < 200 KB**',reply_to_message_id=message.id)
            return

        msg = app.get_messages(message.chat.id, int(message.reply_to_message.id))
        file = app.download_media(msg)
        os.rename(file,f'{message.from_user.id}-thumb.jpg')
        app.send_message(message.chat.id, '**Thumbnail is Set**',reply_to_message_id=message.id)

    except:
        app.send_message(message.chat.id, '**reply __/thumb__ to a image document of size less than 200KB**',reply_to_message_id=message.id)


# show thumb command
@app.on_message(filters.private & filters.command(["show"]))
def showthumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return
    
    if os.path.exists(f'{message.from_user.id}-thumb.jpg'):
        app.send_photo(message.chat.id,photo=f'{message.from_user.id}-thumb.jpg',reply_to_message_id=message.id)
    else:
        app.send_message(message.chat.id, '**Thumbnail is not Set**',reply_to_message_id=message.id)


# remove thumbline command
@app.on_message(filters.private & filters.command(["remove"]))
def removethumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return
    
    
    if os.path.exists(f'{message.from_user.id}-thumb.jpg'):
        os.remove(f'{message.from_user.id}-thumb.jpg')
        app.send_message(message.chat.id, '**Thumbnail is Removed**',reply_to_message_id=message.id)
    else:
        app.send_message(message.chat.id, '**Thumbnail is not Set**',reply_to_message_id=message.id)


# thumbline
@app.on_message(filters.photo)
def ptumb(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return
    
    file = app.download_media(message)
    os.rename(file,f'{message.from_user.id}-thumb.jpg')
    app.send_message(message.chat.id, '**Thumbnail is Set**',reply_to_message_id=message.id)
    

# change mode
@app.on_message(filters.private & filters.command(["change"]))
def change(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return
    
    info = extras.getdata(str(message.from_user.id))
    extras.swap(str(message.from_user.id))
    if info == "V":
        app.send_message(message.chat.id, '__Mode changed from **Video** format to **Document** format__',reply_to_message_id=message.id)
    else:
        app.send_message(message.chat.id, '__Mode changed from **Document** format to **Video** format__',reply_to_message_id=message.id)

        
# multiple links handler
def multilinks(message,links):
    for link in links:
        d = threading.Thread(target=lambda:down(message,link),daemon=True)
        d.start()
        d.join()


# mdisk link in text
@app.on_message(filters.text)
def mdisktext(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    
    if not checkuser(message):
        app.send_message(message.chat.id, """
	Your ARE NOT A PAID USER\n
Please /upgrade your subscription
	""",reply_to_message_id=message.id)
        return

    if "https://mdisk.me/" in message.text:
        links = message.text.split("\n")
        if len(links) == 1:
            d = threading.Thread(target=lambda:down(message,links[0]),daemon=True)
            d.start()
        else:
            d = threading.Thread(target=lambda:multilinks(message,links),daemon=True)
            d.start()   
    else:
        app.send_message(message.chat.id, '**Send only __MDisk Link__**',reply_to_message_id=message.id)


# polling
app.run()
