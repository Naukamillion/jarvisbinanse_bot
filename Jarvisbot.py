import telebot
import requests
from binance.client import Client
import os
import time
import urllib3

# Прокси настройки
proxies = {
    'http': 'http://45.77.201.156:8080',
    'https': 'http://45.77.201.156:8080',
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Получение токенов из переменных окружения
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, {"proxies": proxies})

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ JarvisBinance_Bot запущен!")

@bot.message_handler(commands=['balance'])
def balance(message):
    try:
        balance = client.get_asset_balance(asset='USDT')
        bot.send_message(message.chat.id, f"💰 Баланс USDT: {balance['free']}")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")

bot.polling(non_stop=True)
