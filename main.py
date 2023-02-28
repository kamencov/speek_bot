from gtts import gTTS
import telebot
from API_Token import Token_API
from pydub import AudioSegment
from pydub.effects import speedup

bot = telebot.TeleBot(Token_API)

user_message = ''

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот! Напиши что-нибудь!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    user_message = message.text
    bot.send_message(message.chat.id, 'Скоро файл тебе пришлет бот. Пожалуйста подождите')
    speech = gTTS(text=user_message, lang="ru")
    name = f"{message.chat.id}.mp3"
    speech.save(name)
    with open(name, 'rb') as file:
        audio = AudioSegment.from_mp3(file)
        
        # настраиваем скорость речи
        new_file = speedup(audio, 1.2, 120)
        
        # name_new.mp3 - пишем название файла который будет по итогу.
        new_file.export("name_new.mp3", format="mp3")
        name_2 = "name_new.mp3"
        
        with open(name_2, 'rb') as file_2:
            bot.send_document(message.chat.id, file_2)


if __name__ == "__main__":
    bot.polling()
