from stellar_sdk import LiquidityPoolAsset, Asset
import requests

# Public Network: https://horizon.stellar.org/
# Test Network: https://horizon-testnet.stellar.org/


def get_lp(s: Asset, b: Asset):
    try:
        liquidity_pool = LiquidityPoolAsset(asset_a=b, asset_b=s)
        print(liquidity_pool.liquidity_pool_id)
    except ValueError as ve:
        print(ve)
        liquidity_pool = LiquidityPoolAsset(asset_a=s, asset_b=b)
    url = "https://horizon-testnet.stellar.org" + "/liquidity_pools/" + liquidity_pool.liquidity_pool_id
    print(url)
    r = requests.get(url)
    if r.status_code == 404:
        return None
    print(r.url)
    print(liquidity_pool.asset_a)
    print(liquidity_pool.asset_b)
    return liquidity_pool


native = Asset.native()
usdc_asset = Asset(code="USDC", issuer="")
get_lp(usdc_asset, native)
