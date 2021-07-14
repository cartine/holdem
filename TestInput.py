from multiprocessing import Pool, Manager
import time
import random


def run_player2(q, thread):
    print('><><', thread)
    queue_size = q.qsize()
    if queue_size < 1:
        return
    print(2)
    if thread == 1:
        while q.qsize() == queue_size:
            print('M')
            time.sleep(.5)
            num = random.randint(0, 100)
            if num > 90:
                q.put('player2')
                print('player2')
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            time.sleep(.5)
            num = random.randint(0, 100)
            if num > 90:
                q.put('player2')
                print('player2')
                break


def run_player3(q, thread):
    queue_size = q.qsize()
    if queue_size < 1:
        return
    print(3)
    if thread == 1:
        while q.qsize() == queue_size:
            num = random.randint(0, 100)
            if num > 90:
                q.put('player3')
                print('player3')
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            time.sleep(.5)
            num = random.randint(0, 100)
            print('K')
            if num > 50:
                q.put('player3')
                print('player3')
                break


def run_player4(q, thread):
    queue_size = q.qsize()
    if queue_size < 1:
        return
    print(4)
    if thread == 1:
        while q.qsize() == queue_size:
            num = random.randint(0, 100)
            if num > 90:
                print('Thread 1', num)
                q.put('player4')
                print('player4')
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            time.sleep(.5)
            num = random.randint(0, 100)
            if num > 90:
                q.put('player4')
                print('player4')
                break


def run_player5(q, thread):
    queue_size = q.qsize()
    if queue_size < 1:
        return
    print(5)
    if thread == 1:
        while q.qsize() == queue_size:
            num = random.randint(0, 100)
            if num > 90:
                q.put('player5')
                print('player5')
                break
    if thread == 2:
        while q.qsize() - queue_size < 2 and q.qsize() > 0:
            time.sleep(.5)
            num = random.randint(0, 100)
            if num > 99:
                q.put('player5')
                print('player5')
                break


def find_self(q):
    print('New')
    num = random.randint(0, 100)
    while num != 90:
        num = random.randint(0, 100)
        time.sleep(.2)
    print('<><<>>')
    time.sleep(3)
    q.put('Done')
    q.put('Done')
    for m in range(0, q.qsize()):
        print(q.get())
    print('Changed', q.qsize())


if __name__ == '__main__':
    time1 = time.time()
    m = Manager()
    q = m.Queue()
    q.put('New')
    pool = Pool(processes=1)
    functs = [run_player2, run_player3, run_player4]
    p1 = pool.apply_async(find_self, args=(q,))
    for i in range(0, len(functs)):
        if i % 2 == 1:
            continue
        pool2 = Pool(processes=2)
        try:
            p2 = pool2.apply_async(functs[i].__call__, args=(q, 1))
            p3 = pool2.apply_async(functs[i+1].__call__, args=(q, 2))
        except:
            pass
        pool2.close()
        pool2.join()
    print('Finito')
    pool.close()
    pool.join()
    print('TIME:', time.time() - time1)

# IDEA - HAVE THE FOLLOW-UP FUNCTION BE A PARAMETER OF THE ORIGINAL FUNCTION / MAYBE USE KWARGS