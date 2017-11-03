#!/home/projects/django/bin/python
import sys
import _thread
import time
import socket

global results
results = ""
def check_port(host,port, result = 1):
	print("[Checking Host: " + host + ", port: " + port)
	try:
		# Creating a socket object named 'sock'
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Setting socket timeout so that the socket does not wait forever to complete  a connection
		sock.settimeout(0.5)
		# Connect to the socket
		# if the connection was successful, that means the port
		# is open, and the output 'r' will be zero
		r = sock.connect_ex((host, int(port)))
		if r == 0:
			result = 'OPEN'
		else:
			result = 'CLOSED'
		sock.close() # closing the socket
	except Exception as e:
		print("ERROR")
		print(e)
		pass
	#print("[+] Host: " + host + ", port: " + port + " " + str(result))
	global results 
	results = results + "[+] Host: " + host + ", port: " + port + " " + str(result) + "\n"
	#results[host][port]=result
	#print(results)
	#return result

def portscan(hosts, ports):
	global results
	results = ""
	num_hosts=len(hosts)
	num_ports=len(ports)
	#print(num_hosts, num_ports)
	#global results
	#results = [[0 for x in range(num_hosts)] for y in range(num_ports)]
	print ("Scan in progress...")
	for host in hosts:
		#print(host)
		for port in ports:
			#print(port)
			"""if qin.full()==False:
				qin.put(host, port)	
			else:
				print("\n[ERROR]	Queue `qin` is too small!")"""
			_thread.start_new_thread( check_port, (host,port,))
			time.sleep(0.5)
	return results

def print_test():
	print("This is a test")


#Main Program:
#args_str=sys.argv
#hosts=args_str[1].split(",")
#ports=args_str[2].split(",")

#portscan(hosts,ports)
