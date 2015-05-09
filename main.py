# - * - Codage: utf-8 - * -
from tkinter import *
from dialog import *
from socket import *
from threading import *
from time import *

threadOn=True

def broadcast_client():
	"""Thread signalant à intervalle régulier la présence du logiciel à l'ensemble du réseau par un broadcast."""
	cs = socket(AF_INET, SOCK_DGRAM)
	cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	while threadOn:
		cs.sendto(b'Bonjour.', ('255.255.255.255', 4490))
		sleep(10)
	cs.close()
	
def getIpLocal():
	"""Fonction pour récuperer l'adresse local de l'ordinateur pour éviter de se broadcast soi même"""
	s = socket(AF_INET, SOCK_DGRAM)
	s.connect(("192.0.0.0", 666))
	return s.getsockname()[0]
	s.close()
	
def getClientsConnectes():
	"""Fonction pour actualiser la liste des clients en ligne"""
	cs = socket(AF_INET, SOCK_DGRAM)
	cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	try:
		cs.bind(('255.255.255.255', 4490))
	except:
		print ('failed to bind')
		cs.close()
		raise
		cs.blocking(0)

	ipl = getIpLocal()

	while threadOn:
		data = cs.recvfrom(20)
		if data[1][0] != ipl:
			print (data[1][0] + " >> " + data[0].decode('UTF-8'))
	cs.close()
	exit()

def fetch():
    """Affiche la sélection actuelle de la liste"""
    print(list.get(ACTIVE))

def refreship():

	list.delete(0,END)
	cs = socket(AF_INET, SOCK_DGRAM)
	try:
		cs.bind(('255.255.255.255', 4490))
	except:
		print ('failed to bind')
		cs.close()
		raise
		cs.blocking(0)

	cs.settimeout(1)


	ip_list = []
	time1 = time()
	ipl = getIpLocal()
	i = 0
	while time() - time1 < 10.0:
		try :
			data = cs.recvfrom(20)
			if data[1][0] != ipl:
				print ("Client trouvé en : " + data[1][0]) #Affiche dans un terminal (si présent)
				list.insert(i, data[1][0]) #Ajoute au tableau 
				i+=1
			else :
				print ("Local Broadcast")
		except :
			print ("Time out")
	cs.close()


window = Tk() # Fenetre principale
window.title("Principale") # On modifie le tritre de la fenêtre
window.configure(background="white") #On met le fond blanc

#On initialise l'objet de la boite de dialogue
test=WindowDialog()



champ_label = Label(window, text="Ordinateur connecté au réseau : ",relief=FLAT, background ="white") # On créer un "label" avec un relief "FLAT" et un fond blanc



list = Listbox(window, relief=FLAT, background ="white", width=50, height=20,font="arial 12 ") # On créer un "label" avec un relief "FLAT" et un fond blanc


picture2 = PhotoImage(file='dialog.gif') #Met une image à la place du texte
bouton_com = Button(window, image=picture2, command=lambda:test.new_windows(list.get(ACTIVE)), relief=FLAT, background ="#3498db", fg="white", font="arial 15 bold") # Lorsqu'on clique ?a active la fonction fetch, style en relief groove


picture = PhotoImage(file='refresh.gif') #Met une image à la place du texte
bouton_rafraichir = Button(window, image=picture, command=lambda:Thread(target = refreship).start(), relief=FLAT, background ="#3498db", fg="white",font="arial 15 bold") # Lorsqu'on clique ?a active la fonction fetch, style en relief groove


#On met en page
champ_label.grid(row=1, sticky=W,padx=5, pady=3)
list.grid(row =2,rowspan=16, sticky =W, padx=10, pady=5)
bouton_com.grid(row =2,column =3, sticky =W, padx=10)
bouton_rafraichir.grid(row =3,column =3, sticky =W, padx=10)


Thread(target = broadcast_client).start()


window.mainloop()

