from autobahn.twisted.websocket import WebSocketServerProtocol
from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.enums import *

client = Client()
bm = BinanceSocketManager(client)
# start any sockets here, i.e a trade socket

def process_message(msg):
  print("message type: {}".format(msg['e']))
  print(msg)
  # do something

conn_key = bm.start_trade_socket('ASRBTC', process_message)
# then start the socket manager
bm.start()
