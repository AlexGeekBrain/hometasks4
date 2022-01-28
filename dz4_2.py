from requests import get, utils
from decimal import Decimal

resp = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(code):
    content = resp.split('<Valute ID=')
    for i in content:
        if code.upper() in i:
            print(code.upper(), end=' ')
            return Decimal(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))


print(currency_rates(input('Введите желаемую валюту: ')))
