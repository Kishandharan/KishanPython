import time

def connect():
    print("Connecting to internet...")
    time.sleep(2)
    print("Connected")
    print(__name__)

if __name__ == "__main__":
    connect()
