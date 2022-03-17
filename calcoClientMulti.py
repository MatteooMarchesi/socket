#calcolatrice client per calcoServer.py versione multithread
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22220
NUM_WORKERS=2

def genera_richieste(num,address,port):
    start_time_thread= time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except Exception as e:
        print(e)
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    #1. rimpiazzare questa parte con la generazione di operazioni e numeri random, non vogliamo inviare sempre 3+5 
    primoNumero=random.randint(1,100) #generazione di un numero casuale da 1 a 100, assegnandolo al primoNumero
    secondoNumero=random.randint(1,100) #generazione di un numero casuale da 1 a 100, assegnandolo al secondoNumero
    simbolo=random.randint(0,3) #generazione di un numero casuale da 1 a 3
    if simbolo==0:
        operazione="+"
    elif simbolo==1:
        operazione="-"
    elif simbolo==2:
        operazione="*"
    else:
        operazione="/"
    #assegno al simbolo un numero, per capire quale operazione eseguire
    

    #2. comporre il messaggio, inviarlo come json e ricevere il risultato
    
    messaggio={'primoNumero':primoNumero, 'operazione':operazione, 'secondoNumero':secondoNumero}
    messaggio=json.dumps(messaggio) #serve a convertire un oggetto Python in una stringa 
    s.sendall(messaggio.encode("UTF-8")) #definisce che ogni carattere è composto da una sequenza di uno o più byte.
    data=s.recv(1024)
    print("Risultato: ",data.decode()) 

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name}: Risultato: {data.decode()}") # trasforma il vettore di byte in stringa
    s.close()
    end_time_thread=time.time()
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)

if __name__ == '__main__':
    start_time=time.time()
    # 3 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    for i in range(NUM_WORKERS):
        genera_richieste(i,SERVER_ADDRESS,SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # 4 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # ad ogni iterazione appendo il thread creato alla lista threads
    for num in range(NUM_WORKERS):
        t1=threading.Thread(target=genera_richieste, args=(num,SERVER_ADDRESS,SERVER_PORT))
        threads.append(t1)

    # 5 avvio tutti i thread
    for t1 in threads:
        t1.start()

    # 6 aspetto la fine di tutti i thread 
    for t1 in threads:
        t1.join()
        
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # 7 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # ad ogni iterazione appendo il thread creato alla lista threads
    for p1 in range(NUM_WORKERS):
        p1=multiprocessing.Process(target=genera_richieste, args=(num,SERVER_ADDRESS,SERVER_PORT))
        process.append(p1)

    # 8 avvio tutti i processi
    for p1 in process:
        p1.start()
    # 9 aspetto la fine di tutti i processi
    for p1 in process:
        p1.join() 
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)
