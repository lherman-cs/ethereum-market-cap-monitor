from os.path import abspath, dirname

BASE_DIR = dirname(abspath(__file__))

COINBASE_API_URL = 'https://api.coinbase.com/v2/prices/eth-usd/spot?quote=true'

GOOGLE_API_SCOPE = ['https://spreadsheets.google.com/feeds']
GOOGLE_CREDENTIAL_PATH = 'credential.json'

SHEET_TITLE = 'Investment'

ETH_POS = (5, 11)