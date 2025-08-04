import telebot
import requests
import time

# 🔐 Токен Telegram бота
bot = telebot.TeleBot("6517590667:AAEH1IjWZAPx8Ku_3q6bgoQGByJ61PBv2QY")

# 🌐 Прокси для доступа к Binance
proxies = {
    "http": "http://51.158.68.133:8811",
    "https": "http://51.158.68.133:8811"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Бот работает и подключается к Binance!")

    # Тестовый запрос к Binance
    try:
        response = requests.get("https://api.binance.com/api/v3/ping", proxies=proxies)
        if response.status_code == 200:
            bot.send_message(message.chat.id, "✅ Успешно подключен к Binance API!")
        else:
            bot.send_message(message.chat.id, f"⚠️ Ответ от Binance: {response.status_code}")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка подключения: {e}")

# 🔁 Постоянная работа
bot.polling()
