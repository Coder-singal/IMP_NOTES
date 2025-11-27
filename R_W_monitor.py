import threading
import time

class RWMonitor:
    def __init__(self):
        self.read_count = 0
        self.lock = threading.Lock()
        self.ok_to_write = threading.Condition(self.lock)
    def start_read(self):
        with self.lock:
            self.read_count += 1
    def end_read(self):
        with self.lock:
            self.read_count -= 1
            if self.read_count == 0:
                self.ok_to_write.notify()
    def start_write(self):
        with self.lock:
            while self.read_count > 0:
                self.ok_to_write.wait()
    def end_write(self):
        with self.lock:
            self.ok_to_write.notify()
monitor = RWMonitor()
def reader(id):
    monitor.start_read()
    print(f"Reader {id} reading")
    time.sleep(1)
    monitor.end_read()
def writer(id):
    monitor.start_write()
    print(f"Writer {id} writing")
    time.sleep(1)
    monitor.end_write()
threads = [
    threading.Thread(target=reader, args=(1,)),
    threading.Thread(target=writer, args=(1,)),
    threading.Thread(target=reader, args=(2,)),
    threading.Thread(target=writer, args=(2,)),
    threading.Thread(target=reader, args=(3,))
]
for t in threads: t.start()
for t in threads: t.join()
