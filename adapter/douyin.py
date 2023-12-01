import datetime

from network.websocket_mapping import Websocket
from protobuf.douyin_pb2 import PushFrame, ChatMessage, GiftMessage
from utils import douyin_util
from utils.logger import init_logger

# 定义全局变量logger
logger = init_logger()


# 注册连接事件
def on_open(ws, message):
    print('on_open')


# 注册接收事件
def on_message(ws, message):
    #  解析websocket 推送数据
    response, frame = douyin_util.parse_response(message)

    # 如果需要持续推送，则发送心跳包给平台
    if response.need_ack:
        send_push_frame = PushFrame()
        send_push_frame.payload_type = 'ack'
        send_push_frame.payload = response.internal_ext.encode('utf-8')
        send_push_frame.LogID = frame.LogID
        ws.send(send_push_frame.SerializeToString())

    # 5.获取数据内容(需根据不同method，使用不同的结构对象对 数据 进行解析)注意:此处只处理 WebcastChatMessage ，其他处理方式都是类似的。
    for message in response.messages:
        # 获取对应的Message protobuf对象，可全局搜索：webcast.im.XXX，比如：webcast.im.GiftMessage
        # 大幕内容
        if "WebcastChatMessage" == message.method:
            # print("message：", message)
            # print("---------------message-------------------")
            # chat_message_bytes = gzip.decompress(message.payload)
            # print("chat_message_bytes：", chat_message_bytes)
            chat_message = ChatMessage()
            chat_message.ParseFromString(message.payload)
            now = datetime.datetime.now()
            logger.info(f'{now.strftime("%H:%M:%S")}【弹幕】 {chat_message.user.nickName}：{chat_message.content}')

        # 礼物内容
        if "WebcastGiftMessage" == message.method:
            gift_message = GiftMessage()
            gift_message.ParseFromString(message.payload)
            now = datetime.datetime.now()
            logger.error(f'{now.strftime("%H:%M:%S")}【礼物】 {gift_message.user.nickName}：{gift_message.gif.describe}')


# 注册连接错误事件
def on_error(ws, message):
    print('on_error', message)


# 注册关闭事件
def on_close(ws, message):
    print('on_close')


# 连接抖音直播间信息
def connect_douyin_live_room():
    # 获取直播间地址
    live_url = 'https://live.douyin.com/567789235524'
    # 获取直播间socket url
    wss_url, ttwid = douyin_util.fetch_live_room_wss_url(live_url)
    logger.info(f'wss_url：{wss_url}')
    logger.info(f'ttwid：{ttwid}')
    # 创建socket连接
    websocket = Websocket(wss_url)
    # 注册连接事件
    websocket.register_open(on_open)
    # 注册接收事件
    websocket.register_message(on_message)
    # 注册连接错误事件
    websocket.register_error(on_error)
    # 注册关闭事件
    websocket.register_close(on_close)
    # 设置请求头信息
    websocket.set_header(
        {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'Upgrade',
            'Host': 'webcast5-ws-web-lf.douyin.com',
            'Origin': 'https://live.douyin.com',
            'Pragma:': 'no-cache',
            'Sec-Websocket-Extensions:': 'permessage-deflate; client_max_window_bits',
            'Sec-Websocket-Key:': 'VCZM2MxeS9C1t+Td9TRk6B==',
            'Sec-Websocket-Version:': '13',
            'Upgrade:': 'websocket',
            'User-Agent:': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
    )
    # 设置cookie信息
    websocket.set_cookie('ttwid=' + ttwid)
    # 连接websocket
    websocket.connect()
