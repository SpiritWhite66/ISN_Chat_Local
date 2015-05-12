# -*- coding: UTF-8 -*-

class FileLog :
    """ gère les log et autres fichier"""
    
    def write_log(self):
        """ écrit chaque connexion dans un fichier de log"""
        log = "Pseudo" + "24/04/21:41 \n"
        file_log = open("log.txt", "a") 
        file_log.write(log)
        file_log.close()
    
    def remove_log(self):
        """On vide le fichier de log"""
        file_log = open("log.txt", "w") 
        file_log.write("")
        file_log.close()
    
    def read_line(self):
        """Lit dans le fichier pass.txt le pseudo et le mot de passe : 
            - En ligne 1 il y a le pseudo
            - En ligne 2 le password"""
        self.read_ligne = []
        f = open('pass.txt','r')
        for ligne in f:
            self.read_ligne.append(ligne)
                    
    def getPass(self):
        """Retourne le password
        |!!!!| UNIQUEMENT APRES read_line |!!!!|
        """
        password = str(self.read_ligne[2])[9:len(self.read_ligne[2])]
        return password
    
    def getPseudo(self):
        """Retourne le password
        |!!!!| UNIQUEMENT APRES read_line |!!!!|
        """
        pseudo = str(self.read_ligne[1])[7:len(self.read_ligne[1])-1]

        return pseudo


            
