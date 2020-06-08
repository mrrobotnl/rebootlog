import time
import os
import datetime


def controleerofikerben():
    check = os.path.exists('rebootlog.txt')
    if check == True:
        print("Het document Rebootlog.txt bestaat")
    else:
        print("het bestand Rebootlog bestaat niet en wordt aangemaakt!")
def logbook():
    current = (str(datetime.datetime.now()))
    rebootlog = open("rebootlog.txt", "a")
    rebootlog.write("\n Herstart succesvol gedaan op:")
    rebootlog.write(current)
def reboot():
    for i in range(1,10):
        print("herstarten op:", i)
        time.sleep(1)
    os.system("sudo reboot")

controleerofikerben()
logbook()
reboot()