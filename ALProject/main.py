# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Projet.Modele.BacthFile import BacthFile
from Projet.Modele.File import File
from Projet.Modele.FileManager import FileManager
from Projet.Modele.Worker import Worker
#from Projet.RessouceExterne.BachtFileGenerator import BatchFileGenerator
from Projet.Exposition.APIfileManager import APIfileManager
from Projet.RessouceExterne.BachtFileGenerator import BatchFileGenerator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #ENVIRONNEMENT#

    myAPI = APIfileManager()
    myAPI.init()
    generator = BatchFileGenerator(myAPI)

    generator.start()  # démarre le thread,
    myAPI.fileManager.start()  # démarre le thread,


    #ENVIRONNEMENT#





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
