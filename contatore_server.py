import socket 
import json

HOST="127.0.0.1"
PORT=65435

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("[*] In ascolto su %s: %d"%(HOST,PORT))
    clientscoket, address=s.accept()
    con=1
    with clientscoket as cs:
        print("Connessione da ",address)
        while True:
            data=cs.recv(1024)
            if not data:
                break 
            data=data.decode()
            stringa=data
            print("Stringa ricevuta "+stringa)
            if stringa!="KO":
                ris=stringa+" "+str(con)
                con+=1
            ris=str(ris)
            cs.sendall(ris.encode("UTF-8")) #manda il vettore in risposta al client

    
