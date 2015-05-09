from tkinter import *
#from PIL import Image, ImageTk
from log import *
from hashlib import *

class connect :
    """ Affiche la fenetre de dialogue"""
    
    def verif(self):
        pseudo = self.valeurpseudo.get()
        password = self.valeurpass.get()
        read=FileLog()
        read.read_line()
        passcrypt = sha256(password.encode('utf-8') + b"e2556fdfsd156321dvf54gf875")
        pseudocrypt = sha256(pseudo.encode('utf-8') + b"e2556fdfsd156321dvf54gf875")        
        if (pseudocrypt.hexdigest()==str(read.getPseudo())) & (passcrypt.hexdigest() == str(read.getPass())):
            print("Connexion réussi ....")
            self.accept_connexion()
        else :
            print('refused')
    
    def accept_connexion(self):
        self.fenetre.quit()
        
        
    def Dialog_Connect(self):
        """fenetre de dialogue lors de la connexion"""
        self.fenetre = Tk()
        self.fenetre.title("Connexion")
        self.fenetre.configure(background="white")
       
        

        #Canevas = Canvas(self.fenetre,background ="white", relief=FLAT )              
        #photo = ImageTk.PhotoImage(file="logo.jpg")                  
        #Canevas.config(height=photo.height(),width=photo.width(),background ="white", relief=FLAT)  
        #Canevas.create_image(0,0,anchor=NW,image=photo)     
        
        
        pseudo_label =Label(self.fenetre, text="Pseudo : ",background ="white")
        pass_label =Label(self.fenetre, text="Password : ",background ="white" )
        
        self.valeurpseudo = StringVar()
        self.valeurpseudo.set("Pseudo")
        ligne_pseudo = Entry(self.fenetre, textvariable=self.valeurpseudo)
 
        self.valeurpass = StringVar()
        self.valeurpass.set("password")
        ligne_pass = Entry(self.fenetre, textvariable=self.valeurpass, show="*")
        
        bouton_connect = Button(self.fenetre, text='Connexion',command=self.verif, width=20,height=2, relief=FLAT, background ="#8ccff9") #On tente la connexion 
        #Canevas.grid(row=1,columnspan = 4, sticky=N)
        pseudo_label.grid(row=2, sticky=W, padx=10)
        pass_label.grid(row =3, sticky =W, padx=10)
        ligne_pseudo.grid(row =2,column =2, sticky =W,padx=10)
        ligne_pass.grid(row =3,column =2, sticky =W, padx=10)
        bouton_connect.grid(row=2,column = 3,rowspan=2, sticky=W,padx=10)
        
        self.fenetre.mainloop()
        
    
test=connect()
test.Dialog_Connect()
