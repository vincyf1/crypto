import os

from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer, Asset
import requests
import json

# 1. Load Keys
# In this case this account will be the distributor.
server = Server("https://horizon-testnet.stellar.org")
source_account = Keypair.from_secret(os.getenv('Account1_SecretSeed'))
source_public_key = source_account.public_key
source_secret = source_account.secret

# 2. Create an object to represent the new asset
asset = Asset('USDC', os.getenv('Account4_PublicKey'))

# 3. Sell of Asset
print("Building Transaction...")

base_fee = server.fetch_base_fee()
stellar_account = server.load_account(source_public_key)

transaction = (
    TransactionBuilder(
        source_account=stellar_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_manage_sell_offer_op(
        selling=asset,
        buying=Asset.native(),
        amount="1",  # Feel free to change this.
        price="10",
        offer_id=0
    )
    .build()
)

print('Signing Transaction...')
transaction.sign(source_secret)
response = server.submit_transaction(transaction)

print(f"This is the response from selling the token: {json.dumps(response, indent=2)}")
