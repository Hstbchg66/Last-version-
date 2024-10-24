from telethon.sync import TelegramClient, events
import re, random, asyncio, requests, telebot

token ="7272877488:AAHG8RNVjzBPNXkO3HGDz6jOCutnPGDEDc0" 
bot = telebot.TeleBot(token, parse_mode="HTML")

api_id = '22235163'
api_hash = 'c92aeb0b68ba393fba0c81bf2f2445da'

client = TelegramClient("session", api_id, api_hash)

target_channel_id = "-1002180179897"  # يوزر القناة التي سيتم النشر فيها

video_urls = [
    "https://t.me/TORKE_CC/67390"  # رابط الفيديو المطلوب
]  # روابط فيديو يأخذ منها عشوائيًا

new = []

async def extract_card(search):  # استخراج معلومات البطاقة من الرسالة
    month_match = re.search(r'\b(0?[1-9]|1[0-2])\b', search)
    month = month_match.group(0)
    year_match = re.search(r'\b(20[2-4][0-9]|2[4-9]|3[0-5])\b', search)
    year = year_match.group(0)
    
    num_match = re.search(r'\b\d{15,16}\b', search)
    num = num_match.group(0)
    
    if num.startswith("3"):
        cvv_match = re.search(r'\b(?!20[2-3][0-9])\d{4}\b', search)
    else:
        cvv_match = re.search(r'\b\d{3}\b(?!\s*(20[2-4][0-9]|2[4-9]|3[0-5]))', search)

    cvv = cvv_match.group(0)
    card = f'{num}|{month}|{year}|{cvv}'
    print(card)
    return num, month, year, cvv

ids = [
	-1001833380321,
	-1001793269672,
	-1002271549376,
	-1002154860004,
	-1002212525911,
	-1002204186591,
	-1001410519743,
	-1001662369046,
]  # أيدي القنوات التي يأخذ منها الرسائل

@client.on(events.NewMessage(chats=ids))
async def process_message(event):
    print(event.message.text)
    search = event.message.text
    if search:
        try:
            num, month, year, cvv = await extract_card(search)
        except:
            return
        card = f'{num}|{month}|{year}|{cvv}'
        if num not in new:
            new.append(num)
            video_url = random.choice(video_urls)
            brand, bin, type, level, bank, country_name, country_flag = await info(card)
            bot.send_video(
                target_channel_id,
                video_url,
                caption=f'• 𝐍𝐞𝐰 𝐜𝐚𝐫𝐝 ✅\n—————★☆★★—————\n• 𝗖𝗮𝗿𝐝 <code>{card}</code>\n• 𝗜𝗻𝗳𝗼: {bin} - {brand} - {type} - {level}\n• 𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n• 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n—————★☆★★—————\n𝐁𝐲: <a href="http://t.me/TORKE_CC">𝗧𝗘𝗞𝗔 🏴‍☠️ </a>',
                parse_mode='HTML'
            )

async def info(card):
    response = requests.get('https://bins.antipublic.cc/bins/' + card[:6])
    
    data = ['bin', 'brand', 'type', 'level', 'bank', 'country_name', 'country_flag']
    result = []
        
    for field in data:
        try:
            result.append(response.json()[field])
        except:
            result.append("------")  
    
    return tuple(result)

print("Bot started. Listening for commands...")
client.start()
client.run_until_disconnected()