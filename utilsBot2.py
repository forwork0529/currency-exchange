import requests
import json
from configBot import keys, APIKEY

class ConversionException(Exception):
    pass

class CryyptoConverter:
    @staticmethod
    def convert(quote, base ,amount):
        if quote == base:
            raise ConversionException('Невозможно перевести одинаковые валюты')
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException('Не удалось обработать количество')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}!')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать  {base}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}&api_key={{APIKEY}} ')
        middle_base = json.loads(r.content)[keys[base]]
        return middle_base

class CountTB: #  класс из задания для учёта количества единиц конвертируемой валюты
    @staticmethod
    def multi(amount, middle_base):
        return  float(amount) * float(middle_base)


