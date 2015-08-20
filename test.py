from multiprocessing import Pool
ccds = range(9)+range(10,104)

def onechip(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=4)
    result = pool.map(onechip, ccds)
    print result
