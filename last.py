import requests,re
from telebot import TeleBot, types
import time
import telebot
import os
import timedelta
import user_agent
import telebot
import random
import time
from datetime import datetime, timedelta
from telebot import types
import json
import os
from collections import defaultdict
import telebot
from bs4 import BeautifulSoup
import telebot
import telebot
import random
import time
from datetime import datetime, timedelta
from telebot import types
from telebot import types
from telethon import TelegramClient
import asyncio
try:
    import telebot
except:
    import os
    os.system("pip install pyTelegramBotAPI")
from telebot import *
from gate7 import Tele
from colorama import Fore
sto = {"stop": False}  # To control the stopping of the checking process
token = "7385888101:AAFv-Y4ox7nPSsw1mh-a1T9CggCE1WJnnWU"
id = 6898845629
bot=telebot.TeleBot(token,parse_mode="HTML")
owner_id = 6898845629  # استبدل بمعرف المالك الخاص بك
admin_id = 6898845629
admin_list = []  # قائمة الأدمن (يمكنك تخزينها في ملف لتكون دائمة)
bot_status = True  # حالة البوت، True يعني أن البوت يعمل، False يعني أنه مغلق

# وظيفة لحفظ قائمة الأدمن في ملف (لجعلها دائمة)
def save_admin_list():
    with open("admin_list.txt", "w") as file:
        for admin in admin_list:
            file.write(str(admin) + "\n")

# وظيفة لتحميل قائمة الأدمن من ملف (عند إعادة تشغيل البوت)
def load_admin_list():
    global admin_list
    if os.path.exists("admin_list.txt"):
        with open("admin_list.txt", "r") as file:
            admin_list = [int(line.strip()) for line in file]

# تحميل قائمة الأدمن عند تشغيل البوت
load_admin_list()

# كود /start: يعرض معلومات المستخدم بالإضافة إلى أزرار تحكم للمالك
@bot.message_handler(commands=["start"])
def user_info(message):
    global bot_status

    user_id  = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    image_url = "https://t.me/nxbdhsvsbxbc/3"  # استبدل هذا الرابط برابط الصورة على تيليجرام

    # إذا كان المستخدم هو المالك، إضافة أزرار التحكم
    if user_id == owner_id:
        keyboard = types.InlineKeyboardMarkup()
        stop_button = types.InlineKeyboardButton(text="𝗦𝘁𝗼𝗽 𝗧𝗵𝗲 𝗕𝗼𝘁 ⛔", callback_data="stop_bot")
        start_button = types.InlineKeyboardButton(text="𝗥𝘂𝗻 𝗧𝗵𝗲 𝗕𝗼𝘁 ✅", callback_data="start_bot")
        status_button_text = "𝗢𝗡 ✅" if bot_status else "𝗢𝗙𝗙 ❌"
        status_button = types.InlineKeyboardButton(text=status_button_text, callback_data="bot_status")
        add_admin_button = types.InlineKeyboardButton(text="➕ 𝗔𝗱𝗱 𝗡𝗲𝘄 𝗔𝗱𝗺𝗶𝗻", callback_data="add_admin")
        remove_admin_button = types.InlineKeyboardButton(text="❌ 𝗗𝗲𝗹𝗲𝘁𝗲 𝗔𝗱𝗺𝗶𝗻", callback_data="remove_admin")
        keyboard.add(stop_button, start_button, status_button, add_admin_button, remove_admin_button)
        bot.send_photo(
            message.chat.id,
            image_url,
            caption=f'''
• 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗚𝗼𝗸𝘂 𝗨𝗹𝘁𝗿𝗮 𝗜𝗻𝘀𝘁𝗶𝗻𝗰𝘁 𝗕𝗼𝘁

• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 : Braintree 11$

• 𝗨𝘀𝗲 /chk + 𝗰𝗰 𝗙𝗼𝗿 𝗦𝘁𝗮𝗿𝘁 𝗖𝗵𝗲𝗰𝗸
• 𝗬𝗼𝘂 𝗠𝘂𝘀𝘁 𝗕𝗲 𝗮 𝗩𝗜𝗣 𝗨𝗦𝗘𝗥

• 𝗬𝗼𝘂𝗿 𝗡𝗮𝗺𝗲 : {first_name}
• 𝗬𝗼𝘂𝗿 𝗜𝗗 : {user_id}
''', reply_markup=keyboard
        )
    else:
        # إذا كان البوت مغلقًا
        if not bot_status:
            bot.reply_to(message, "𝗧𝗵𝗲 𝗕𝗼𝘁 𝗶𝘀 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝗶𝗹𝘆 𝗖𝗹𝗼𝘀𝗲𝗱.")
        else:
            bot.send_photo(
                message.chat.id,
                image_url,
                caption=f'''
• 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗚𝗼𝗸𝘂 𝗨𝗹𝘁𝗿𝗮 𝗜𝗻𝘀𝘁𝗶𝗻𝗰𝘁 𝗕𝗼𝘁

• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 : Braintree 11$

• 𝗨𝘀𝗲 /chk + 𝗰𝗰 𝗙𝗼𝗿 𝗦𝘁𝗮𝗿𝘁 𝗖𝗵𝗲𝗰𝗸
• 𝗬𝗼𝘂 𝗠𝘂𝘀𝘁 𝗕𝗲 𝗮 𝗩𝗜𝗣 𝗨𝗦𝗘𝗥

• 𝗬𝗼𝘂𝗿 𝗡𝗮𝗺𝗲 : {first_name}
• 𝗬𝗼𝘂𝗿 𝗜𝗗 : {user_id}
'''
            )

# استقبال الضغطات على أزرار inline
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global bot_status

    if call.data == "stop_bot" and call.from_user.id == owner_id:
        # إيقاف البوت
        bot_status = False
        bot.send_message(call.message.chat.id, "𝗧𝗵𝗲 𝗕𝗼𝘁 𝗛𝗮𝘀 𝗕𝗲𝗲𝗻 𝗦𝘁𝗼𝗽𝗽𝗲𝗱. ❌")
        update_status_button(call.message)  # تحديث زر الحالة
    elif call.data == "start_bot" and call.from_user.id == owner_id:
        # تشغيل البوت
        bot_status = True
        bot.send_message(call.message.chat.id, "𝗧𝗵𝗲 𝗕𝗼𝘁 𝗛𝗮𝘀 𝗕𝗲𝗲𝗻 𝗔𝗰𝘁𝗶𝘃𝗮𝘁𝗲𝗱. ✅")
        update_status_button(call.message)  # تحديث زر الحالة
    elif call.data == "bot_status":
        # تحديث الحالة عند الضغط على زر الحالة
        status_message = "𝗢𝗡 ✅ " if bot_status else "𝗢𝗙𝗙 ❌ "
        bot.answer_callback_query(call.id, status_message)
    elif call.data == "add_admin" and call.from_user.id == owner_id:
        # إضافة أدمن جديد
        bot.send_message(call.message.chat.id, "𝗦𝗲𝗻𝗱 𝗔𝗱𝗺𝗶𝗻 𝗜𝗗.")
        bot.register_next_step_handler(call.message, process_admin_id)
    elif call.data == "remove_admin" and call.from_user.id == owner_id:
        # حذف أدمن
        bot.send_message(call.message.chat.id, "𝗦𝗲𝗻𝗱 𝗔𝗱𝗺𝗶𝗻 𝗜𝗗.")
        bot.register_next_step_handler(call.message, process_remove_admin)
    else:
        bot.answer_callback_query(call.id, "ليس لديك صلاحية لهذا الإجراء.")

