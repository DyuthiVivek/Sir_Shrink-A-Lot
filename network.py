import socket
import pickle
import sys


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.16.145.21"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            print("reached here")
        
            return pickle.loads(self.client.recv(2048*4))
        except:
            print("not connecting")
            pass

    def send(self, data):
        try:
            if data[0] == None:
                self.client.send(pickle.dumps(data))
                sys.exit()
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*4))
        except socket.error as e:
            print(e)
