import os

from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
from stellar_sdk.exceptions import NotFoundError, BadResponseError, BadRequestError

server = Server("https://horizon-testnet.stellar.org")

source_key = Keypair.from_secret(os.getenv('Account1_SecretSeed'))
destination_id = os.getenv('Account2_PublicKey')

try:
    server.load_account(destination_id)
except NotFoundError:
    raise Exception("The destination account does not exist!")

source_account = server.load_account(source_key.public_key)
base_fee = server.fetch_base_fee()

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .append_payment_op(destination=destination_id, asset=Asset.native(), amount="100")
    .add_text_memo("Test Transaction")
    .set_timeout(30)
    .build()
)
transaction.sign(source_key)

try:
    response = server.submit_transaction(transaction)
    print(f"Response: {response}")
except (BadRequestError, BadResponseError) as err:
    print(f"Something went wrong!\n{err}")
