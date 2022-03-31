#nome del file : pagellaClientMulti.py
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4

#Versione 1 
def genera_richieste1(num,address,port):
    start_time_thread=time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    #1. Generazione casuale:
    #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
    studenti=random.randint(1,5) 
    
    if studenti==1:
        stud="Marchesi"
    elif studenti==2:
        stud="D'alba"
    elif studenti==3:
        stud="Farè"
    elif studenti==4:
        stud="Fulginiti"
    else:
        stud="Faulisi"

    #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
    materia=random.randint(1,5)

    if materia==1:
        mat="Matematica"
    elif materia==1:
        mat="Italiano"
    elif materia==1:
        mat="Inglese"
    elif materia==1:
        mat="Storia"
    else:
        mat="Geografia"

    #   di un voto (valori ammessi 1 ..10)
    voti=random.randint(1,10)

    #   delle assenze (valori ammessi 1..5) 
    assenze=random.randint(1,5)

    #2. comporre il messaggio, inviarlo come json
    #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    messaggio={'stud':stud, 'mat':mat, 'voti':voti, 'assenze':assenze}
    messaggio=json.dumps(messaggio) #serve a convertire un oggetto Python in una stringa 
    s.sendall(messaggio.encode("UTF-8")) #definisce che ogni carattere è composto da una sequenza di uno o più byte.
    data=s.recv(1024)
    print("Valutazione: ",data.decode())
    #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
        print(f"{threading.current_thread().name}: Valutazione: {data.decode()}")
    s.close()
    end_time_thread=time.time()
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)




#Versione 2 
def genera_richieste2(num,address,port): 
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
  #....
  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
  
    studenti=['Marchesi','Dalba','Fulginiti','farè','Faulisi']
    materie=['Matematica','Inglese','Storia','Gpoi']
    studente=studenti[random.randint(0,4)]
    pagella[]
    for m in materie:
        voto=random.randint(1,10)
        assenze=random.randint(1,5)
        pagella.append((m,voto,assenze))

  #2. comporre il messaggio, inviarlo come json
    messaggio={'studente':studente, 'pagella':pagella}
    print(f"Dati inviati al server {messaggio}")
    messaggio=json.dumps(messaggio) #serve a convertire un oggetto Python in una stringa 
    s.sendall(messaggio.encode("UTF-8")) #definisce che ogni carattere è composto da una sequenza di uno o più byte.
    data=s.recv(1024)
    data=data.decode()
    data=json.loads(data)
    print(f"Dati: {data}")

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name}: Valutazione: {data.decode()}")
    s.close()

  
    
#Versione 3
def genera_richieste3(num,address,port): 
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

  #....
  #   1. Per ognuno degli studenti ammessi: 5 cognomi a caso scelti da una lista
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: tabellone={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9,3), ("Storia",8,2), ("Geografia",8,1)],
  #                       "Cognome2":[("Matematica",7,2), ("Italiano",5,3), ("Inglese",4,12), ("Storia",5,2), ("Geografia",4,1)],
  #                        .....}
    studenti=['Marchesi','Dalba','Fulginiti','farè','Faulisi']
    materie=['Matematica','Inglese','Storia','Gpoi']
    tabellone{}
    for stud in studenti:
        pagella[]
        for m in materie:
            voto=random.randint(1,10)
            assenze=random.randint(1,5)
            pagella.append((m,voto,assenze))
        tabellone[stud]=pagella

#2. comporre il messaggio, inviarlo come json
    print("Dati inviati")
    pp.pprint.PrettyPrinter(indent=4)
    pp.pprint(tabellone)
    tabellone=json.dumps(tabellone) #serve a convertire un oggetto Python in una stringa 
    s.sendall(tabellone.encode("UTF-8")) #definisce che ogni carattere è composto da una sequenza di uno o più byte.
    data=s.recv(1024)
    data=data.decode()
    data=json.loads(data)
    print("Dati inviati")
    pp.pprint(data)

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        for elemento in data:
            print(f"{threading.current_thread().name}: Valutazione: {data.decode()}")
    s.close()

  #3  ricevere il risultato come json e stampare l'output come indicato in CONSOLE CLIENT V.3

    if __name__ == '__main__': 
        start_time=time.time()
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    for i in range(NUM_WORKERS):
        genera_richieste1(i,SERVER_ADDRESS,SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    for num in range(NUM_WORKERS):
        t1=threading.Thread(target=genera_richieste1, args=(num,SERVER_ADDRESS,SERVER_PORT))
        t2=threading.Thread(target=genera_richieste2, args=(num,SERVER_ADDRESS,SERVER_PORT))
        t3=threading.Thread(target=genera_richieste3, args=(num,SERVER_ADDRESS,SERVER_PORT))
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
    for num in range(NUM_WORKERS):
        p1=multiprocessing.Process(target=genera_richieste1,args=(num,SERVER_ADDRESS,SERVER_PORT))
        p2=multiprocessing.Process(target=genera_richieste2,args=(num,SERVER_ADDRESS,SERVER_PORT))
        p3=multiprocessing.Process(target=genera_richieste3,args=(num,SERVER_ADDRESS,SERVER_PORT))
    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    for p1 in range(NUM_WORKERS):
        p1=multiprocessing.Process(target=genera_richieste1, args=(num,SERVER_ADDRESS,SERVER_PORT))
        process.append(p1)

    # 8 avvio tutti i processi
    for p1 in process:
        p1.start()
    # 9 aspetto la fine di tutti i processi
    for p1 in process:
        p1.join() 

    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)