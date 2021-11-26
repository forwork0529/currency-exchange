import requests
import json
from configBot import keys, APIKEY

class ConversionException(Exception):
    pass

class ValuePreparer:
    @staticmethod
    def convert(quote, base ,amount):
        if quote == base:
            raise ConversionException('Невозможно перевести одинаковые валюты')
        try:
            a = float(amount)
        except ValueError:
            raise ConversionException('Не удалось обработать количество')
        try:
            a = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}!')
        try:
            a = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать  {base}!')



class CountTB: #  класс из задания для запроса на API c учётом количества единиц конвертируемой валюты
    @staticmethod
    def get_price(quote, base, amount):
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}&api_key={{APIKEY}} ')
        middle_base = json.loads(r.content)[keys[base]]
        return float(amount) * float(middle_base)




