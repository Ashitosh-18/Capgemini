import threading
import time
def even():
    for i in range(10+1):
        if(i%2==0):
            print(i)
            i+=1
            time.sleep(0.1)
    print("even task is completed")
    
def odd():
    for i in range(10+1):
        if(i%2!=0):
            print(i)
            i+=1
            time.sleep(1)
    print("odd task is complted")
    
thread_1=threading.Thread(target=even)
thread_2=threading.Thread(target=odd)
thread_1.start()
thread_1.join()
thread_2.start()
thread_2.join()
print("all threads are joined")