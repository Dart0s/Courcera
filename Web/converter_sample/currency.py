from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}")  # Использовать переданный requests
    soup = BeautifulSoup(response.content, "xml")

    if cur_from != 'RUR':
        value_from = soup.find('CharCode', text=cur_from).find_next_sibling('Value').string
        value_from = Decimal(value_from.replace(',', '.'))
        nominal_from = soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string
        nominal_from = Decimal(nominal_from.replace(',', '.'))
        value_from_one = value_from / nominal_from
    else:
        value_from_one = Decimal('1')

    if cur_to != 'RUR':
        value_to = soup.find('CharCode', text=cur_to).find_next_sibling('Value').string
        value_to = Decimal(value_to.replace(',', '.'))
        nominal_to = soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string
        nominal_to = Decimal(nominal_to.replace(',', '.'))
        value_to_one = value_to / nominal_to
    else:
        value_to_one = Decimal('1')

    result = (value_from_one * amount / value_to_one).quantize(Decimal('1.0000'))
    return result  # не забыть про округление до 4х знаков после запятой


if __name__ == "__main__":
    result = convert(Decimal("1000.1000"), 'RUR', 'JPY', "17/02/2005", requests)
    print(result)