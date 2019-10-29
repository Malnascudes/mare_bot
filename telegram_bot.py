from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import random
import logging

updater = Updater(token='1061747586:AAGzaVExHeaLcHpqUhoxCuwAVzpwTxeCmvc', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

mare_messages = ["Pues dar una vuelta, avanzar en el curso del trabajo y si puedo leer",
                 "Y estar con los abuelos que eso ya es un trabajo!!! Pobrecillos cada vez estan mas mayores",
                 "Pero necesitan también mucho cariño",
                 "Tu no te preocupes qye estoy bien\nSi en unos dias n se te va pasando pido cita",
                 "Cuidate mucho mi niño",
                 "Te quiero mucho",
                 "Estoy bien, dentro de que he tenido una operación",
                 "Que tengas un dia fenomenal!!!",
                 "😘"]

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola, soy la teva Mare. ¿Cómo estás?")

# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def mares_talking(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(mare_messages))

# def caps(update, context):
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Calla y hazme caso. Deja las barritas.")
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# echo_handler = MessageHandler(Filters.text, echo)
# dispatcher.add_handler(echo_handler)

mare_talk_handler = MessageHandler(Filters.text, mares_talking)
dispatcher.add_handler(mare_talk_handler)

# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.start_polling()
