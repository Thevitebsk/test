import requests

class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount):
        return amount / self.exchange_rate

def get_exchange_rate():
    url = 'https://www.nbrb.by/api/exrates/rates/USD?parammode=2'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Не удалось получить данные с API.")

    data = response.json()
    return data['Cur_OfficialRate']

if __name__ == "__main__":
    try:
        exchange_rate = get_exchange_rate()
        converter = CurrencyConverter(exchange_rate)

        amount = float(input("Введите количество вашей валюты: "))
        usd_amount = converter.convert_to_usd(amount)
        print(f"Сумма в долларах США: {usd_amount:.2f}")
    except Exception as e:
        print(f"Ошибка: {e}")
