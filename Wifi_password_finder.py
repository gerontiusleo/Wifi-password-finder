#import subprocess module
import subprocess

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

profiles = [iplit(":")[1][1:-1] for i in data if "All user profile" in i]


for i in profiles:
	results = subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('utf-8').split('\n')
	
	#storinf the passwords after coverting them into  list
	results = [b.split(":")[1][1:-1] for b in results if "Key content" in b]
	
	#try and except method
	try:
		print ("{:<30}| {:<}",format(i, results[0]))
		
	except IndexError:
		print("	{:<30}| {:<}",format(i, ""))
