import json
import socket

SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22224

def invia_comandi(sock_service):
    while True:
        num1=input("Digita numero, se invece vuoi uscire digita exit() ")
        if num1=="exit()":
            break
        num1=float(num1)
        operazione=input("Inserisci l'operazione desiderata (+,-,*,/,%)")
        num2=float(input("Digita il secondo numero "))
        messaggio={'num1':num1, 'operazione':operazione, 'num2':num2}
        messaggio=json.dumps(messaggio)#serve a convertire un oggetto Python in una stringa 
        sock_service.sendall(messaggio.encode("UTF-8"))#definisce che ogni carattere è composto da una sequenza di uno o più byte.
        data=sock_service.recv(1024)#recv() viene utilizzata per ricevere dati dai socket 
        print("Risultato: ",data.decode()) 

def  connessione_server(address, port):
    sock_service=socket.socket()
    sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
    print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
    invia_comandi(sock_service)

if __name__=='__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT) 