# تحديث زر الحالة
def update_status_button(message):
    status_button_text = "✅ 𝗧𝗵𝗲 𝗕𝗼𝘁 𝗜𝘀 𝗪𝗼𝗿𝗸𝗶𝗻𝗴" if bot_status else "❌ 𝗧𝗵𝗲 𝗕𝗼𝘁 𝗜𝘀 𝗦𝘁𝗼𝗽"
    keyboard = types.InlineKeyboardMarkup()
    stop_button = types.InlineKeyboardButton(text="𝗦𝘁𝗼𝗽 𝗧𝗵𝗲 𝗕𝗼𝘁 ⛔", callback_data="stop_bot")
    start_button = types.InlineKeyboardButton(text="𝗥𝘂𝗻 𝗧𝗵𝗲 𝗕𝗼𝘁 ✅", callback_data="start_bot")
    status_button = types.InlineKeyboardButton(text=status_button_text, callback_data="bot_status")
    add_admin_button = types.InlineKeyboardButton(text="➕ 𝗔𝗱𝗱 𝗡𝗲𝘄 𝗔𝗱𝗺𝗶𝗻", callback_data="add_admin")
    remove_admin_button = types.InlineKeyboardButton(text="❌ 𝗗𝗲𝗹𝗲𝘁𝗲 𝗔𝗱𝗺𝗶𝗻", callback_data="remove_admin")
    keyboard.add(stop_button, start_button, status_button, add_admin_button, remove_admin_button)
    bot.edit_message_reply_markup(message.chat.id, message_id=message.message_id, reply_markup=keyboard)

# استقبال أيدي الأدمن الجديد وإضافته إلى القائمة
def process_admin_id(message):
    try:
        new_admin_id = int(message.text)  # تحويل النص إلى رقم
        admin_list.append(new_admin_id)
        save_admin_list()  # حفظ قائمة الأدمن في ملف
        bot.reply_to(message, f'''𝗧𝗵𝗲 𝗡𝗲𝘄 𝗔𝗱𝗺𝗶𝗻 𝗛𝗮𝘀 𝗕𝗲𝗲𝗻 𝗔𝗱𝗱𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆.
{new_admin_id}''')
    except ValueError:
        bot.reply_to(message, "⚠️ يرجى إرسال أيدي صالح!")

# استقبال معرف الأدمن لحذفه من القائمة
def process_remove_admin(message):
    try:
        remove_admin_id = int(message.text)  # تحويل النص إلى رقم
        if remove_admin_id in admin_list:
            admin_list.remove(remove_admin_id)
            save_admin_list()  # حفظ قائمة الأدمن بعد الحذف
            bot.reply_to(message, f'''𝗧𝗵𝗲 𝗔𝗱𝗺𝗶𝗻 𝗛𝗮𝘀 𝗕𝗲𝗲𝗻 𝗥𝗲𝗺𝗼𝘃𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆.
{remove_admin_id}''')
        else:
            bot.reply_to(message, "⚠️ هذا المعرف ليس في قائمة الأدمن.")
    except ValueError:
        bot.reply_to(message, "⚠️ يرجى إرسال معرف صالح!")

import logging
import requests
from telebot import TeleBot

