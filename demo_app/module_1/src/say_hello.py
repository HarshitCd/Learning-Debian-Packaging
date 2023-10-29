import time
from module_1.src.utils.utils_hello import utils_hello

def main():
    while True:
        print("Hello")
        time.sleep(2)
        utils_hello()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting say_hello.py")