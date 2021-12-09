import random
import time
while True:
    rnd = random.randrange(1,10000000000001,1)
    print(str(rnd) + str(rnd * 2)  + str(rnd * 3)  + str(rnd * 3)  + str(rnd* 3)  + str(rnd* 4)  + str(rnd)  + str(rnd)  + str(rnd) )
    time.sleep(random.random() / 10)
    if(rnd == 1):
        break


