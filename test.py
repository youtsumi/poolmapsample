from multiprocessing import Pool
ccds = range(9)+range(10,104)

class Ccd:
    def __init__(self,x):
	self.x=x
    def process(self):
	self.ret=self.x**2

def onechip(x):
    ccd=Ccd(x)
    ccd.process()
    return ccd

if __name__ == '__main__':
    pool = Pool(processes=16)
    result = pool.map(onechip, ccds)
    for ccd in  result:
	print ccd.x, ccd.ret
