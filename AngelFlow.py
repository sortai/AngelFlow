import numpy as np

class layer:
    """Dummy layer class."""
    pass

class mlayer(layer):
    """Matrix layer."""
    def __init__(self, io = None, imat = None):
        if imat is None:
            if io is None:
                #shape is assumed to be (1, 1)
                self.mat = np.mat("1+0j")
                self.vec = np.mat("0j")
            else:
                #truncated identity
                self.mat = np.mat("; ".join("0+0j "*min(i,io[0])+"1+0j"*int(i<io[0])+" 0+0j"*max(io[0]-1-i,0) for i in range(io[1])))
        else:
            self.mat = np.mat(imat)
                
    @property
    def io(self):
        s = self.mat.shape
        return (s[1],s[0])
