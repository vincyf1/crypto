from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
from stellar_sdk.exceptions import NotFoundError, BadResponseError, BadRequestError

server = Server("https://horizon-testnet.stellar.org")
source_key = Keypair.from_secret('SA4QHCIDFMA3OPMK4Q564HG2OIRKASH4Q6QWHF7XC567PWGNIUG3UVBC')
destination_id = 'GBFIKP4DHX2VWTRHFLNQDOZF5UPTH3PDVCMWPUA2SET4HVQAAC4NZXXX'

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
    .set_timeout(0)
    .build()
)
transaction.sign(source_key)

try:
    response = server.submit_transaction(transaction)
    print(f"Response: {response}")
except (BadRequestError, BadResponseError) as err:
    print(f"Something went wrong!\n{err}")
