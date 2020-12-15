import queue
from multiprocessing import Pool
import time
from MessAround import *
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, q):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.q = q
#    def run(self):
#       print ("Starting " + self.name)
#       process_data(self.name, self.q)
#       print ("Exiting " + self.name)
#
# def process_data(threadName, q):
#    while not exitFlag:
#       queueLock.acquire()
#       if not workQueue.empty():
#          data = q.get()
#          queueLock.release()
#          print ("%s processing %s" % (threadName, data))
#       else:
#          queueLock.release()
#          time.sleep(1)
#
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
#
# if __name__ == '__main__':
#     # Create new threads
#     for tName in threadList:
#        thread = myThread(threadID, tName, workQueue, t)
#        thread.start()
#        threads.append(thread)
#        threadID += 1
#
#     # Fill the queue
#     queueLock.acquire()
#     for word in nameList:
#        workQueue.put(word)
#     queueLock.release()
#
#     # Wait for queue to empty
#     while not workQueue.empty():
#        pass
#
#     # Notify threads it's time to exit
#     exitFlag = 1
#
#     # Wait for all threads to complete
#     for t in threads:
#        t.join()
#     print ("Exiting Main Thread")
#
#
if __name__ == '__main__':
    # margin_of_error = []
    # for x in range(0, 100):
    boogaloo = [('J', 'C'), (2, 'C')]
    boogaloo2 = [(4, 'S'), (6, 'H'), (3, 'C'), ('A', 'C'), (9, 'C')]
    pool = Pool(processes=4)
    start = time.time()
    th1 = pool.apply_async(monte_carlo_post_flop, [boogaloo, boogaloo2, 4])
    th2 = pool.apply_async(monte_carlo_post_flop, [boogaloo, boogaloo2, 4])
    th3 = pool.apply_async(monte_carlo_post_flop, [boogaloo, boogaloo2, 4])
    th4 = pool.apply_async(monte_carlo_post_flop, [boogaloo, boogaloo2, 4])
    th5 = pool.apply_async(monte_carlo_post_flop, [boogaloo, boogaloo2, 4])
    th6 = pool.apply_async(monte_carlo_post_flop, [boogaloo, boogaloo2, 4])
    th7 = pool.apply_async(monte_carlo_post_flop, [boogaloo, boogaloo2, 4])
    th8 = pool.apply_async(monte_carlo_post_flop, [boogaloo, boogaloo2, 4])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
    target = 94.82
    p1 = th1.get() - target
    p2 = ((th1.get() + th2.get())/2) - target
    p3 = ((th1.get() + th2.get() + th3.get())/3) - target
    p4 = ((th1.get() + th2.get() + th3.get() + th4.get())/4) - target
    p5 = ((th1.get() + th2.get() + th3.get() + th4.get() + th5.get())/5) - target
    p6 = ((th1.get() + th2.get() + th3.get() + th4.get() + th5.get() + th6.get())/6) - target
    p7 = ((th1.get() + th2.get() + th3.get() + th4.get() + th5.get() + th6.get() + th7.get())/7) - target
    p8 = ((th1.get() + th2.get() + th3.get() + th4.get() + th5.get() + th6.get() + th7.get() + th8.get())/8) - target
    print('p1:', p1)
    print('p2:', p2)
    print('p3:', p3)
    print('p4:', p4)
    print('p5:', p5)
    print('p6:', p6)
    print('p7:', p7)
    print('p8:', p8)
    #     margin_of_error.append(p8)
    # margin_of_error = np.array(margin_of_error)
    # margin_of_error = np.mean(margin_of_error)
    # print(margin_of_error)