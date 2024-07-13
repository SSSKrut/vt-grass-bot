import time
import telebot
from config.settings import BOT_TOKEN
from management.commands.start import start_command
from management.commands.flower import send_flower

bot = telebot.TeleBot(BOT_TOKEN)

bot.register_message_handler(
    lambda message: start_command(message, bot), commands=["start"]
)
bot.register_message_handler(
    lambda message: send_flower(message, bot), commands=["flower"]
)


def handle_exception(e: Exception):
    print(e)


bot_running = True


@bot.message_handler(commands=["stop"])
def stop_bot(message) -> None:
    global bot_running
    bot_running = False


while bot_running:
    try:
        bot.polling()
    except Exception as e:
        handle_exception(e)
        time.sleep(5)
