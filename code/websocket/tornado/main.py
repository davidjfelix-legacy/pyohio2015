#!/usr/bin/env python3

from tornado import websocket, web, ioloop

HACKY_DB = {
    "sockets" : []
}

class SubscribeSocket(websocket.WebSocketHandler):
    def open(self):
        HACK_DB['sockets'].append(self)

    def on_close(self):
        HACK_DB['sockets'].remove(self)

class PublishHandler(web.RequestHandler):
    def post(self):
        for socket in HACKY_DB['sockets']:
            socket.write_message(self.request.body)
        self.set_status(200)
        self.write()

def main():
    app = web.Application([
        web.url(r"/sub", SubscribeSocket),
        web.url(r"/pub", PublishHandler),
    ])
    app.listen(8080)
    ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()

