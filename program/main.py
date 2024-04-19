if __name__ == "__main__":
    print('Artur you cool', )


















# from dydx3 import Client
# from web3 import Web3
# from pprint import pprint
# from datetime import datetime, timedelta
#
# from dydx3.constants import MARKET_BTC_USD
# from dydx3.constants import ORDER_SIDE_SELL
# from dydx3.constants import ORDER_TYPE_LIMIT
# from dydx3.constants import TIME_IN_FORCE_GTT
#
# # # Testnet
# from dydx3.constants import API_HOST_GOERLI
#
# # # Mainnet
# # from dydx3.constants import API_HOST_MAINNET
#

#
# print('API_HOST_GOERLI --> ', API_HOST_GOERLI)
#
# # Constants
# ETHEREUM_ADDRESS = "0x4c13dfa4Fd6D0dfe63c73c3da0660404a2e42195"
# ETH_PRIVATE_KEY = "0x04b5c4a9a27fc559f047f2e9304fd459ebacead80dd18da05eb4a1fc9d1ce263"
#
# STARK_PRIVATE_KEY = "075b9cbd33bcbde369313088d11ebb94b4ca76a2a0d9d29d8c5c060371a6cf1e"
# DYDX_API_KEY = "0f28e716-57d0-c300-4561-9f6b0a43ad63"
# DYDX_API_SECRET = "mnPSb1mgcM7sVzX0dU6oeTdE-7QfWp7Gw9MsjIM1"
# DYDX_API_PASSPHRASE = "TtQVr_TQyHlVEA_eLYMd"
# HOST = API_HOST_GOERLI
#
# # HTTP Provider
# HTTP_PROVIDER = "https://sepolia.infura.io/v3/911cde61cefc41fea13ef23145de40f5"
#
# #  Create client connection
# client = Client(
#     host=HOST,
#     api_key_credentials={
#         "key": DYDX_API_KEY,
#         "secret": DYDX_API_SECRET,
#         "passphrase": DYDX_API_PASSPHRASE,
#     },
#     stark_private_key=STARK_PRIVATE_KEY,
#     eth_private_key=ETH_PRIVATE_KEY,
#     default_ethereum_address=ETHEREUM_ADDRESS,
#     web3=Web3(Web3.HTTPProvider(HTTP_PROVIDER))
# )
#
# # Check connection
# account = client.private.get_accounts()
# print('account --> ', account.data)
#
# account_id = account.data['accounts'][0]['id']
# quote_balance = account.data["accounts"][0]["quoteBalance"]
# print('account_id --> ', account_id)
# print('quote_balance --> ', quote_balance)
#
# markets = client.public.get_markets()
# print('markets --> ', markets.data['markets']['UMA-USD']['indexPrice'])
#
# # OHLC CandlestickData
# candles = client.public.get_candles(
#     market="BTC-USD",
#     resolution="1HOUR",
#     limit=3
# )
#
# # PPrint Result
# pprint(candles.data["candles"][0])
#
# #  Get Position Id
# account_response = client.private.get_account()
# position_id = account_response.data['account']['positionId']
# print('position_id --> ', position_id)
#
# # Get expiration time
# server_time = client.public.get_time()
# print('server_time --> ', server_time.data)
# expiration_s = datetime.fromisoformat(server_time.data["iso"].replace("Z", "+00:00"))
# expiration = datetime.fromisoformat(server_time.data["iso"].replace("Z", "+00:00")) + timedelta(seconds=70)
# print('expiration_s --> ', expiration_s.timestamp())
# print('expiration   --> ', expiration.timestamp())
#
# # Place an order
# placed_order = client.private.create_order(
#   position_id=position_id,
#   market="BTC-USD",
#   side="BUY",
#   order_type="MARKET",
#   post_only=False,
#   size='0.001',
#   price='1000000',
#   limit_fee='0.015',
#   expiration_epoch_seconds=expiration.timestamp(),
#   time_in_force="FOK",
#   reduce_only=False
# )
#
# # pprint(placed_order.data)
#
#
#
