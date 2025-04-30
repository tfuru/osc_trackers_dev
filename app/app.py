import argparse
import socket

from typing import List
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

# トラッカーの数
TRACKER_COUNT = 8

PORT = 9000
CLUSTER_APP_HOST = "192.168.86.107"
_client = udp_client.SimpleUDPClient(CLUSTER_APP_HOST, PORT)

# そのままのデータを送信
def passthrough(address: str, *osc_arguments: List[str]):
  printdata(address, osc_arguments)
  try:
    _client.send_message(address, osc_arguments)
    printdata(address, osc_arguments)
  except ValueError: pass

# 送信するデータを変更
def bridge(address: str, *osc_arguments: List[str]):
  # printdata("[BASE] {}".format(address), osc_arguments)
  # uni-studio 1.4.0
  # 基準トラッキングデバイス HMD
  # 全てのトラッカー送信 ON
  try:
    if (address.find("/tracking/trackers/head") > -1):
      _client.send_message(address, osc_arguments)
      # printdata(address, osc_arguments)
    else:
      if (TRACKER_COUNT == 6):
        bridge6(address, *osc_arguments)
      elif (TRACKER_COUNT == 8):
        bridge8A(address, *osc_arguments)
        # bridge8B(address, *osc_arguments)
      elif (TRACKER_COUNT == 11):
        bridge11(address, *osc_arguments)

  except ValueError: pass

# 6点トラッキング
def bridge6(address: str, *osc_arguments: List[str]):
  # 6点
  # 腰 /tracking/trackers/2   -> /tracking/trackers/1
  # 右足 /tracking/trackers/5  -> /tracking/trackers/2
  # 左足 /tracking/trackers/3  -> /tracking/trackers/3
  try:
    if (address.find("/tracking/trackers/2") > -1):
      address = address.replace("/trackers/2", "/trackers/1")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/5") > -1):
      address = address.replace("/trackers/5", "/trackers/2")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/3") > -1):
      address = address.replace("/trackers/3", "/trackers/3")
      _client.send_message(address, osc_arguments)
    # printdata(address, osc_arguments)
    
  except ValueError: pass

# 8点トラッキング
def bridge8A(address: str, *osc_arguments: List[str]):
  # 8点
  # 腰 /tracking/trackers/2   -> /tracking/trackers/1
  # 右足 /tracking/trackers/5  -> /tracking/trackers/2
  # 右もも /tracking/trackers/6 -> /tracking/trackers/4  
  # 左足 /tracking/trackers/3  -> /tracking/trackers/3
  # 左もも /tracking/trackers/4 -> /tracking/trackers/5

  try:
    if (address.find("/tracking/trackers/2") > -1):
      address = address.replace("/tracking/trackers/2", "/tracking/trackers/1")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/5") > -1):
      address = address.replace("/tracking/trackers/5", "/tracking/trackers/2")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/3") > -1):
      address = address.replace("/tracking/trackers/3", "/tracking/trackers/3")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/6") > -1):
      address = address.replace("/tracking/trackers/6", "/tracking/trackers/4")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/4") > -1):
      address = address.replace("/tracking/trackers/4", "/tracking/trackers/5")
      _client.send_message(address, osc_arguments)      
    # printdata(address, osc_arguments)
 
  except ValueError: pass

# 8点トラッキング
def bridge8B(address: str, *osc_arguments: List[str]):
  # 8点
  # 腰 /tracking/trackers/2   -> /tracking/trackers/1
  # 右足 /tracking/trackers/5  -> /tracking/trackers/2
  # 左足 /tracking/trackers/3  -> /tracking/trackers/3

  # 右肘 /tracking/trackers/7 -> /tracking/trackers/8
  # 左肘 /tracking/trackers/8 -> /tracking/trackers/7

  try:
    if (address.find("/tracking/trackers/1") > -1):
      # address = address.replace("/tracking/trackers/1", "/tracking/trackers/1")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/2") > -1):
      address = address.replace("/tracking/trackers/2", "/tracking/trackers/6")
      _client.send_message(address, osc_arguments)      
    elif (address.find("/tracking/trackers/5") > -1):
      address = address.replace("/tracking/trackers/5", "/tracking/trackers/2")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/3") > -1):
      address = address.replace("/tracking/trackers/3", "/tracking/trackers/3")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/7") > -1):
      address = address.replace("/tracking/trackers/7", "/tracking/trackers/8")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/8") > -1):
      address = address.replace("/tracking/trackers/8", "/tracking/trackers/7")
      _client.send_message(address, osc_arguments)
    # printdata(address, osc_arguments)
 
  except ValueError: pass

# 11点トラッキング
def bridge11(address: str, *osc_arguments: List[str]):
  # printdata(address, osc_arguments)
  # 11点
  # 頭 /tracking/trackers/head -> /tracking/trackers/head
  # 胸 /tracking/trackers/1   -> /tracking/trackers/1
  # 腰 /tracking/trackers/2   -> /tracking/trackers/6 
  # 左足 /tracking/trackers/3  -> /tracking/trackers/3
  # 左もも /tracking/trackers/4 -> /tracking/trackers/5
  # 右足 /tracking/trackers/5  -> /tracking/trackers/2
  # 右もも /tracking/trackers/6 -> /tracking/trackers/4
  # 右肘 /tracking/trackers/7 -> /tracking/trackers/8
  # 左肘 /tracking/trackers/8 -> /tracking/trackers/7
  try:
    if (address.find("/tracking/trackers/1") > -1):
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/2") > -1):
      address = address.replace("/tracking/trackers/2", "/tracking/trackers/6")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/3") > -1):
      address = address.replace("/tracking/trackers/3", "/tracking/trackers/4")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/4") > -1):
      address = address.replace("/tracking/trackers/4", "/tracking/trackers/5")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/5") > -1):
      address = address.replace("/tracking/trackers/5", "/tracking/trackers/2")
      _client.send_message(address, osc_arguments) 
    elif (address.find("/tracking/trackers/6") > -1):
      address = address.replace("/tracking/trackers/6", "/tracking/trackers/3")
      _client.send_message(address, osc_arguments) 
    elif (address.find("/tracking/trackers/7") > -1):
      address = address.replace("/tracking/trackers/7", "/tracking/trackers/8")
      _client.send_message(address, osc_arguments)
    elif (address.find("/tracking/trackers/8") > -1):
      address = address.replace("/tracking/trackers/8", "/tracking/trackers/7")
      _client.send_message(address, osc_arguments)
    printdata(address, osc_arguments)

  except ValueError: pass

def printdata(address: str, *osc_arguments: List[str]):
    print(address + "  " + str(osc_arguments[0]))

def osc_loop():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
      default="0.0.0.0", help="The ip to listen on")
    parser.add_argument("--port",
      type=int, default=PORT, help="The port to listen on")
    args = parser.parse_args()

    _dispatcher = dispatcher.Dispatcher()
    _dispatcher.map("/*", bridge)
    # _dispatcher.map("/*", passthrough)

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), _dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

def printHost():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    print("{} {}".format(host, ip))
 
if __name__ == "__main__":
    printHost()
    osc_loop()