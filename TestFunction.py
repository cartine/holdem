from multiprocessing import Pool
import time


def runA():
    time.sleep(.1)
    return 'A'


def runB():
    return 'B'


def runC():
    time.sleep(.2)
    return 'C'


def runD():
    return 'D'


def getResults(result):
    global results
    results.append(result)


if __name__ == '__main__':
    time1 = time.time()
    results = []
    pool = Pool(processes=4)
    for i in range(10):
        print('started p1')
        p1 = pool.apply_async(runA, callback=getResults)
        print('finished p1')
        print('starting p2')
        p2 = pool.apply_async(runB, callback=getResults)
        print('finished p2')
        print('starting p3')
        p3 = pool.apply_async(runC, callback=getResults)
        print('finished p3')
        print('starting p4')
        p4 = pool.apply_async(runD, callback=getResults)
        print('finished p4')
        p1.get()
        p2.get()
        p3.get()
        p4.get()
        # pool.close()
        # pool.join()
    # processes = [p1, p2, p3, p4]

    time2 = time.time() - time1
    print(time2)
    print(results)