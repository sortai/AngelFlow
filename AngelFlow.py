import numpy as np

class layer:
    """Dummy layer class."""
    pass

class mlayer(layer):
    """Matrix layer."""
    def __init__(self, io = None, mat = None):
        if mat is None:
            if io is None:
                #shape is assumed to be (1, 1)
                self.mat = np.mat("1+0j")
                self.vec = np.mat("0j")
            else:
                #truncated identity
                self.mat = np.mat(np.eye(io[-1],io[0], dtype=np.complex_))
        else:
            self.mat = np.mat(mat)
                
    @property
    def io(self):
        s = self.mat.shape
        return (s[1],s[0])
