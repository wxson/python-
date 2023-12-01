from websocket import WebSocketApp


class Websocket:
    # 连接
    _wss_url = None
    # 连接事件
    _on_open = None
    # 消息事件
    _on_message = None
    # 错误事件
    _on_error = None
    # 关闭事件
    _on_close = None
    # header
    _header = None
    # cookie
    _cookie = None

    def __init__(self, wss_url):
        self.wss_url = wss_url.rstrip('/')

    def register_open(self, on_open):
        self._on_open = on_open

    def register_message(self, on_message):
        self._on_message = on_message

    def register_error(self, on_error):
        self._on_error = on_error

    def register_close(self, on_close):
        self._on_close = on_close

    def set_header(self, header):
        self._header = header

    def set_cookie(self, cookie):
        self._cookie = cookie

    def connect(self):
        ws = WebSocketApp(
            url=self.wss_url,
            header=self._header,
            cookie=self._cookie,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close
        )
        ws.run_forever()
