import digits
from datetime import datetime
from time import sleep
from os import system

def main():
        try:
            while True:
                currentTime = datetime.now()
                h = currentTime.hour
                if h<10: hour = '0'+str(h)
                else: hour = str(h)
                m = currentTime.minute
                if m<10: minutes = '0'+str(m)
                else: minutes = str(m)
                s = currentTime.second
                if s<10: seconds = '0'+str(s)
                else: seconds = str(s)
                to_display = hour + ':' + minutes + ':' + seconds
                # to_display = str(currentTime.hour) + str(currentTime.minute) + str(currentTime.second)
                digits.printDigits(to_display)
                sleep(1)
                system('cls')
        except:
            print('Dziękujemy za skorzystanie z naszego zegara')

main()