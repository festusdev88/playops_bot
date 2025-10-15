from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
STICKER_LINK = os.getenv("STICKER_LINK")

if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN not set in .env")

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        status = getattr(member, "status", None)
        if status in ("member", "administrator", "creator"):
            bot.send_message(chat_id, f"✅ Verified — here is your sticker pack:\n{STICKER_LINK}")
        else:
            bot.send_message(chat_id, f"⚠️ Please join {CHANNEL_USERNAME} then send /start again.")
    except Exception as e:
        bot.send_message(chat_id, "⚠️ Could not verify membership. Make sure the bot is added to the channel as admin.")
        print("get_chat_member error:", e)

if __name__ == "__main__":
    print("🤖 Bot is running...")
    bot.polling(non_stop=True)
