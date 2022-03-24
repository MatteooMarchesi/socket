import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
class Client():
    def genera_richieste(num,address,port):
        sock_service=socket.socket()
        sock_service.connect((address,port))
        return sock_service

    def invia_comandi(self,sock_service):
        while True:
            try:
                primoNum=input("inserire il numero se si vuole uscire scrivere exit() ") 
                if primoNum=="exit()":
                    break
                primoNum=float(primoNum)
                operazione=input("Inserisci l'operazione che si vuole fare  (+,-,*,/,%)")
                secondoNum=float(input("Digita il secondo numero "))
                dati={'primoNum':primoNum, 'operazione':operazione, 'secondoNum':secondoNum}
            except EOFError:
                print("\nOkay. Exit")
                break
            if not dati:
                print("Non puoi inviare una stringa vuota")
                continue
            if dati == '0':
                print("chiudo connessione")
                sock_service.close()
                break

            dati=json.dumps(dati) 
            sock_service.sendall(dati.encode("UTF-8"))
            data=sock_service.recv(1024) 
            print("Risultato uscito : ",data.decode()) 

c1=Client()
sock_serv=c1.genera_richieste(SERVER_ADDRESS,SERVER_PORT)
c1.invia_comandi(sock_serv)