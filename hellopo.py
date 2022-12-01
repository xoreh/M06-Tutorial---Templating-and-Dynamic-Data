import random, time, datetime, os



def process():
    time1 = random.uniform(0,1)
    print("Wait a random number: "+str(time1))
    time.sleep(time1)
    print('CURRENT TIME: ', datetime.datetime.now(),'\n')
