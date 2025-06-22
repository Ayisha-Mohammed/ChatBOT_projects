from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import token

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, World"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("hello", hello))

    print("Bot is running... Send /hello to your bot on Telegram.")
    app.run_polling()

