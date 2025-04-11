import logging
import os
import telegram
from telegram.ext import Updater, CommandHandler

# إعدادات البوت
TOKEN = "7807395933:AAFtsYTkiTHUGilo_T3c1i94qxEC55o594E"
IMAGE_URL = "https://i.ibb.co/7bqbs7v/skull.png"

# إعدادات التسجيل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# بدء التشغيل
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=IMAGE_URL, caption="""
زوج: EUR/USD (OTC)
الاتجاه: صعود
المدة: 1 دقيقة
التحليل: كسر مقاومة قوية + ترند صاعد + مؤشر RSI فوق 70
ادخل الصفقة بعد دقيقة واحدة من الآن.

(سنقوم بإرسال نتيجة الصفقة بعد انتهائها)
""")
    # إرسال نتيجة تجريبية بعد دقيقة (اختباريًا فقط)
    context.job_queue.run_once(lambda ctx: ctx.bot.send_message(chat_id=chat_id, text="نتيجة الصفقة: ربح ✅"), 60)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()