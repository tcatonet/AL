class RemoveFileFromBacthFileCommand:
    def __init__(self,bacthFile):
        self.bacthFile = bacthFile

    def removeFile(self):
        if len(bacthFile) >0:
            file = self.bacthFile[0]
            del bacthFile[0]
            return file
        else:
            raise Exception("No File in BacthFile")