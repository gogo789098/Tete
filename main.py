
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import openai
import os

# مفاتيح API
TELEGRAM_TOKEN = "7846025677:AAGaVtZG1BImOpVnWmRuThVI9sz3v6q3ktQ"
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

# إعداد السجلات
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً! أرسل الأمر /image متبوعًا بوصف الصورة.")

# /image command
async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("يرجى إرسال وصف بعد الأمر /image، مثل: /image قطة في الفضاء")
        return

    await update.message.reply_text("جارٍ إنشاء الصورة...")

    try:
        response = openai.Image.create(prompt=prompt, n=1, size="512x512")
        image_url = response['data'][0]['url']
        await update.message.reply_photo(photo=image_url)
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("image", generate_image))
    app.run_polling()
