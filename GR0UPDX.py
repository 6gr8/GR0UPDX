import telebot
from telebot.types import Message, ChatPermissions

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message: Message):
    if message.chat.type == "private":
        bot.reply_to(message, (
        "👋 **Thanks for using the GR0UPDX Bot!**\n\n"
        "This bot can help you manage your group , Here are the commands you can use:\n"
        "\n"
        "1️⃣ Pin Messages /pin 📌\n"
        "2️⃣ Mute Users /mute 🔇\n"
        "3️⃣ Unmute Users /unmute 🔊\n"
        "4️⃣ Kick Users /kick 👥\n\n"
        "Add the bot as an admin ⚙️\n"
        "Coded By MrDeNsor | Source code In My Github : 6gr8"
    ))
    else:
        print("MEWO")
@bot.message_handler(commands=['kick'])
def kick(message: Message):
    chatid = message.chat.id
    if message.chat.type == "private":
        bot.reply_to(message, f"Add Me In Group..")
    else:
        userid = message.from_user.id
        member = bot.get_chat_member(chatid, userid)
        if member.status == 'administrator' or member.status == 'creator':
            userM = message.reply_to_message.from_user.id
            bot.kick_chat_member(message.chat.id, userM)
            bot.reply_to(message, "User kicked !")
        else:
            bot.reply_to(message, "You are not an admin in this group.")
    
@bot.message_handler(commands=['pin'])
def pin(message: Message):
    chatid = message.chat.id
    if message.chat.type == "private":
        bot.reply_to(message, f"Add Me In Group..")
    else:
        
        checkbot = bot.get_chat_member(chatid, bot.get_me().id)
        if not (checkbot.status == 'administrator' or checkbot.status == 'creator'):
            bot.reply_to(message, "I am not an admin in this group !!")
        else:
            userid = message.from_user.id
            member = bot.get_chat_member(chatid, userid)
            if member.status == 'administrator' or member.status == 'creator':
                if message.reply_to_message:
                    bot.pin_chat_message(chatid, message.reply_to_message.message_id)
                    bot.reply_to(message, "Done !")
                else:
                    bot.reply_to(message, "Reply to the message you want to pin using /pin!")
            else:
                bot.reply_to(message, "You are not an admin in this group.")

@bot.message_handler(commands=['mute'])
def mute(message: Message):
    chatid = message.chat.id
    if message.chat.type == "private":
        bot.reply_to(message, f"Add Me In Group ..")
    else:
        checkbot = bot.get_chat_member(chatid, bot.get_me().id)
        if not (checkbot.status == 'administrator' or checkbot.status == 'creator'):
            bot.reply_to(message, "I am not an admin in this group !!")
        else:
            try:
                userid = message.from_user.id
                member = bot.get_chat_member(chatid, userid)
                if member.status == 'administrator' or member.status == 'creator':
                    if message.reply_to_message:
                        userM = message.reply_to_message.from_user.id
                        bot.restrict_chat_member(
                            chatid, 
                            userM, 
                            permissions=ChatPermissions(can_send_messages=False)
                            )
                        bot.reply_to(message, "User muted !")
                    else:
                        bot.reply_to(message, "Reply to the user you want to mute using /mute!")
                else:
                    bot.reply_to(message, "You are not an admin in this group.")
            except:
                bot.reply_to(message, "Error.")

@bot.message_handler(commands=['unmute'])
def unmute(message: Message):
    chatid = message.chat.id
    
    if message.chat.type == "private":
        bot.reply_to(message, f"Add Me In Group ..")
    else:
        checkbot = bot.get_chat_member(chatid, bot.get_me().id)
        if not (checkbot.status == 'administrator' or checkbot.status == 'creator'):
            bot.reply_to(message, "I am not an admin in this group !!")
        else:
            userid = message.from_user.id
            member = bot.get_chat_member(chatid, userid)
            if member.status == 'administrator' or member.status == 'creator':
                if message.reply_to_message:
                    userM = message.reply_to_message.from_user.id
                    bot.restrict_chat_member(
                        chatid, 
                        userM, 
                        permissions=ChatPermissions(can_send_messages=True, can_send_media_messages=True)
                        )
                    bot.reply_to(message, "User unmuted !")
                else:
                    bot.reply_to(message, "Reply to the user you want to unmute using /unmute!")
            else:
                bot.reply_to(message, "You are not an admin in this group.")
bot.polling()
