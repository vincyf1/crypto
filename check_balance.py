from stellar_sdk import Server

server = Server('https://horizon-testnet.stellar.org')
public_key = ['GCQPIQF5T3VL5U33BFQFZRLLWG52I7TPC5CAUIHEXUB7ELXZYKJ25FHQ',
              'GD7ZOVHTZAQQSBFWSAMVPX5UPN5TP2V3RN76XIBQVAEAOG5UGQXRRWIW']
for key in public_key:
    account = server.accounts().account_id(key).call()

    for balance in account['balances']:
        print(f"Type: {balance['asset_type']}, Balance: {balance['balance']} XLM")
