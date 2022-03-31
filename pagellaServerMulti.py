#nome del file : pagellaServerMulti.py

import socket
from threading import Thread
import json


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225

#Versione 1 
def ricevi_comandi1(sock_service,addr_client):
    while True:
        data=sock_service.recv(1024)
        if not data: 
                break
        data=data.decode()
        data=json.loads(data)        
        #1. recuperare dal json studente, materia, voto e assenze
        #2. restituire un messaggio in json contenente studente, materia e una valutazione testuale :
        # voto < 4 Gravemente insufficiente
        # voto [4..5] Insufficiente
        # voto = 6 Sufficiente
        # voto = 7 Discreto 
        # voto [8..9] Buono
        # voto = 10 Ottimo

        stud=data['stud']
        mat=data['mat']
        voti=data['voti']
        assenze=data['assenze']
        risultato=""
        if voti<4:
            risultato="Gravemente insufficiente"
        elif voti==4 or voti==5:
            risultato="Insufficiente"
        elif voti==6:
            risultato="Sufficiente"
        elif voti==7:
            risultato="Discreto"
        elif voti==8 or voti==9:
            risultato="Buono"
        else:
            risultato="Ottimo" 
        risultato=str(risultato)
        sock_service.sendall(risultato.encode("UTF-8"))

def ricevi_comandi2(sock_service,addr_client):
    while True:
        data=sock_service.recv(1024)
        if not data:
            break
        data=data.decode{}
        data=json.loads(data)

    studente=data['studente']
    pagella=['pagella']

    assenze=0
    media=0
    for i,p in enumerate(pagella):
        media+=int(p[1])
        assenze+=int(p[2])
    media=media/i
    messaggio={'studente':studente,
    'media':media,
    'assenze':assenze}
    print("Dati inviati:")
    print(messaggio)
    messaggio=json.dumps(messaggio)
    sock_service.sendall(messaggio.encode("UTF-8"))
sock_service.close()
       
  #....
  #1.recuperare dal json studente e pagella
  #2. restituire studente, media dei voti e somma delle assenze :

#Versione 3
def ricevi_comandi3(sock_service,addr_client): 
    while True:
        data=sock_service.recv(1024)
        if not data:
            break
        data=data.decode{}
        data=json.loads(data)

    pp=pprint.PrettyPrinter(indent=4)
    tabellone[]
    
    for stud in data:
        pagella=data[stud]
        assenze=0
        media=0
        for i,p in enumerate(pagella):
            media+=int(p[1])
            assenze+=int(p[2])
        media=media/i
        messaggio={'studente':studente,
        'media':media,
        'assenze':assenze}
        tabellone.append(messaggio)
    print("Dati inviati:")
    messaggio=tabellone
    messaggio=json.dumps(messaggio)
    sock_service.sendall(messaggio.encode("UTF-8"))
sock_service.close()
  


def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nCreo un thread per servire le richieste ")
        try:
            Thread(target=ricevi_comandi1,args=(sock_service,addr_client)).start()
        except:
            print("il thread non si avvia")
            sock_listen.close()
        
def avvia_server(SERVER_ADDRESS,SERVER_PORT):
    sock_listen=socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock_listen.bind((SERVER_ADDRESS,SERVER_PORT))
    sock_listen.listen(5)
    print("Server in ascolto su %s." %str((SERVER_ADDRESS,SERVER_PORT)))
    ricevi_connessioni(sock_listen)

if __name__=='__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)