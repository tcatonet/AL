class DeplaceBacthFileCommand:
    def __init__(self,origine,Bacthfile):
        self.Bacthfile = Bacthfile
        self.Bacthfile.worker = origine
