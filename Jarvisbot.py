import requests
import time
import os

# ✅ Прокси для доступа к Binance
proxies = {
    "http": os.environ.get("Proxy_url"),
    "https": os.environ.get("Proxy_url")
}

# ✅ Тестовая проверка соединения с Binance
def test_binance_connection():
    try:
        response = requests.get("https://api.binance.com/api/v3/ping", proxies=proxies, timeout=10)
        if response.status_code == 200:
            print("✅ Успешно подключен к Binance API")
        else:
            print(f"⚠️ Ответ от Binance: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")

# 🔁 Основной цикл
if __name__ == "__main__":
    print("🤖 Бот запущен и работает без Telegram...")
    while True:
        test_binance_connection()
        time.sleep(60)  # Проверяет каждую минуту
