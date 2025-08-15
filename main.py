import os
import logging
from telegram.ext import Application, CommandHandler
from flask import Flask, jsonify
from threading import Thread

# Flask для health checks
app = Flask(__name__)
@app.route('/health')
def health_check():
    return jsonify({"status": "ok"}), 200

# Проверка токена
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("❌ Укажите BOT_TOKEN в настройках Render!")

async def start(update, context):
    await update.message.reply_text("Бот работает с новым токеном!")

def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    # Запуск Flask в фоне
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    # Запуск бота
    run_bot()