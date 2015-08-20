from multiprocessing import Pool
import numpy
ccds = range(9)+range(10,104)

class Ccd:
    def __init__(self,visit,ccd):
	self.visit=visit
	self.ccd=ccd

    def processA(self):
	"""write something what you want to do"""
	self.ret=self.ccd**2

    def processB(self,thresh):
	"""write something what you want to do"""
	if self.ret>thresh:
	    self.ret=numpy.sqrt(self.ccd)
	else:
	    self.ret=0

def onechip(ccd):
    ccd.processA()
    ccd.processB(1024)
    return ccd

if __name__ == '__main__':
    visits=range(100,200,2)
    targets=[]
    for visit in visits:
	for ccd in ccds:
	    targets.append(Ccd(visit,ccd))

    pool = Pool(processes=16)
    result = pool.map(onechip, targets)
    for ccd in  result:
	print ccd.visit, ccd.ccd, ccd.ret
