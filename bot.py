import os

import telebot
from dotenv import load_dotenv
from google import genai

from src.gemini_service import generate_professional_prompt


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Create Gemini client
client = genai.Client(
    api_key=GEMINI_API_KEY
)


# Create Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🤖 Welcome to Prompt Generator!\n\n"
        "Send me your requirement and I will "
        "generate a professional AI prompt."
    )


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "📝 Send me your requirement.\n\n"
        "Example:\n"
        "Create a Spring Boot REST API for user registration."
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):

    user_input = message.text

    bot.send_message(
        message.chat.id,
        "⏳ Generating your prompt..."
    )

    try:

        generated_prompt = generate_professional_prompt(
            client=client,
            model="gemini-2.5-flash",
            level="Advanced",
            category="Coding",
            tone="Professional",
            user_input=user_input
        )

        bot.send_message(
            message.chat.id,
            generated_prompt
        )

    except Exception as e:

        print("ERROR:", repr(e))

        bot.send_message(
            message.chat.id,
            f"❌ Error: {str(e)}"
        )

print("Bot is running...")

bot.infinity_polling()