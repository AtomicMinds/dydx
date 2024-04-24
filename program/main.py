from constants import ABORT_ALL_POSITION, FIND_COINTEGRATED
from func_connections import connect_dydx
from func_private import place_market_order, abort_all_positions
from func_public import construct_market_prices

if __name__ == "__main__":
    print('Artur you cool', )

    # Connect to client
    try:
        print("Connecting to Client...")
        client = connect_dydx()
    except Exception as e:
        print("Error connecting to client: ", e)
        exit(1)

    # Abort all open position
    if ABORT_ALL_POSITION:
        try:
            print("Closing all position...")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Error closing all position: ", e)
            exit(1)

    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:
        # Construct Market Prices
        try:
            print("Fetching market prices, please allow 3 mins...")
            df_market_price = construct_market_prices(client)
        except Exception as e:
            print("Error constructing market prices: ", e)
            exit(1)
























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
#
# # pprint(placed_order.data)
#
#
#
