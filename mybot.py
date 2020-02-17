from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from key_file import key
import logging

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
'usrlib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, 
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(f'Привет {update.message.chat.first_name}! Ты написал {update.message.text}')
    print(user_text)
    logging.info('User: %s, Chat id: %s, Message: %s',
                update.message.chat.username,
                update.message.chat.chat.id,
                update.message.text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(key, request_kwargs=PROXY)

    logging.info('Бот запускается.')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) 
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()


