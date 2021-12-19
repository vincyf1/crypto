"""
Account# 1
=======================
Public Key:  {'GCQPIQF5T3VL5U33BFQFZRLLWG52I7TPC5CAUIHEXUB7ELXZYKJ25FHQ'}
Secret Seed:  {'SDGKC646AW4TLBYCN34UZ5CGQJ75ZDNKITOSKUJ64CDG5HFH7XCNYQEF'}

Account# 2
=======================
Public Key:  {'GD7ZOVHTZAQQSBFWSAMVPX5UPN5TP2V3RN76XIBQVAEAOG5UGQXRRWIW'}
Secret Seed:  {'SDUN2UUOMQZEHGICFGVYZ5D4RLCC3CBWAMZHWJNHOSVWVLOIWERIQDYJ'}
"""
import requests

from stellar_sdk import Keypair

keypair = Keypair.random()

print('Public Key: ', {keypair.public_key})
print('Secret Seed: ', {keypair.secret})

url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': keypair.public_key})
print(response)

