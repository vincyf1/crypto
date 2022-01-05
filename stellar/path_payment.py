from stellar_sdk import Server, Keypair, Network, TransactionBuilder, Asset
import os

server = Server("https://horizon-testnet.stellar.org")
source = Keypair.from_secret(os.getenv('Account1_SecretSeed'))
# source_account = server.load_account(source.public_key)
#
# asset_to_buy = Asset("USDC", "")
# stellar = Asset('XLM')
# lumen = Asset("XLM", issuer=None)
#
# payments = Server.strict_receive_paths(
#     server,
#     source=[stellar],
#     destination_asset=asset_to_buy,
#     destination_amount='1'
# ).call()
# print(payments)

# from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
#
# server = Server(horizon_url="https://horizon-testnet.stellar.org")
# source_keypair = Keypair.from_secret(
#     ""
# )

source_account = server.load_account(account_id=source.public_key)

native_asset = Asset('XLM')
asset_to_buy = Asset('USDC', '')

path_payments = Server.strict_receive_paths(
    server, source=[native_asset], destination_asset=asset_to_buy,
    destination_amount='100',
).call()

print(path_payments)
#
# path = [
#     Asset("USD", ""),
#     Asset("EUR", ""),
# ]
# transaction = (
#     TransactionBuilder(
#         source_account=source_account,
#         network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
#         base_fee=100,
#     )
#     .append_path_payment_strict_receive_op(
#         destination="",
#         send_asset=Asset.native(),
#         send_max="1000",
#         dest_asset=Asset(
#             "GBP", ""
#         ),
#         dest_amount="5.50",
#         path=path,
#     )
#     .set_timeout(30)
#     .build()
# )
# transaction.sign(source)
# response = server.submit_transaction(transaction)
