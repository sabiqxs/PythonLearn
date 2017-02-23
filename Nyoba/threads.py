import threading

class SabiqMessengger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
x = SabiqMessengger(name="sending messengger")
y = SabiqMessengger(name="Receive messengger")
x.start()
y.start()