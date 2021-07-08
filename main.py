import os
API_KEY = os.getenv('API_KEY')
import telebot
import requests
import string
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hello'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
  
  file_id = message.photo[2].file_id
  file_info = bot.get_file(file_id)
  print(file_info)
  file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_KEY, file_info.file_path))
  open(file_id+'.png','wb').write(file.content)
  
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
  
  file_id = message.audio.file_id
  file_name = message.audio.file_name
  url = file_name.replace(" ", "");
  file_info = bot.get_file(file_id)
  print(file_name)
  file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_KEY, file_info.file_path))
  open(url,'wb').write(file.content)
  print (url)
  bot.reply_to(message,'https://replit.com/@MojtabaAzizi/telegramBot#'+url)
bot.polling()
