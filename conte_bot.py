from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, CallbackContext

import os
import random

random.seed(2022)
PORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ["TOKEN"]

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Ohi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Nessuno può aiutarti, nemmeno io!')

def dicci_qualcosa(update: Update, context: CallbackContext) -> None:
    """Send a message of your choice."""
    if update.message.text == '1':
        context.bot.send_message(message_id = update.message.message_id,
                             chat_id = update.message.chat_id,
                             text = 'Old')
    elif update.message.text == '2':
        context.bot.send_message(message_id = update.message.message_id,
                             chat_id = update.message.chat_id,
                             text = u'\U0001F611')
    elif update.message.text == '3':
        context.bot.send_message(message_id = update.message.message_id,
                             chat_id = update.message.chat_id,
                             text = u'\U0001F644')
    elif update.message.text == '4':
        context.bot.send_message(message_id = update.message.message_id,
                             chat_id = update.message.chat_id,
                             text = 'Moggi era innocente! \U0001F624')
    elif update.message.text == '5':
        context.bot.send_message(message_id = update.message.message_id,
                             chat_id = update.message.chat_id,
                             text = 'L\'ho fatto/visto/sentito/scoperto/mangiato/visitato prima io!')
    elif update.message.text == '6':
        context.bot.send_message(message_id = update.message.message_id,
                             chat_id = update.message.chat_id,
                             text = 'Eh vabbè...')
    else:
        context.bot.send_message(message_id = update.message.message_id,
                             chat_id = update.message.chat_id,
                             text = 'Non ci penso proprio! \U0001F624')


def lamentati(update: Update, context: CallbackContext) -> None:
    """Send a random message."""
    sentences = [
        'Mi rifiuto di parlare di calcio con voi che non ne sapete un ca**o! \U0001F624',
        'Mi rifiuto di parlare con gente che non sa cosa significhi "pleonastico" \U0001F624',
        'La pizza napoletana mi ha stufato... a Milano esiste solo quella... \U0001F624',
        'Non ho mai detto che la De Filippi sia bella, è una legenda metropolitana! \U0001F624',
        'Quando lavoravo per il tizio di FI mi avete isolato tutti... \u2639\uFE0F'
    ]
    context.bot.send_message(message_id = update.message.message_id,
                            chat_id = update.message.chat_id,
                            text = random.choice(sentences))



def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler('dicci_qualcosa', dicci_qualcosa))
    dp.add_handler(CommandHandler('lamentati', lamentati))
    
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://ilconte.herokuapp.com/' + TOKEN)
    
    updater.idle()


if __name__ == '__main__':
    main()