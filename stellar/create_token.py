import os
import json
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Signer, Asset
import requests

# Load Source Keys
source_keypair = Keypair.from_secret(os.getenv('Account1_SecretSeed'))
source_public_key = source_keypair.public_key
source_secret_key = source_keypair.secret

server = Server(horizon_url="https://horizon-testnet.stellar.org/")
#
# # -- USDC -- #
# # Create new token using issuing account
# issue_account_keypair = Keypair.from_secret(os.getenv('Account4_SecretSeed'))
# issue_account_public_key = issue_account_keypair.public_key
# issue_account_secret_key = issue_account_keypair.secret
#
# asset = Asset('USDC', issue_account_public_key)
#
# # Trust Issuing Account to Source Account
# base_fee = server.fetch_base_fee()
# source_account = server.load_account(source_public_key)
#
# transaction = (
#     TransactionBuilder(
#         source_account=source_account,
#         network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
#         base_fee=base_fee,
#     )
#     .append_change_trust_op(
#         asset=asset,
#     )
#     .build()
# )
# print('Signing Transaction')
# transaction.sign(source_keypair.secret)
# response = server.submit_transaction(transaction)
#
# print(f"This is the response from trusting the Issuer: {json.dumps(response, indent=2)}")
#
# # Transfer funds to Source Account in USDC
# issuer_account = server.load_account(issue_account_public_key)
#
# transaction = (
#     TransactionBuilder(
#         source_account=issuer_account,
#         network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
#         base_fee=base_fee,
#     )
#     .append_payment_op(
#         destination=source_public_key,
#         asset=asset,
#         amount='10000',
#     )
#     .build()
# )
# print('Signing Transaction for Transfer of USDC')
# transaction.sign(issue_account_secret_key)
# response = server.submit_transaction(transaction)
#
# print(f"This is the response from transferring USDC: {json.dumps(response, indent=2)}")

# -- GBP -- #
# Create new token using issuing account
issue_account_keypair = Keypair.from_secret(os.getenv('Account5_SecretSeed'))
issue_account_public_key = issue_account_keypair.public_key
issue_account_secret_key = issue_account_keypair.secret

asset = Asset('GBP', issue_account_public_key)

# Trust Issuing Account to Source Account
base_fee = server.fetch_base_fee()
source_account = server.load_account(source_public_key)

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_change_trust_op(
        asset=asset,
    )
    .build()
)
print('Signing Transaction')
transaction.sign(source_keypair.secret)
response = server.submit_transaction(transaction)

print(f"This is the response from trusting the Issuer: {json.dumps(response, indent=2)}")

# Transfer funds to Source Account in GBP
issuer_account = server.load_account(issue_account_public_key)

transaction = (
    TransactionBuilder(
        source_account=issuer_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_payment_op(
        destination=source_public_key,
        asset=asset,
        amount='1000',
    )
    .build()
)
print('Signing Transaction for Transfer of USDC')
transaction.sign(issue_account_secret_key)
response = server.submit_transaction(transaction)

print(f"This is the response from transferring GBP: {json.dumps(response, indent=2)}")