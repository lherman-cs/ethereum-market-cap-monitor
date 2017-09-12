from argparse import ArgumentParser
from os import chdir
from os.path import dirname
from time import sleep

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from requests import request

import settings

def get_eth_price():
    url = settings.COINBASE_API_URL
    r = request("GET", url)

    data = r.json()
    return data['data']['amount']

def update(watch=False):
    creds = ServiceAccountCredentials.from_json_keyfile_name(
                    settings.GOOGLE_CREDENTIAL_PATH, settings.GOOGLE_API_SCOPE)
    client = gspread.authorize(creds)

    sheet = client.open(settings.SHEET_TITLE).sheet1

    if watch:
        while True:
            old_price = sheet.cell(*settings.ETH_POS).value
            new_price = get_eth_price()

            sheet.update_cell(*settings.ETH_POS, new_price)
            print('Changed from {} to {}'.format(old_price, new_price))
            
            sleep(5)
    else:
       old_price = sheet.cell(*settings.ETH_POS).value
       new_price = get_eth_price()

       sheet.update_cell(*settings.ETH_POS, new_price)
       print('Changed from {} to {}'.format(old_price, new_price))        


def main():
    chdir(settings.BASE_DIR)

    parser = ArgumentParser()
    parser.add_argument('-w', '--watch', action='store_true', help='Set watcher. Default: False')

    args = parser.parse_args()

    update(args.watch)

if __name__ == '__main__':
    main()
