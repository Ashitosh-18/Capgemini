import threading
import time

def daemon_task():
    while True:
        print("Deamon thread running...")
        time.sleep(1)
        
daemon_thread=threading.Thread(target=daemon_task,daemon=True)
daemon_thread.start()

time.sleep(6)
print("Main thread exiting")