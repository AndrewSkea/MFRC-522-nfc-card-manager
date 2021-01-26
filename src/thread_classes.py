
import threading
import time


class ReadThread(threading.Thread):
    def __init__(self, reader):
        self.status = "Place RFID card on reader until confirmation here"
        self.cid = None
        self.text = None
        self.init_time = time.time()
        self.reader = reader
        super().__init__()

    def run(self):
        print("Starting Read")
        t = time.time() - self.init_time
        while self.cid is None and t < 30:
            t = time.time() - self.init_time
            self.cid, self.text = self.reader.read_no_block()
            self.status = "Place RFID card on reader until confirmation here. (timeout in {}s)".format(int(30-t))
            time.sleep(0.1)
        self.status = "complete"


class WriteThread(threading.Thread):
    def __init__(self, reader, write_text):
        self.status = "Place RFID card on reader until confirmation here"
        self.cid = None
        self.text = None
        self.write_text = write_text
        self.init_time = time.time()
        self.reader = reader
        super().__init__()

    def run(self):
        print("Trying to write: " + self.write_text)
        t = time.time() - self.init_time
        while self.cid is None and t < 30:
            t = time.time() - self.init_time
            self.cid, self.text = self.reader.write_no_block(self.write_text)
            self.status = "Place RFID card on reader until confirmation here. (timeout in {}s)".format(int(30-t))
            time.sleep(0.1)
        self.status = "complete"