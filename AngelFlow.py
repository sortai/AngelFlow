import numpy as np

class layer:
    """Dummy layer class."""
    pass

class llayer(layer):
    """Linear layer."""
    def __init__(self, imat = None, ivec = None, shape = None):
        if shape is not None and len(shape)>2: shape = (shape[0], shape[-1])
        if imat is None:
            if shape is None: self.mat = np.mat("1+0j")
            else:
                #truncated identity matrix
                self.mat = np.mat(np.identity(max(shape),dtype=np.complex_)[:min(shape)])
                if shape[0]>shape[1]: self.mat = self.mat.T
        else: self.mat = np.mat(imat)
        if ivec is None:
            if shape is None: self.vec = np.mat("0+0j")
            else: self.vec = np.mat(np.zeros(shape[0]),dtype=np.complex_)
        else: self.vec = np.mat(ivec)
        
