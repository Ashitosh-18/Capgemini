import threading #1 
import time      #2

print("Main thread started")  #3

def single_task():
    print("Sub task started") #5
    time.sleep(4)             #6
    print("Sub task ended")   #7
    
thread=threading.Thread(target=single_task) #4
thread.start()                              #5
thread.join()                               #8

# If we use ".join()" main thread will wait for sub thread to complete its execution 
# after the execution of sub thread it will join the main thread and main thread will again start

# If we don't use ".join()" the main thread will complete its execution without waiting
# After the sub thread execution is done, it will join the main thread in between


print("Main thread execution completed")    #9