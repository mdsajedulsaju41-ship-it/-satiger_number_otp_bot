from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("☎️ Get Number", callback_data="number"),
         InlineKeyboardButton("💳 Withdraw", callback_data="withdraw")],
        [InlineKeyboardButton("👤 Referral", callback_data="referral"),
         InlineKeyboardButton("📊 Live Traffic", callback_data="traffic")],
        [InlineKeyboardButton("🏆 Top User", callback_data="top"),
         InlineKeyboardButton("💬 Support", callback_data="support")],
        [InlineKeyboardButton("👤 My Profile", callback_data="profile")]
    ]
    await update.message.reply_text(
        "Welcome to SA Tiger Bot 🐯\n\nSelect an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "number": "Contact admin for authorized number services.",
        "withdraw": "Withdraw requests will be available soon.",
        "referral": f"Your Telegram ID: {query.from_user.id}",
        "traffic": "Traffic statistics coming soon.",
        "top": "Top users coming soon.",
        "support": "Please contact the administrator.",
        "profile": f"Your ID: {query.from_user.id}"
    }

    await query.edit_message_text(messages.get(query.data, "Welcome!"))

def main():
    import os
    token = os.environ["BOT_TOKEN"]
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
