from time import sleep
class Trafficlight:
    __color = ['red','yellow', 'green']
    def running (self):
        i = 0

        while i != 3:
            print (Trafficlight.__color[i])
            if i ==0:
                sleep(7)
            elif i ==1:
                sleep (2)
            elif i == 2:
                sleep (5)
            i +=1
t_r = Trafficlight()
t_r.running()

