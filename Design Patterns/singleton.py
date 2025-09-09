# class Singleton:
#     _instance = None # static variable hold the singleton instance

#     def __new__(cls): # __new__ this method runs before __init__ (used when we have to do something before creating an object)
#         if cls._instance is None:
#             print('Creating singleton onject....')
#             cls._instance = super().__new__(cls)
#             return cls._instance
#         else:
#             print('Using existing singleton object')
#             return cls._instance
        

# obj1 = Singleton()
# obj2 = Singleton()
# obj3 = Singleton()

# print(id(obj1))
# print(id(obj2))
# print(id(obj3))

# print(obj1 is obj2)
# print(obj2 is obj3)
# print(obj3 is obj1)

import threading
import time

class BrokenSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double check locking
                if cls._instance is None:
                    time.sleep(0.1)
                    print(f"[{threading.current_thread().name}] - Creating new object....")
                    cls._instance = super(BrokenSingleton, cls).__new__(cls)
                return cls._instance

def access_brokenSingleton():
    instance = BrokenSingleton()
    print(f"[{threading.current_thread().name}] - Instance ID : {id(instance)}")

threads = []
for i in range(10):
    t = threading.Thread(target=access_brokenSingleton, name=f"Thread-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()