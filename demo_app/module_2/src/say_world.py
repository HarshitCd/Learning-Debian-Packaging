import time

def main():
    while True:
        time.sleep(2)
        print("World")
              
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting say_world.py")