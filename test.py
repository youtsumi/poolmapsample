from multiprocessing import Pool
import numpy
ccds = range(9)+range(10,104)

class Ccd:
    def __init__(self,x):
	self.x=x

    def processA(self):
	"""write something what you want to do"""
	self.ret=self.x**2

    def processB(self,thresh):
	"""write something what you want to do"""
	if self.ret>thresh:
	    self.ret=numpy.sqrt(self.x)
	else:
	    self.ret=0

def onechip(x):
    ccd=Ccd(x)
    ccd.processA()
    ccd.processB(1024)
    return ccd

if __name__ == '__main__':
    pool = Pool(processes=16)
    result = pool.map(onechip, ccds)
    for ccd in  result:
	print ccd.x, ccd.ret
