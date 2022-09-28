# 1. Loop through pairs of coins and get the price of each pair
# 2. Build adjacency matrix of prices
# 3. Find arbitrage opportunities and print them out

from stellar_sdk import LiquidityPoolAsset, Asset
import requests
# my_coins = ['XLM', 'BTC', 'AQUA', 'USDC', 'MOBI', 'XRP', 'ETH', 'LTC', 'BCH', 'EOS', 'BNB', 'TRX', 'ADA', 'XMR', 'DASH',
#             'XEM' 'ETC', 'ZEC', 'BTG', 'QTUM', 'OMG', 'ICX', 'LSK', 'ZIL', 'BNB', 'VEN', 'DOGE', 'DCR', 'BTS', 'BCD',
#             'STEEM', 'WAVES', 'STRAT', 'NEO', 'XVG', 'SC', 'BCN', 'DGB', 'DGD', 'DOGE', 'DASH', 'SLT']

my_coins = ['XLM', 'USDC', 'BTC', 'ZHR', 'BUSD1', 'AQUA', 'MOBI', 'XRP', 'ETH', 'LTC', 'BCH', 'EOS', 'BNB', 'TRX', 'ADA']

# Create issuer accounts and allow trust

issuer = {
    'XLM': 'None',
    'USDC': 'GCZFA6BAM4CQNRKPANYAIA3DEQ6LVR33SMV6VWTO3VS6Z77MIGNXOPNK',
    'ZHR': 'GCFK3TE3JUZK2ENQ26ZJ36H7JRX2IRS5JVSPQEAEZMLEHGD6QQISLWCU',
    'BUSD1': 'GCIEGKAZ4ZUM4PEBTDXUMG6N4ZXOTCCK3UMSJCJ33QE5SVMCTTBKCVNY',
    'BTC': 'GCYJWZ4WOO3Z56TGAORNJLDIBSL6XXLFACGWDONZLXZJCM7SZI4INV34',
    'AQUA': 'GBNZILSTVQZ4R7IKQDGHYGY2QXL5QOFJYQMXPKWRRM5PAV7Y4M67AQUA',
    'MOBI': 'GA6HCMBLTZS5VYYBCATRBRZ3BZJMAFUDKYYF6AH6MVCMGWMRDNSWJPIH',
    'XRP': 'GCNSGHUCG5VMGLT5RIYYZSO7VQULQKAJ62QA33DBC5PPBSO57LFWVV6P',
    'ETH': 'GCNSGHUCG5VMGLT5RIYYZSO7VQULQKAJ62QA33DBC5PPBSO57LFWVV6P',
    'LTC': 'GCNSGHUCG5VMGLT5RIYYZSO7VQULQKAJ62QA33DBC5PPBSO57LFWVV6P',
    'BCH': 'GCNSGHUCG5VMGLT5RIYYZSO7VQULQKAJ62QA33DBC5PPBSO57LFWVV6P',
    'EOS': 'GAAPFSGAM5QKEYHJ5WVPEZMTKTKC3C45AMCAUPYZAHLWX6MOXNAABIEX',
    'BNB': 'GCQEKCSJ7IQTEEOT57T5LXKEYPPEBZGODQZHUYOBW6HKNSXUXAMH376F',
    'TRX': 'GCQEKCSJ7IQTEEOT57T5LXKEYPPEBZGODQZHUYOBW6HKNSXUXAMH376F',
    'ADA': 'GCQEKCSJ7IQTEEOT57T5LXKEYPPEBZGODQZHUYOBW6HKNSXUXAMH376F',
}


def get_price(coin: Asset, coin_2: Asset):
    try:
        liquidity_pool = LiquidityPoolAsset(asset_a=coin, asset_b=coin_2)
        # print(coin.code, coin_2.code)
        # print(liquidity_pool.liquidity_pool_id)
        if liquidity_pool:
            url = "https://horizon-testnet.stellar.org" + "/liquidity_pools/" + liquidity_pool.liquidity_pool_id
            # print(url)
            r = requests.get(url)
            fail = 0
            success = 0
            if r.status_code == 404:
                return None
            else:
                print(f'{coin} - {coin_2}')
                print('SUCCESS')
    except ValueError as ve:
        pass
        # print(f'Swapping to {coin_2} {coin}')
        # liquidity_pool = LiquidityPoolAsset(asset_a=coin_2, asset_b=coin)



def get_coin_asset(coin: str) -> Asset:
    if coin == 'XLM':
        return Asset.native()
    else:
        return Asset(coin, issuer[coin])

def loop_through_coins(coins: list):
    for coin in coins:
        for coin_2 in coins:
            if coin == coin_2:
                continue
            else:
                get_price(get_coin_asset(coin), get_coin_asset(coin_2))


loop_through_coins(my_coins)

# def build_adjacency_matrix():
#     pass
#
# def find_arbitrage_opportunities():
#     pass