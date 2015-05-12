# -*- coding: UTF-8 -*-
from Tkinter import *
from socket import *
from threading import *
from time import *

def getIpLocal():
	"""Fonction pour récuperer l'adresse local de l'ordinateur pour éviter de se broadcast soi même"""
	s = socket(AF_INET, SOCK_DGRAM)
	s.connect(("192.0.0.0", 666))
	return s.getsockname()[0]
	s.close()

class WindowDialog :
    """ Affiche la fenetre de dialogue"""

    def __init__(self):
        """ On définit les variables"""
        self.ip = "00.000.000.001"
        self.ip_l = getIpLocal()
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.settimeout(30)

    def setIp(self, new_ip):
        """modifie la valeur de l'ip"""
        self.ip=new_ip
        
    def getIp(self):
        """écrit l'ip dans la console et retourne"""
        print(self.ip)
        return self.ip

    def add_message(self, message, ip) :
        """ ajoute le message au widget texte"""
        self.dialog_texte.insert(END ,ip + " : "+ str(message) +"\n")
        
    def send_message(self, message) :
        """ Fonction pour envoyer des messages à l'ordinateur distant."""
        self.s.sendall(message.encode('UTF-8'))
        self.add_message(message, self.ip_l)
        
        
    def recevoir(self) :
        """Fonction lançant le serveur et acceptant les connexions."""
        h= ''
        p= 7891
        s = socket(AF_INET, SOCK_STREAM)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((h, p))
        s.listen(1)
        conn, addr = s.accept()
        print('Connected by', addr)
        data= " "
        while not(not data or data==b"\r\n"):
            data= conn.recv(1024)
            print(data.decode('UTF-8'))
            self.add_message(data.decode('UTF-8'), self.ip)
        conn.close()
        s.close()
        exit()
    
    def envoyer(self):
        """Client pour envoyer les messages (thread)"""
        h = self.ip
        p = 7891
        try:
            self.s.connect((h,p))
            self.add_message("Vous êtes connecté.", "Système")
        except:
            self.add_message("Erreur de connexion", "Système")
            self.bouton_send.config(state=DISABLED)
            self.s.close()
            exit()

    def new_windows(self, ip_adress) :
        """ Ouvre une nouvelle fenetre"""
        self.setIp(ip_adress)
        fenetre = Toplevel()
        fenetre.title("Dialogue")
        
        champ_label =Label(fenetre, text="En communication avec : " + self.ip)
        champ_label.pack()

        self.dialog_texte=Text(fenetre, width=50, height=10, relief=FLAT)
        self.dialog_texte.insert(END,'Patientez pendant la connexion... \n')
        self.dialog_texte.pack()
        
        self.valeurOneVar = StringVar()
        self.valeurOneVar.set("Entrer votre message")
        ligne_message = Entry(fenetre, textvariable=self.valeurOneVar)
        ligne_message.pack()
        
        
        self.bouton_send = Button(fenetre, text='Envoyer', command=lambda:self.send_message(self.valeurOneVar.get()), width=20,height=2, relief=FLAT, background ="#3498db") 
        self.bouton_send.pack()
        Thread(target = self.recevoir).start()
        Thread(target = self.envoyer).start()
        
        fenetre.mainloop()
