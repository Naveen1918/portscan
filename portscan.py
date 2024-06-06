#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored

'''
#simple port scanner
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is for IPv4 & SOCK_STREAM says we r using tcp packets to perform connection
#socket.setdefaulttimeout(2)

host = input("enter the IPv4 address to scan: ")

#port = int(input("enter the port number: "))

#connect func for above host n port

def portscanner(port):
	if sock.connect_ex((host, port)):
		print(colored("[!!]Port %d is closed"%(port), "red"))
	else:
		print(colored("[+]Port %d is open"%(port),"green"))

for port in range(1,1000):
	portscanner(port)'''

#advanced port scanner
def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost,tgtPort))
		banner = sock.recv(1024)
		if banner:
			print(colored(str(tgtPort) + "/tcp "+(colored(str(banner),"blue"))+ " open","green"))
		else:
			print(colored("%d/tcp open"%tgtPort,"green"))

	except:
		print(colored("%d/tcp closed"%tgtPort, "red"))
	finally:
		sock.close()

def portScan(tgtHost, tgtPort):
	try:
		tgtIP = gethostbyname(tgtHost) #to IP from name
	except:
		print("cannot resolve: unknown Host %s"% tgtHost)
	try:
		tgtName = gethostbyaddr(tgtIP) # name from IP
		print("Scan result for: "+ tgtName[0])
	except:
		print("scan result for: "+ tgtIP)
	setdefaulttimeout(1)
	#below creating threads to run simultaneous scanning of ports
	for port in tgtPort:
		t=Thread(target=connScan, args=(tgtHost, int(port)))
		t.start()




def main():
	print(colored("||\\\    ||          ========  =======     //\\\     ||\\\    ||", attrs=['reverse', 'blink']))
	print(colored("|| \\\   ||          ||        ||         //  \\\    || \\\   ||", attrs=['reverse', 'blink']))
	print(colored("||  \\\  ||          ========  ||        //    \\\   ||  \\\  ||", attrs=['reverse', 'blink']))
	print(colored("||   \\\ ||                 || ||       //      \\\  ||   \\\ ||", attrs=['reverse', 'blink']))
	print(colored("||    \\\||          ========  ======= //        \\\ ||    \\\||", attrs=['reverse', 'blink']))
	parser = optparse.OptionParser('Usage of program: ' + '-H<target host> -p<target ports>')
	parser.add_option('-H', dest = 'tgtHost', type='string', help='Specify target host')
	parser.add_option('-p', dest = 'tgtPort', type='string', help='Specify target ports separated by comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPort = str(options.tgtPort).split(',') #to get multiple ports separated by comma
	if (tgtHost == None) | (tgtPort[0] == None):
		print(parser.usage)
		exit(0)
	portScan(tgtHost, tgtPort)

if __name__ == '__main__':
	main()