# إعداد السجل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# إعدادات وكيل المستخدم لمحاكاة متصفح حقيقي
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# دالة لفحص الحماية في الموقع (CAPTCHA أو Cloudflare)
def check_protection(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if "captcha" in response.text.lower():
            return "Recaptcha موجودة"
        elif "cloudflare" in response.headers.get("Server", "").lower():
            return "Cloudflare موجودة"
        else:
            return "𝗡𝗼"
    except requests.RequestException:
        return "𝗖𝗮𝗻'𝘁 𝗔𝗰𝗰𝗲𝘀𝘀 𝗧𝗵𝗲 𝗪𝗲𝗯𝘀𝗶𝘁𝗲"

# دالة لفحص بوابة الدفع في الموقع
def check_payment_gateway(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # التحقق من وجود جميع بوابات الدفع
        if "stripe" in response.text.lower():
            return "Stripe"
        elif "braintree" in response.text.lower():
            return "Braintree"
        elif "paypal" in response.text.lower():
            return "PayPal"
        elif "square" in response.text.lower():
            return "Square"
        elif "authorize.net" in response.text.lower() or "authorize.net" in response.url.lower():
            return "Authorize.Net"
        elif "razorpay" in response.text.lower():
            return "Razorpay"
        elif "mollie" in response.text.lower():
            return "Mollie"
        elif "2checkout" in response.text.lower() or "verifone" in response.text.lower():
            return "2Checkout"
        elif "adyen" in response.text.lower():
            return "Adyen"
        elif "klarna" in response.text.lower():
            return "Klarna"
        elif "worldpay" in response.text.lower():
            return "Worldpay"
        elif "sagepay" in response.text.lower():
            return "SagePay"
        else:
            return "𝗨𝗻𝗸𝗻𝗼𝘄𝗻 𝗚𝗮𝘁𝗲𝘄𝗮𝘆"
    except requests.RequestException:
        return "𝗖𝗮𝗻'𝘁 𝗔𝗰𝗰𝗲𝘀𝘀 𝗧𝗵𝗲 𝗪𝗲𝗯𝘀𝗶𝘁𝗲 ❌"

# دالة لمعالجة الأمر /check
@bot.message_handler(commands=["check"])
def check_website(message):
    # استخراج الرابط من الرسالة
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "يرجى إدخال الرابط بعد الأمر /check")
        return

    url = args[1]

    # فحص الحماية وبوابة الدفع
    protection_status = check_protection(url)
    payment_gateway = check_payment_gateway(url)

    # إنشاء رسالة النتيجة
    result_message = f"""
بوابة الدفع: {payment_gateway}
حماية: {protection_status}
"""

    # إرسال النتيجة إلى المستخدم
    bot.reply_to(message, result_message)


    
@bot.message_handler(commands=["owner"])
def owner_info(message):
    owner_id = 6898845629  # The owner's ID
    owner_user = bot.get_chat(owner_id)
    username = owner_user.username
    first_name = owner_user.first_name
    bio = bot.get_chat(owner_id).bio if hasattr(bot.get_chat(owner_id), 'bio') else "No bio available"

    profile_pictures = bot.get_user_profile_photos(owner_id)
    
    info_message = f"""
Owner Info:
- ID: {owner_id}
- Name: {first_name}
- Username: @{username if username else 'Not set'}
- Bio: {bio}
"""

    if profile_pictures.total_count > 0:
        bot.send_photo(message.chat.id, profile_pictures.photos[0][0].file_id, caption=info_message)
    else:
        bot.send_message(message.chat.id, info_message)   
        
        
@bot.message_handler(commands=["id"])
def user_info(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    profile_pictures = bot.get_user_profile_photos(user_id)
    
    info_message = f"""
User Info:
- ID: {user_id}
- Name: {first_name} {last_name}
- Username: @{username if username else 'Not set'}
"""
    
    if profile_pictures.total_count > 0:
        bot.send_photo(message.chat.id, profile_pictures.photos[0][0].file_id, caption=info_message)
    else:
        bot.send_message(message.chat.id, info_message)        
        
        
import phonenumbers
from faker import Faker
from telegram.ext import CommandHandler

# دالة لتوليد بيانات وهمية بناءً على رمز الدولة
def generate_fake_data(country_code):
    country_code = country_code.lower()
    
    # قائمة بجميع الدول المدعومة
    country_mapping = {
        'ar': 'ar_AE',  # الإمارات (العربية)
        'au': 'en_AU',  # أستراليا
        'br': 'pt_BR',  # البرازيل
        'ca': 'en_CA',  # كندا
        'cn': 'zh_CN',  # الصين
        'de': 'de_DE',  # ألمانيا
        'dk': 'da_DK',  # الدنمارك
        'es': 'es_ES',  # إسبانيا
        'fi': 'fi_FI',  # فنلندا
        'fr': 'fr_FR',  # فرنسا
        'in': 'en_IN',  # الهند
        'it': 'it_IT',  # إيطاليا
        'jp': 'ja_JP',  # اليابان
        'kr': 'ko_KR',  # كوريا الجنوبية
        'mx': 'es_MX',  # المكسيك
        'nl': 'nl_NL',  # هولندا
        'no': 'nb_NO',  # النرويج
        'pl': 'pl_PL',  # بولندا
        'pt': 'pt_PT',  # البرتغال
        'ru': 'ru_RU',  # روسيا
        'sa': 'ar_SA',  # السعودية
        'se': 'sv_SE',  # السويد
        'tr': 'tr_TR',  # تركيا
        'uk': 'en_GB',  # المملكة المتحدة
        'us': 'en_US',  # الولايات المتحدة
        'za': 'en_ZA',  # جنوب أفريقيا
        'gr': 'el_GR',  # اليونان
        'ir': 'fa_IR',  # إيران
        'il': 'he_IL',  # إسرائيل
        'cz': 'cs_CZ',  # التشيك
        'hu': 'hu_HU',  # المجر
        'ro': 'ro_RO',  # رومانيا
        'sk': 'sk_SK',  # سلوفاكيا
        'ua': 'uk_UA',  # أوكرانيا
        'at': 'de_AT',  # النمسا
        'ch': 'de_CH',  # سويسرا
        'bg': 'bg_BG',  # بلغاريا
        'hr': 'hr_HR',  # كرواتيا
        'lt': 'lt_LT',  # ليتوانيا
        'si': 'sl_SI',  # سلوفينيا
        'vi': 'vi_VN',  # فيتنام
    }
    
    if country_code in country_mapping:
        locale = country_mapping[country_code]
        fake = Faker(locale)
        country = country_code.upper()
    else:
        return "Sorry, unsupported country code!"
    
    # توليد بيانات وهمية
    full_name = fake.name()
    street_address = fake.street_address()
    city = fake.city()
    state = fake.state()
    postal_code = fake.postcode()
    raw_phone_number = fake.phone_number()

    # تنسيق رقم الهاتف باستخدام مكتبة phonenumbers
    try:
        parsed_phone = phonenumbers.parse(raw_phone_number, country.upper())
        formatted_phone_number = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    except phonenumbers.phonenumberutil.NumberParseException:
        formatted_phone_number = raw_phone_number  # إذا لم ينجح التحليل، اعرض الرقم الخام

    # صياغة الرسالة بالشكل المطلوب
    return f'''
📍 {country} Address Generator
    
𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲: {full_name}
𝗦𝘁𝗿𝗲𝗲𝘁 𝗔𝗱𝗱𝗿𝗲𝘀𝘀: {street_address}
𝗖𝗶𝘁𝘆/𝗧𝗼𝘄𝗻/𝗩𝗶𝗹𝗹𝗮𝗴𝗲: {city}
𝗦𝘁𝗮𝘁𝗲/𝗣𝗿𝗼𝘃𝗶𝗻𝗰𝗲/𝗥𝗲𝗴𝗶𝗼𝗻: {state}
𝗣𝗼𝘀𝘁𝗮𝗹 𝗖𝗼𝗱𝗲: {postal_code}
𝗣𝗵𝗼𝗻𝗲 𝗡𝘂𝗺𝗯𝗲𝗿: {formatted_phone_number}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country}
    '''

# الدالة التي يتم استدعاؤها عند استخدام الأمر /fake
@bot.message_handler(commands=["fake"])
def fake_data_handler(message):
    # استخراج رمز الدولة بعد الأمر
    country_code = message.text.replace("/fake ", "").strip().lower()
    
    if not country_code:
        bot.reply_to(message, "Please provide a country code, e.g., /fake us")
        return

    # توليد البيانات الوهمية
    fake_data = generate_fake_data(country_code)

    # إرسال البيانات للمستخدم
    bot.reply_to(message, fake_data)


        
        

#نظام انشاء الاكواد

import time

# السماح للمالك والأدمن بإنشاء أكواد VIP
@bot.message_handler(commands=["code"])
def create_code(message):
    user_id = message.from_user.id

    # التحقق مما إذا كان المستخدم هو المالك أو الأدمن
    if user_id == owner_id or user_id in admin_list:
        try:
            args = message.text.split()
            hours = int(args[1])
            expiration_time = time.time() + hours * 3600
            code = f"VIP-{int(expiration_time)}"

            with open("codes.txt", "a") as file:
                file.write(f"{code}:{expiration_time}\n")

            bot.reply_to(message, f'''𝗡𝗲𝘄 𝗖𝗼𝗱𝗲 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 🚀
𝗖𝗼𝗱𝗲 : <code>{code}</code> (valid for {hours} hours)
𝗨𝘀𝗮𝗴𝗲 : /redeem [code]
𝗢𝘄𝗻𝗲𝗿 : @Mohamed_Was_Here''')
        except:
            bot.reply_to(message, "Usage: /code [hours]")
    else:
        bot.reply_to(message, "𝗬𝗼𝘂 𝗗𝗼𝗻'𝘁 𝗛𝗮𝘃𝗲 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻 𝘁𝗼 𝗖𝗿𝗲𝗮𝘁𝗲 𝗩𝗜𝗣 𝗖𝗼𝗱𝗲𝘀 ❌")

#نظام استرداد الاكواد

owner_name = "Mohamed Hamdy"  # استبدل هذا الاسم باسم مالك البوت
owner_id = 6898845629  # استبدل بهذا المعرف بمعرف المالك الخا

@bot.message_handler(commands=["redeem"])
def redeem_code(message):
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else "Unknown"
    code = message.text.split()[1] if len(message.text.split()) > 1 else None

    if code:
        with open("codes.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            saved_code, expiration_time = line.strip().split(":")
            if saved_code == code:
                if time.time() < float(expiration_time):
                    # كود صالح
                    with open("premium.txt", "a") as premium_file:
                        premium_file.write(f"{user_id}:{expiration_time}\n")  # إضافة المستخدم إلى قائمة VIP
                    bot.reply_to(message, f'''✅ 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱 𝗮 𝗩𝗜𝗣 𝗰𝗼𝗱𝗲 ✅
𝗢𝘄𝗻𝗲𝗿 : {owner_name} (ID: {owner_id})
𝗬𝗼𝘂𝗿 𝗜𝗗 : {user_id}
𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : @{username}
𝗖𝗼𝗱𝗲 : <code>{code}</code>
𝗩𝗮𝗹𝗶𝗱 𝗳𝗼𝗿 : {(float(expiration_time) - time.time()) / 3600:.2f} hours
''')
                    # حذف الكود بعد الاسترداد
                    lines.remove(line)
                    with open("codes.txt", "w") as file:
                        file.writelines(lines)
                else:
                    bot.reply_to(message, "❌ This code has expired.")
                return
        
        bot.reply_to(message, "❌ Invalid code.")
    else:
        bot.reply_to(message, "Usage: /redeem [code]")


owner_id = 6898845629  # استبدل بمعرف المالك الخاص بك
free_access_until = None  # لتخزين فترة الوصول المجاني إذا كانت موجودة
PREMIUM_FILE = "premium_users.txt"  # ملف لتخزين معلومات VIP

# وظيفة للتحقق مما إذا كان المستخدم مسجلاً كـ VIP
def is_user_registered(user_id):
    if os.path.exists(PREMIUM_FILE):
        with open(PREMIUM_FILE, "r") as file:
            for line in file:
                if str(user_id) in line.strip():
                    return True
    return False

# وظيفة لحذف ملف الوصول المجاني بعد انتهاء الفترة
def delete_free_access_file():
    if os.path.exists("free.txt"):
        os.remove("free.txt")

@bot.message_handler(commands=["plan"])
def plan_details(message):
    user_id = message.from_user.id
    
    # تحقق مما إذا كان المستخدم هو المالك
    if user_id == owner_id:
        # رسالة تحتوي على معلومات المالك
        caption = f'''𝗬𝗼𝘂 𝗔𝗿𝗲 𝗧𝗵𝗲 𝗢𝘄𝗻𝗲𝗿 🤦🏻‍♂
𝗬𝗼𝘂𝗿 𝗣𝗹𝗮𝗻 𝗜𝘀 ∞'''
        # إرسال الفيديو مع الرسالة
        video_file_id = "https://t.me/nxbdhsvsbxbc/8"  # استبدل بـ file_id أو URL الفيديو الصحيح
        bot.send_video(message.chat.id, video_file_id, caption=caption)
        return

    # قراءة الملف والتأكد مما إذا كان المستخدم VIP
    with open("premium.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        saved_user_id, expiration_time = line.strip().split(":")
        if str(user_id) == saved_user_id:
            remaining_time = float(expiration_time) - time.time()
            if remaining_time > 0:
                hours_left = remaining_time / 3600

                # رسالة تحتوي على معلومات VIP مع فيديو
                caption = (f"𝗩𝗜𝗣 𝗦𝘁𝗮𝘁𝘂𝘀:\n"
                           f"- 𝗧𝗶𝗺𝗲 𝗿𝗲𝗺𝗮𝗶𝗻𝗶𝗻𝗴: {hours_left:.2f} hours\n"
                           f"- 𝗜𝗗: {user_id}\n"
                           f"- 𝗡𝗮𝗺𝗲: {message.from_user.first_name}\n")

                # إرسال الفيديو مع الرسالة
                video_file_id = "https://t.me/nxbdhsvsbxbc/5"  # استبدل بـ file_id أو URL الفيديو الصحيح
                bot.send_video(message.chat.id, video_file_id, caption=caption)
            else:
                bot.reply_to(message, "Your VIP status has expired.")
            return

    # إذا لم يكن المستخدم VIP
    bot.reply_to(message, "❌ You are not a VIP user. Please redeem a VIP code to access this feature.")


@bot.message_handler(commands=["access"])
def add_group_access(message):
    user_id = message.from_user.id
    
    # التحقق مما إذا كان المستخدم هو المالك
    if user_id != owner_id:
        bot.reply_to(message, "❌ You do not have permission to use this command.")
        return

    # الحصول على معرف المجموعة من الرسالة
    group_id = message.text.split()[1] if len(message.text.split()) > 1 else None

    if group_id:
        with open("allowed_groups.txt", "a") as file:
            file.write(f"{group_id}\n")
        bot.reply_to(message, f"✅ Group ID {group_id} has been added to the allowed groups.")
    else:
        bot.reply_to(message, "❌ Please provide a valid group ID.")


    
# دالة للتحقق مما إذا كان المستخدم VIP
def is_vip_user(user_id):
    with open("premium.txt", "r") as file:
        for line in file:
            saved_user_id, expiration_time = line.strip().split(":")
            if str(user_id) == saved_user_id and time.time() < float(expiration_time):
                return True
    return False
             
                               

@bot.message_handler(content_types=["document"])
def main(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    name = f"{first_name} {last_name}"
    risk = 0
    last = 0
    inf2 = 0
    bad = 0
    nok = 0
    ok = 0
    checked_cards = 0
    ko = (bot.reply_to(message, f'''－ 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 Bot 𝖦𝖺𝗍𝖾 Braintree 💎.
－ 𝖡𝗈𝗍 𝖡𝗒 => @Mohamed_Was_Here 🐳🏴‍☠️''').message_id)
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open("combo.txt", "wb") as w:
        w.write(ee)
    print(message.chat.id)
    sto.update({"stop": False})
    
    if message.chat.id == id:
        with open("combo.txt") as file:
            lino = file.readlines()
            lino = [line.rstrip() for line in lino]
            total = len(lino)
            start_time = time.time()  # Start time measurement
            
            for cc in lino:
                if sto["stop"]:
                    bot.reply_to(message, '🔒 Stopped checking.')
                    break

                checked_cards += 1  # زيادة عدد البطاقات المفحوصة

                bin = cc[:6]
                url = f"https://lookup.binlist.net/{bin}"
                try:
                    req = requests.get(url).json()
                except:
                    pass
                
                try:
                    inf = req['scheme']
                except:
                    inf = "------------"
                try:
                    type = req['type']
                except:
                    type = "-----------"
                try:
                    brand = req['brand']
                except:
                    brand = '-----'
                try:
                    info = inf + '-' + type + '-' + brand
                except:
                    info = "-------"
                try:
                    ii = info.upper()
                except:
                    ii = "----------"
                try:
                    bank = req['bank']['name'].upper()
                except:
                    bank = "--------"
                try:
                    do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
                except:
                    do = "-----------"
                
                mes = types.InlineKeyboardMarkup(row_width=1)
                lucifer1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
                res = types.InlineKeyboardButton(f"• {last} •", callback_data='u1')
                lucifer3 = types.InlineKeyboardButton(f"• Charged 💎 : [ {ok} ] •", callback_data='u2')
                inf = types.InlineKeyboardButton(f"• Low Balance 🟢 : [ {inf2} ] •", callback_data='u2')
                lucifer4 = types.InlineKeyboardButton(f"• Declined ❌️ : [ {bad} ] •", callback_data='u1')
                risk2 = types.InlineKeyboardButton(f"• Risk 😔 : [ {risk} ] •", callback_data='u1')

                # Add buttons for stop, progress, and time taken
                stop_button = types.InlineKeyboardButton("🛑 Stop", callback_data='stop')
                progress_button = types.InlineKeyboardButton(f"🔄 Progress: {checked_cards}/{total}", callback_data='progress')
                time_taken_button = types.InlineKeyboardButton(f"⏱️ Time: {time.time() - start_time:.2f}s", callback_data='time_taken')

                mes.add(lucifer1, res, lucifer3, inf, lucifer4, risk2, stop_button, progress_button, time_taken_button)

                bot.edit_message_text(chat_id=message.chat.id, message_id=ko,
                                      text=f'''• Gateway ⇾ Braintree Charge 11$
- Send /stop To Stop Checking .''',
                                      parse_mode='markdown', reply_markup=mes)
                
                try:
                    last = str(Tele(cc))
                except Exception as e:
                    print(e)
                    bot.reply_to(message, f"-> {cc} »»  OTP ")
                
                if "risk" in last:
                    risk += 1
                    print(Fore.YELLOW + cc + "->" + Fore.CYAN + last)      
                if "Insufficient Funds" in last:
                    inf2 += 1
                    respo = f'''
𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ 

𝗖𝗮𝗿𝗱 ⇾ <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ⇾ Braintree Charge 11$
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⇾ Insufficient Funds

𝗕𝗜𝗡⇾{ii}
𝐈𝐬𝐬𝐮𝐞𝐫  ⇾ {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ {do}
'''
                    print(Fore.YELLOW + cc + "->" + Fore.GREEN + last)
                    bot.reply_to(message, respo)
                elif "Status code avs: Gateway Rejected: avs" in last or "Approved" in last or "Status code 81724: Duplicate card exists in the vault." in last:
                    ok += 1
                    respo = f'''
𝐀𝐩𝐩𝐨𝐯𝐞𝐝 ✅ 

𝗖𝗮𝗿𝗱 ⇾  <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ⇾ Braintree 11$
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⇾ {last}

[↯] 𝗕𝗜𝗡⇾{ii}
𝐈𝐬𝐬𝐮𝐞𝐫  ⇾ {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ {do}
'''

                    print(cc + "->" + last)
                    bot.reply_to(message, respo)
                else:
                    bad += 1
                    print(cc + "->" + last)
                time.sleep(15)
            if sto["stop"] == False:
                bot.reply_to(message, 'ძ᥆ꪀᥱ ᥴɦᥱᥴƙ ᥲᥣᥣ ᥴᥴ 👻🧸')
    else:
        bot.reply_to(message, 'Tᕼᗴ ᗷOT IՏ ᑭᖇᗴᗰIᑌᗰ ᑕᗩᒪᒣ ᗰᗴ ™ @Mohamed_Was_Here')

@bot.message_handler(commands=["stop"])
def stop_checking(message):
    sto["stop"] = True
    bot.reply_to(message, "🔒 The checking process has been stopped.")

# Add a handler for callback data for stop button
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def callback_stop(call):
    sto["stop"] = True
    bot.answer_callback_query(call.id, "The checking process has been stopped.")

# وظيفة زر التقدم
@bot.callback_query_handler(func=lambda call: call.data == 'progress')
def callback_progress(call):
    bot.answer_callback_query(call.id, f"Progress: {checked_cards}/{total}")

# معرف المالك
owner_id = 6898845629  # استبدل بهذا المعرف بمعرف المالك الخاص بك
PREMIUM_FILE = "premium.txt"  # ملف المستخدمين VIP
free_access_until = None  # متغير للتحكم في الوصول المجاني

# قاموس لتخزين آخر وقت لاستخدام /chk لكل مستخدم
last_chk_use = {}

# دالة للتأكد من إمكانية استخدام الأمر
def can_use_chk(user_id):
    current_time = time.time()
    if user_id in last_chk_use:
        last_used = last_chk_use[user_id]
        if current_time - last_used < 20:  # تحقق مما إذا مر 20 ثانية
            return False, 20 - (current_time - last_used)
    # إذا كانت أكثر من 20 ثانية، يمكنه استخدام الأمر
    last_chk_use[user_id] = current_time
    return True, 0

# دالة للتحقق مما إذا كان المستخدم مسجلاً
def is_user_registered(user_id):
    # قم بكتابة منطق التحقق من تسجيل المستخدم هنا
    return True

# دالة لحفظ وقت الوصول المجاني
def save_free_access_time():
    # منطق حفظ الوقت للوصول المجاني
    pass

# دالة لحذف ملف الوصول المجاني بعد انتهاء الفترة
def delete_free_access_file():
    # منطق حذف الملف
    pass

# متغيرات
owner_id = 6898845629  # معرف المالك
PREMIUM_FILE = 'premium_users.txt'  # ملف المستخدمين VIP
last_chk_use = {}  # لتتبع استخدام الأمر من قبل المستخدمين العاديين

# دالة للتحقق مما إذا كان المستخدم مسجلاً
def is_user_registered(user_id):
    # قم بكتابة منطق التحقق من تسجيل المستخدم هنا
    return True

# دالة لحفظ وقت الوصول المجاني
def save_free_access_time():
    pass

# دالة لحذف ملف الوصول المجاني بعد انتهاء الفترة
def delete_free_access_file():
    pass

# دالة للتحقق مما إذا كان المستخدم يمكنه استخدام الأمر /chk (تطبق فقط على المستخدمين Free)
def can_use_chk(user_id):
    current_time = time.time()
    if user_id in last_chk_use:
        last_used = last_chk_use[user_id]
        if current_time - last_used < 20:  # تحقق مما إذا مر 20 ثانية
            return False, 20 - (current_time - last_used)
    # إذا كانت أكثر من 20 ثانية، يمكنه استخدام الأمر
    last_chk_use[user_id] = current_time
    return True, 0


from gatet import GateTele   # استدعاء دالة الفحص من gatet.py

import requests
import random
from datetime import datetime
import requests
import random
from datetime import datetime

@bot.message_handler(commands=["vbv"])
def start(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username



    # التحقق مما إذا كان المستخدم VIP
    if not is_vip_user(user_id):
        bot.reply_to(message, "❌ You are not authorized to use this command. Please redeem a VIP code first.")
        return

    global free_access_until
    chat_id = message.chat.id
    username = message.from_user.first_name if message.from_user.first_name else "Unknown"

    # التحقق من رتبة المستخدم
    found = 'unpr'
    if user_id == owner_id:
        rank = "OWNER"
    else:
        with open(PREMIUM_FILE, "r") as file:
            for line in file:
                if str(user_id) in line.strip():
                    found = 'pro'
                    rank = "VIP"

    if not 'pro' in found and user_id != owner_id:
        rank = "Free"

        return


    if free_access_until is not None and datetime.now() > free_access_until:
        bot.reply_to(message, "❌ The free access period has ended.")
        delete_free_access_file()
        free_access_until = None
        save_free_access_time()
        return

    if not is_vip_user(user_id):
        bot.reply_to(message, "You need to register first using /register before using this command.")
        return

    if message.reply_to_message:
        cc = message.reply_to_message.text.strip()
    else:
        cc = message.text.replace('/vbv ', '').strip()

    card_details = cc.split('|')

    if len(card_details) != 4 or len(card_details[0]) < 16:
        bot.reply_to(message, "🚫 Oops! It looks like the card details were entered incorrectly.\nUse this format: CC|MM|YYYY|CVV")
        return

    start_time = time.time()  # بداية الفحص
    try:
        # استعلام BIN
        data = requests.get(f'https://lookup.binlist.net/{cc[:6]}').json()
    except:
        data = {}

    # توليد معلومات عشوائية إذا لم تتوفر البيانات الأصلية
    banks_list = ['Random Bank', 'Global Bank', 'Future Finance', 'Star Bank']
    countries_list = ['USA', 'UK', 'France', 'Germany']
    emojis_list = ['🇺🇸', '🇬🇧', '🇫🇷', '🇩🇪']
    schemes_list = ['VISA', 'MasterCard', 'AMEX']
    types_list = ['Credit', 'Debit', 'Prepaid']

    bank = data.get('bank', {}).get('name') or random.choice(banks_list)
    country_name = data.get('country', {}).get('name') or random.choice(countries_list)
    country_emoji = data.get('country', {}).get('emoji') or random.choice(emojis_list)
    scheme = data.get('scheme') or random.choice(schemes_list)
    card_type = data.get('type') or random.choice(types_list)
    
    ko = (bot.reply_to(message, "𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩, 𝙄'𝙢 𝙘𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙮𝙤𝙪𝙧 𝙘𝙖𝙧𝙙...").message_id)

    # استدعاء الدالة الخاصة بفحص البطاقة من ملف gatet.py
    time.sleep(2)
    try:
        last = str(GateTele(cc))
    except Exception as e:
        print(e)
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='Sorry, the server took too long to respond. Please try again later.')
        return

    # قائمة الرسائل التي سيتم إرسالها بناءً على النتيجة
    if "authenticate_attempt_successful" in last:
        msg = f'''
𝗣𝗮𝘀𝘀𝗲𝗱 ✅

𝗖𝗮𝗿𝗱 ⇾ 
<code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ 3DS Lookup
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ 3DS Authenticate Attempt Successful

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)

    elif "authenticate_successful" in last:
        msg = f'''
𝗣𝗮𝘀𝘀𝗲𝗱 ✅

𝗖𝗮𝗿𝗱 ⇾ <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ 3DS Lookup
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ 3DS Authenticate Successful

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)

    elif "challenge_required" in last:
        msg2 = f'''
𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌

𝗖𝗮𝗿𝗱 ⇾ <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ 3DS Lookup
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ 3DS Challenge Required

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg2)

    elif  "authenticate_rejected" in last:
        msg4 = f'''
𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌

𝗖𝗮𝗿𝗱 ⇾ <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ 3DS Lookup
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ 3DS Authenticate Rejected

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg4)
        
    elif  "authenticate_frictionless_failed" in last:
        msg5 = f'''
𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌

𝗖𝗮𝗿𝗱 ⇾ <code>{cc}</code>
𝗚𝗮𝗿𝗲𝘄𝗮𝘆 ⇾ 3DS Lookup
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ 3DS Authenticate Frictionless Failed

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg5)

        print(f"{cc} ➜ {last}")

import requests
import random
from datetime import datetime
from st import StTele  # استيراد الدالة من ملف st.py

@bot.message_handler(commands=["st"])
def start(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username



    # التحقق مما إذا كان المستخدم VIP
    if not is_vip_user(user_id):
        bot.reply_to(message, "❌ You are not authorized to use this command. Please redeem a VIP code first.")
        return

    global free_access_until
    chat_id = message.chat.id
    username = message.from_user.first_name if message.from_user.first_name else "Unknown"

    # التحقق من رتبة المستخدم
    found = 'unpr'
    if user_id == owner_id:
        rank = "OWNER"
    else:
        with open(PREMIUM_FILE, "r") as file:
            for line in file:
                if str(user_id) in line.strip():
                    found = 'pro'
                    rank = "VIP"

    if not 'pro' in found and user_id != owner_id:
        rank = "Free"

        return


    if free_access_until is not None and datetime.now() > free_access_until:
        bot.reply_to(message, "❌ The free access period has ended.")
        delete_free_access_file()
        free_access_until = None
        save_free_access_time()
        return

    if not is_vip_user(user_id):
        bot.reply_to(message, "You need to register first using /register before using this command.")
        return

    if message.reply_to_message:
        cc = message.reply_to_message.text.strip()
    else:
        cc = message.text.replace('/st ', '').strip()

    card_details = cc.split('|')

    if len(card_details) != 4 or len(card_details[0]) < 16:
        bot.reply_to(message, "🚫 Oops! It looks like the card details were entered incorrectly.\nUse this format: CC|MM|YYYY|CVV")
        return

    start_time = time.time()  # بداية الفحص
    try:
        # استعلام BIN
        data = requests.get(f'https://lookup.binlist.net/{cc[:6]}').json()
    except:
        data = {}

    bank = data.get('bank', {}).get('name', 'UNKNOWN').upper()
    country_name = data.get('country', {}).get('name', 'UNKNOWN').upper()
    country_emoji = data.get('country', {}).get('emoji', ' ').upper()
    scheme = data.get('scheme', 'UNKNOWN').upper()
    card_type = data.get('type', 'UNKNOWN').upper()

    ko = (bot.reply_to(message, "𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩, 𝙄'𝙢 𝙘𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙮𝙤𝙪𝙧 𝙘𝙖𝙧𝙙...").message_id)

    # استدعاء الدالة الخاصة بفحص البطاقة من ملف st.py
    time.sleep(2)
    try:
        last = str(StTele(cc))  # استدعاء الدالة الخاصة بفحص البطاقة
    except Exception as e:
        print(e)
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='Sorry, the server took too long to respond. Please try again later.')
        return

    # قائمة الرسائل التي سيتم إرسالها بناءً على النتيجة
    if "success" in last:
        msg = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗮𝗿𝗱 ⇾ <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Stripe Auth
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Success

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝗶𝗲𝘀 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)

    elif "Your card has insufficient funds." in last:
        msg2 = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗮𝗿𝗱 ⇾ <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Stripe Auth
𝗥𝗲𝗳𝗲𝗿𝗲𝗻𝗰𝗲 ⇾ Insufficient Funds

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝗨𝗻𝘁𝗿𝗶𝗲𝘀 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg2)
    else:
        msg2 = f'''
𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌

𝗖𝗮𝗿𝗱 ⇾ <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Stripe Auth
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ {last}

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg2)
  
 
        print(f"{cc} ➜ {last}")


from charge import ChargeTele  # استيراد دالة الفحص من charge.py

@bot.message_handler(commands=["ch"])
def check_card_charge(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    # التحقق مما إذا كان المستخدم VIP
    if not is_vip_user(user_id):
        bot.reply_to(message, "❌ You are not authorized to use this command. Please redeem a VIP code first.")
        return

    # التحقق من وجود تفاصيل البطاقة بعد الأمر
    cc_details = message.text.replace('/ch ', '').strip()
    card_details = cc_details.split('|')

    # التحقق من صحة تنسيق البطاقة وأن أول جزء يحتوي على 16 رقمًا
    if len(card_details) != 4 or len(card_details[0]) < 16:
        bot.reply_to(message, "🚫 Oops! It looks like the card details were entered incorrectly.\nUse this format: CC|MM|YYYY|CVV")
        return

    # بدء عملية الفحص وإرسال رسالة الانتظار
    start_time = time.time()  # بداية الفحص
    ko = (bot.reply_to(message, "𝙥𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 , 𝙞'𝙢 𝙘𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙮𝙤𝙪𝙧 𝙘𝙖𝙧𝙙 ...").message_id)

    try:
        # استدعاء الدالة الخاصة بفحص البطاقة
        last = str(ChargeTele(cc_details))
    except Exception as e:
        print(e)
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='Sorry, the server took too long to respond. Please try again later.')
        return

    # استعلام BIN
    try:
        data = requests.get('https://lookup.binlist.net/' + card_details[0][:6]).json()
    except:
        data = {}

    # استخراج معلومات BIN
    bank = data.get('bank', {}).get('name', 'UNKNOWN').upper()
    country_name = data.get('country', {}).get('name', 'UNKNOWN').upper()
    country_emoji = data.get('country', {}).get('emoji', ' ').upper()
    scheme = data.get('scheme', 'UNKNOWN').upper()
    card_type = data.get('type', 'UNKNOWN').upper()

    # الرسائل التي تحتوي على نتيجة الفحص وتفاصيل المستخدم
    if "success" in last or "OK" in last:
        msg = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗮𝗿𝗱 ⇾ <code>{cc_details}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Stripe Auth 2
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ {last}

𝗕𝗶𝗻 ⇾ {card_details[0][:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ @{username}
𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
    if "3D-AUTH" in last:
        msg = f'''𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌

𝗖𝗮𝗿𝗱 ⇾ <code>{cc_details}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Stripe Auth 2
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ 3D-AUTH

𝗕𝗶𝗻 ⇾ {card_details[0][:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ @{username}
𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        
    else:
        msg = f'''
𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌

𝗖𝗮𝗿𝗱 ⇾ <code>{cc_details}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Stripe Auth 2
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ {last}

𝗕𝗶𝗻 ⇾ {card_details[0][:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ @{username}
𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''

    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)



@bot.message_handler(func=lambda message: message.text.startswith('/chk') or message.text.startswith('.chk'))
def start(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    # التحقق مما إذا كان المستخدم VIP
    if not is_vip_user(user_id):
        bot.reply_to(message, "❌ You are not authorized to use this command. Please redeem a VIP code first.")
        return

    global free_access_until
    chat_id = message.chat.id
    username = message.from_user.first_name if message.from_user.first_name else "Unknown"

    # التحقق من رتبة المستخدم
    found = 'unpr'
    if user_id == owner_id:
        rank = "OWNER"
    else:
        with open(PREMIUM_FILE, "r") as file:
            for line in file:
                if str(user_id) in line.strip():
                    found = 'pro'
                    rank = "VIP"

    if not 'pro' in found and user_id != owner_id:
        rank = "Free"

        return


    # التحقق من وجود تفاصيل البطاقة بعد الأمر
    cc = message.text.replace('/chk ', '').replace('.chk ', '').strip()
    card_details = cc.split('|')

    # التحقق من صحة تنسيق البطاقة وأن أول جزء يحتوي على 16 رقمًا
    if len(card_details) != 4 or len(card_details[0]) < 16:
        bot.reply_to(message, "🚫 Oops! It looks like the card details were entered incorrectly.\nUse this format: CC|MM|YYYY|CVV")
        return


    start_time = time.time()  # بداية الفحص
    try:
        data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
    except:
        data = {}

    # استخراج معلومات BIN
    bank = data.get('bank', {}).get('name', 'UNKNOWN').upper()
    country_name = data.get('country', {}).get('name', 'UNKNOWN').upper()
    country_emoji = data.get('country', {}).get('emoji', ' ').upper()
    scheme = data.get('scheme', 'UNKNOWN').upper()
    card_type = data.get('type', 'UNKNOWN').upper()
    
    ko = (bot.reply_to(message, "𝙥𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 , 𝙞'𝙢 𝙘𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙮𝙤𝙪𝙧 𝙘𝙖𝙧𝙙 ...").message_id)

    # الرسائل التي تحتوي على نتيجة الفحص وتفاصيل المستخدم
    msg = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗮𝗿𝗱 ⇾  <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Charge 11$
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Charged ✅

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''

    msgu = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ 

𝗖𝗮𝗿𝗱 ⇾  <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Charge 11$
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Insufficient Funds

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''

    time.sleep(2)
    try:
        last = str(Tele(cc))  # استدعاء الدالة الخاصة بفحص البطاقة
    except Exception as e:
        print(e)
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='Sorry, the server took too long to respond. Please try again later.')
        return

    if "Insufficient Funds" in last:
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgu)
    elif "YOUR ORDER WAS SUCCESSFUL" in last or "Approved" in last or "YOUR ORDER WAS UNSUCCESSFUL" in last:
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
    else:
        msg2 = f'''
𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌

𝗖𝗮𝗿𝗱 ⇾  <code>{cc}</code>
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Charge 11$
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ {last}

𝗕𝗶𝗻 ⇾ {cc[:6]} - {scheme} - {card_type}
𝗕𝗮𝗻𝗸 ⇾ {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ⇾ {country_name} - {country_emoji}

𝗨𝘀𝗲𝗿 𝗡𝗮𝗺𝗲 ⇾ {username}
𝗥𝗮𝗻𝗸 ⇾ {rank}

𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {time.time() - start_time:.2f} seconds
'''
        print(f"{cc} ➜ {last}")
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg2)


@bot.message_handler(commands=["restart"])
def start(message):
	try:
		os.remove('start.start')
		bot.reply_to(message, " 𝙩𝙝𝙚 𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙧𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙✅")
	except:
		bot.reply_to(message, "error")
@bot.message_handler(commands=["vip"])
def start(message):
	chat_id = message.from_user.id
	if chat_id == 6898845629:
		id=message.text.replace("/add ", "")
		with open("premium.txt", "a+") as file:
			file.writelines('\n'+id)
		bot.reply_to(message,"𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙖𝙙𝙙𝙚𝙙 𝙩𝙤 𝙥𝙧𝙚𝙢𝙞𝙪𝙢 𝙪𝙨𝙚𝙧𝙨 💸✅")

import time
import threading

def remove_expired_users():
    while True:
        time.sleep(60)  # تحقق كل ساعة
        current_time = time.time()

        # تحديث ملف VIP
        with open("premium.txt", "r") as file:
            lines = file.readlines()

        with open("premium.txt", "w") as file:
            for line in lines:
                user_id, expiration_time = line.strip().split(":")
                if current_time < float(expiration_time):
                    file.write(line)  # الاحتفاظ بالمستخدم
                else:
                    # يمكن إرسال رسالة للمستخدم بأن الكود قد انتهى
                    bot.send_message(user_id, "Your VIP status has expired.")

ADMIN_ID = 6898845629  # استبدل هذا بمعرف الأدمن الفعلي


@bot.message_handler(commands=["report"])
def report_to_users(message):
    if message.from_user.id == ADMIN_ID:  # تأكد من أن المستخدم هو الأدمن
        try:
            # استخرج الرسالة من الأمر
            report_message = message.text.replace('/report ', '').strip()
            if not report_message:
                bot.reply_to(message, "Usage: /report [message]")
                return
            
            # قراءة معرفات المستخدمين من الملف
            with open("users.txt", "r") as file:
                user_ids = file.readlines()

            # إرسال الرسالة إلى جميع المستخدمين
            for user_id in user_ids:
                user_id = user_id.strip()
                try:
                    bot.send_message(user_id, report_message)
                except Exception as e:
                    print(f"Could not send message to {user_id}: {str(e)}")  # تجاهل المستخدمين الذين لا يمكن إرسال الرسائل إليهم

            bot.reply_to(message, "Report sent to all users.")
        
        except FileNotFoundError:
            bot.reply_to(message, "No users found.")
    else:
        bot.reply_to(message, "You do not have permission to send reports.")								

# أمر /register لتسجيل المستخدم
@bot.message_handler(commands=["register"])
def register_user(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    # تحقق مما إذا كان المستخدم مسجل بالفعل
    try:
        with open("registered_users.txt", "r") as file:
            if str(user_id) in file.read():
                bot.reply_to(message, "You are already registered.")
                return
    except FileNotFoundError:
        pass  # إذا لم يكن الملف موجودًا، سيتم إنشاؤه تلقائيًا عند التسجيل

    # إضافة معرف المستخدم إلى الملف
    with open("registered_users.txt", "a") as file:
        file.write(f"{user_id}\n")
    
    bot.reply_to(message, f"Thank you {first_name}, you have successfully registered!")

# دالة لفحص تسجيل المستخدم
def is_user_registered(user_id):
    try:
        with open("registered_users.txt", "r") as file:
            registered_users = file.read().splitlines()
            return str(user_id) in registered_users
    except FileNotFoundError:
        return False

# أمر /ban لحظر عضو بالرد على رسالته
@bot.message_handler(commands=["ban"])
def ban_user(message):
    if message.reply_to_message:  # التحقق من وجود رد على رسالة
        user_id_to_ban = message.reply_to_message.from_user.id  # الحصول على معرف العضو المراد حظره
        user_name_to_ban = message.reply_to_message.from_user.first_name  # الحصول على اسم العضو
        chat_id = message.chat.id
        
        try:
            bot.kick_chat_member(chat_id, user_id_to_ban)  # حظر العضو من المجموعة
            bot.reply_to(message, f"🚫 The user {user_name_to_ban} has been banned from the group.")
        except Exception as e:
            bot.reply_to(message, f"❌ Failed to ban the user: {str(e)}")
    else:
        bot.reply_to(message, "Please reply to the message of the user you want to ban.")

# أمر /unban لإلغاء حظر عضو بالرد على رسالته
@bot.message_handler(commands=["unban"])
def unban_user(message):
    if message.reply_to_message:  # التحقق من وجود رد على رسالة
        user_id_to_unban = message.reply_to_message.from_user.id  # الحصول على معرف العضو المراد إلغاء حظره
        user_name_to_unban = message.reply_to_message.from_user.first_name  # الحصول على اسم العضو
        chat_id = message.chat.id
        
        try:
            bot.unban_chat_member(chat_id, user_id_to_unban)  # إلغاء حظر العضو من المجموعة
            bot.reply_to(message, f"✅ The user {user_name_to_unban} has been unbanned from the group.")
        except Exception as e:
            bot.reply_to(message, f"❌ Failed to unban the user: {str(e)}")
    else:
        bot.reply_to(message, "Please reply to the message of the user you want to unban.")
											

@bot.message_handler(commands=["gen"])
def generate_cards(message):
    start_time = time.time()  # Start timing the process
    user_name = message.from_user.first_name  # User's first name
    user_id = message.from_user.id  # User's ID

    try:
        # Extract BIN and amount from the message
        args = message.text.split()
        if len(args) != 3:
            raise ValueError("Invalid arguments")

        bin_number = args[1]  # BIN
        amount = int(args[2])  # Amount

        # List to store generated cards
        card_list = []

        # Generate random cards
        for _ in range(amount):
            # Generate a random card number (e.g., 16 digits)
            random_number = ''.join(random.choices('0123456789', k=10))  # 10 random digits
            card_number = f"{bin_number}{random_number}"  # Combine BIN with random digits

            # Generate expiration date (month and year)
            month = random.randint(1, 12)
            year = random.randint(2024, 2031)  # Year range from 2024 to 2031

            # Generate CVV (3 random digits)
            cvv = ''.join(random.choices('0123456789', k=3))

            # Add the card to the list in the required format
            card_list.append(f"{card_number}|{month:02}|{year}|{cvv}")

        # Save cards to a text file
        filename = "[@GokuBlackRobot].txt"
        with open(filename, "w") as file:
            for card in card_list:
                file.write(f"{card}\n")

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time

        # Send the text file and information about the process
        with open(filename, "rb") as file:
            # Create a message with the process information
            process_info = (
                f"• 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗖𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝗱\n"
                f"👤 𝗨𝘀𝗲𝗿 {user_name} (ID: {user_id})\n"
                f"🔢 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝗖𝗖𝘀 ⇾ {amount}\n"
                f"⏱️ 𝗧𝗶𝗺𝗲 𝘁𝗮𝗸𝗲𝗻 ⇾ {elapsed_time:.2f} seconds"
            )
            # Send the file and the process information
            bot.send_document(message.chat.id, file, caption=process_info)

    except ValueError as e:
        bot.reply_to(message, str(e))
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

        								
# قائمة الكلمات الممنوعة
banned_words = ["كسمك", "المتناكة","احبه","معرص","عرص","خول","زانية","احبة","زانيه"]  # أضف كلماتك الممنوعة هنا

@bot.message_handler(func=lambda message: True)
def check_message(message):
    # تحقق من أن الرسالة ليست من البوت نفسه
    if message.from_user.is_bot:
        return

    # تحقق إذا كانت الرسالة تحتوي على أي من الكلمات الممنوعة
    for word in banned_words:
        if word in message.text:
            # حذف الرسالة
            bot.delete_message(message.chat.id, message.message_id)
            # الرد على العضو
            bot.send_message(message.chat.id, f"🚫 {message.from_user.first_name} (@{message.from_user.username}), هذه الكلمة ممنوعة.")
            break  # الخروج من الحلقة بعد حذف الرسالة																														
print("STARTED BOT [@Mohamed_Was_Here]")
bot.infinity_polling()
  