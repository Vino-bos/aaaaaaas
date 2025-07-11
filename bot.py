
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json, os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", 0))

# load DB
db_path = "db.json"
if os.path.exists(db_path):
    with open(db_path, "r") as f:
        db = json.load(f)
else:
    db = {
        "payment_link": "https://lynk.id/pixelmarttt/9nvw7d644n4l/checkout?token=cGFyYW1zPSU1QiU1RCZiaWRfcHJpY2U9MCZxdHlfcHJvZD0x",
        "groups": {}
    }

def save_db():
    with open(db_path, "w") as f:
        json.dump(db, f, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    token = args[0] if args else "info"

    if token == "info":
        await update.message.reply_text(
            f"💳 Silakan lakukan pembayaran di link berikut:\n{db['payment_link']}\n\n"
            "Setelah itu klik link konfirmasi yang kamu dapatkan setelah pembayaran."
        )
    elif token in db["groups"]:
        await update.message.reply_text(
            f"✅ Terima kasih, berikut link grup kamu:\n{db['groups'][token]}"
        )
    else:
        await update.message.reply_text("❌ Token konfirmasi tidak dikenal.")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("⛔ Hanya owner yang bisa menambahkan.")
        return

    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Format: /add <token_konfirmasi> <link_grup>")
        return

    token, link_grup = args[0], args[1]
    db["groups"][token] = link_grup
    save_db()

    bot_user = await context.bot.get_me()
    await update.message.reply_text(
        f"✅ Token konfirmasi dibuat!\n\n"
        f"Bagikan ke pembeli:\nhttps://t.me/{bot_user.username}?start={token}"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.run_polling()

if __name__ == "__main__":
    main()
