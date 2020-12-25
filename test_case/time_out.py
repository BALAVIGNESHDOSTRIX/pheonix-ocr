import time 

def Test():
    CallMe("BALA")
    return 1

def CallMe(param):
    time.sleep(1)
    print(param)

if __name__ == "__main__":
    Test()