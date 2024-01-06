"""
Zadanie 4:

napisz program (cli) który wywoływany z opcjonalnym parametrem daty, pobiera cenę złota na daną datę (lub dzisiejszą) z endpoint REST http://api.nbp.pl/

można użyć dowolnych bibliotek

"""

import argparse
import requests
from datetime import datetime

def is_valid_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_gold_price(date):
    url = f'http://api.nbp.pl/api/cenyzlota/{date}' if date else 'http://api.nbp.pl/api/cenyzlota/today'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['cena']
    else:
        print(f'Error: {response.status_code}')
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', help='date in format YYYY-MM-DD')
    args = parser.parse_args()
    date = args.date

    if date is not None and not is_valid_date_format(date):
        print('Invalid date format')
        date = None

    gold_price = get_gold_price(date)

    if gold_price is not None:
        print(f'Gold price for {date or "today"}: {gold_price} PLN')


if __name__ == '__main__':
    main()