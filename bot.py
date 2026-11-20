
import os
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("☎️ Get Number", callback_data="number"),
            InlineKeyboardButton("💳 Withdraw", callback_data="withdraw")
        ],
        [
            InlineKeyboardButton("👤 Referral", callback_data="referral"),
            InlineKeyboardButton("📊 Live Traffic", callback_data="traffic")
        ],
        [
            InlineKeyboardButton("🏆 Top User", callback_data="top"),
            InlineKeyboardButton("💬 Support", callback_data="support")
        ],
        [
            InlineKeyboardButton("📥 OTP Download", callback_data="otp"),
            InlineKeyboardButton("🎁 Bulk Number", callback_data="bulk")
        ]
    ]

    await update.message.reply_text(
        "🐯 Welcome to SA Tiger Bot!\n\nSelect an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "number": "Authorized number services.",
        "withdraw": "Withdraw request coming soon.",
        "referral": f"Your Telegram ID: {query.from_user.id}",
        "traffic": "Traffic statistics coming soon.",
        "top": "Top users coming soon.",
        "support": "Contact support.",
        "otp": "Authorized verification services only.",
        "bulk": "Bulk management coming soon."
    }

    await query.edit_message_text(messages.get(query.data, "Welcome!"))

async def main():
    token = os.environ["BOT_TOKEN"]

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    print("SA Tiger Bot is running!")

    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped.")
