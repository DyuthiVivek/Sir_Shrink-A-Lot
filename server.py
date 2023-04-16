import socket
from _thread import *
from player import Player
import pickle
import pygame

server = "172.16.145.21"
port = 5555

initial_ht = 100
initial_wt = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


players = [[0,0,initial_wt, initial_ht,1,0], [1027-50,0,initial_wt, initial_ht,1,1]] #player object stored on the server

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048*4))
            print("received data")
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

