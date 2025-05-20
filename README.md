
# Telegram AI Image Bot

بوت تلغرام يقوم بتوليد صور باستخدام الذكاء الاصطناعي (OpenAI DALL·E).

## طريقة التشغيل

1. ثبت المتطلبات:
```bash
pip install -r requirements.txt
```

2. شغّل البوت:
```bash
python main.py
```

## الأوامر المتاحة

- `/start` — للترحيب.
- `/image [وصف]` — لإنشاء صورة بناءً على وصفك.

مثال:
```
/image أسد يطير في السماء
```

## النشر على Render

1. ارفع هذا المشروع إلى GitHub.
2. ادخل إلى [https://render.com](https://render.com) واختر "New Web Service".
3. اربط مستودع GitHub.
4. اختر:
   - **Environment:** Python 3
   - **Start Command:** `python main.py`
