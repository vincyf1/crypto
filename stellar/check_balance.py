from stellar_sdk import Server

server = Server('https://horizon-testnet.stellar.org')
public_key = ['GBUIND2QZBXZS4YYQCVL4LI4JW73TCGYBSLCSRFJLZTGNR6AV5SFFHHH',
              'GBFIKP4DHX2VWTRHFLNQDOZF5UPTH3PDVCMWPUA2SET4HVQAAC4NZXXX']
for key in public_key:
    account = server.accounts().account_id(key).call()

    for balance in account['balances']:
        print(f"Type: {balance['asset_type']}, Balance: {balance['balance']} XLM")
