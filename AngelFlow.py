import numpy as np

class layer:
    """Dummy layer class."""
    pass

class matlayer(layer):
    """Matrix layer."""
    def __init__(self, io = None, mat = None):
        if mat is None:
            if io is None:
                #shape is assumed to be (1, 1)
                self.mat = np.mat("1+0j")
            else:
                try: io[0]
                except TypeError:
                    io = (io, io)
                #'eye'
                self.mat = np.mat(np.eye(io[-1],io[0], dtype=np.complex_))
        else:
            self.mat = np.mat(mat)
                
    @property
    def io(self):
        s = self.mat.shape
        return (s[1],s[0])

class addlayer(layer):
    "Vector additive layer"
    def __init__(self, io = None, vec = None):
        if vec is None:
            if io is None:
                #shape is assumed to be (1, 1)
                self.vec = np.asarray([[0+0j]])
            else:
                try:
                    if io[0] != io[-1]: raise ValueError("io of an additive layer must be square")
                except TypeError:
                    io = (io, io)
                self.vec = np.asarray([[0+0j]]*io[0])
    
    @property
    def io(self):
        return (self.vec.shape[0], self.vec.shape[0])


