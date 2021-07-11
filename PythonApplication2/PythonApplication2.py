import telebot

token='1834677175:AAGMX-eXrKddPBVKqzz0P4FbskWwCqqKr9c'
bot = telebot.TeleBot(token)
GROUP_ID=1001174068521
blacklist=['курьер']
blacklist=['подработка']
@bot.message_handler(content_types=["text"])
def handle_text(message):
    for x in blacklist:
        if(x in message.text):
            bot.delete_message(message.chat.id, message.message_id)
        else:
            pass
        
if __name__ == "__main__":
    bot.infinity_polling()
