import socket
import json

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        stringa=input('Inserire #list per visualizzare i voti inseriti \nInserire #set /nomestudente per inserire uno studente \nnInserire #put /nomestudente/materia/voto/ore per aggiungere i voti allo studente \nnInserire #get /nomestudente per richiedere i voti dello studente \n #exit \n')
        if (stringa.find('#exit') != -1):
            break

        messaggio={
            'stringa' : stringa
        }
        messaggio=json.dumps(messaggio)
        s.sendall(messaggio.encode("UTF-8"))
        deserialized_dict=s.recv(1024)
        if (stringa.find('#list') != -1):
            deserialized_dict = json.loads(deserialized_dict)
        elif (stringa.find('#get') != -1):
            deserialized_dict = json.loads(deserialized_dict)
        else:
            deserialized_dict = deserialized_dict.decode()
        print("\n")
        print(deserialized_dict,"\n")