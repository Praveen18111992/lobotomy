import SocketServer
import threading
from blessings import Terminal
t = Terminal()


class ScalpelRequestHandler(SocketServer.BaseRequestHandler):
    """
    Handle socket request

    TODO: Pass data off to analysis engine
    """
    def handle(self):
        data = self.request.recv(1024)
        self.request.send(data)
        return


class ScalpelServer(object):
    """
    The ScalpelServer is meant to handle all in bound data
    from the on device agent
    """

    def __init__(self):
        super(ScalpelServer, self).__init__()
        self.address = ("localhost", 6666)
        self.server = SocketServer.TCPServer(self.address, ScalpelRequestHandler)
        self.ip, self.port = self.server.server_address

    def run(self):
        """
        Start threading the new Socket Server instance
        """
        try:
            thread = threading.Thread(target=self.server.serve_forever)
            thread.setDaemon(True)
            thread.start()
        except Exception as e:
            raise e

    def stop(self):
        """
        Stop the current SocketServer instance
        """
        self.server.socket.close()
