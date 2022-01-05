import requests
import logging
from stellar_sdk import Keypair

try:
    keypair = Keypair.random()
except Exception as e:
    logging.error('Error creating keypair!')
    raise Exception(e)


print('Public Key: ', {keypair.public_key})
print('Secret Seed: ', {keypair.secret})

# Fund the account with XLM
url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': keypair.public_key})
print(response)
