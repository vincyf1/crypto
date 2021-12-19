import os

from stellar_sdk import Server

server = Server('https://horizon-testnet.stellar.org')
public_key = []

for i, j in os.environ.items():
    if 'PublicKey' in i:
        public_key.append(j)

for key in public_key:
    account = server.accounts().account_id(key).call()

    for balance in account['balances']:
        print(f"Account ID: {key}, Type: {balance['asset_type']}, Balance: {balance['balance']} XLM")
