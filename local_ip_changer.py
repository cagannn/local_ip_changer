import os
import pyfiglet 
import random 
import time
f = pyfiglet.figlet_format("Local ip changer", font="slant")
print(f)


second=int(input("[+]How many second do you want to between two ip for change:"))
interface=input("[+]What type of interface do you use (eth0, wlan0):")
	
try:
	while True:
		random_ip='192.168.'+str(random.randint(0,256))+"."+str(random.randint(0,256))
		os.system('ifconfig '+interface+" "+random_ip)
		print('[+]Your ip address changed as '+random_ip)
		time.sleep(second)
except KeyboardInterrupt:
	os.system("service networking restart")
	os.system("service NetworkManager restart")
	print("\n[+]networking and NetworkManager services has been restarted")
