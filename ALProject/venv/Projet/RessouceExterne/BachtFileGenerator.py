from Projet.Modele.Worker import Worker
from Projet.Modele.BacthFile import BacthFile
from Projet.Modele.File import File
from Projet.Exposition.APIfileManager import APIfileManager
import threading
import time


class BatchFileGenerator(threading.Thread):
    def __init__(self, APIfileManager):
        threading.Thread.__init__(self)
        self.name = "simulation file generator"
        self.fileManager = APIfileManager.fileManager
        self.limitAction=20
        self.API = APIfileManager

    def runGenerateFile(self,listFile):
        self.API.addBacthFile(listFile)
        #print (listFile)
        time.sleep(0.8)



    def run(self):

        while True:
            listfile = [File("Fichier1", "Blablabla"), File("Fichier2", "Blablabla"), File("Fichier3", "Blablabla"),
                        File("Fichier4", "Blablabla"), File("Fichier5", "Blablabla")]

            self.runGenerateFile(listfile)
