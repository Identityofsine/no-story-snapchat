import os

def load_text():
	ips = []
	with open('detected.ip.txt', 'r') as f:
		for line in f:
			#strip any '#' from the line
			if not line.startswith('#'):
				# find index of #
				index = line.find('#')
				# if found, strip it
				if index != -1:
					line = line[:index]
				#strip any whitespace
				line = line.strip()
				if line == '':
					continue
				#append to list
				ips.append(line)
				
	return ips

def output_wireshark_predicate(ips):
	#generate wireshark predicate
	wireshark_predicate = ''
	for ip in ips:
		wireshark_predicate += 'ip.src != %s && ip.dst != %s && ' % (ip, ip)
	return '(tcp && ip.src == 10.8.0.2) && (%s)' % (wireshark_predicate[:-4])

def generate_iptables(ips):
	#generate iptables
	iptables = ''
	for ip in ips:
		iptables += 'iptables -A FORWARD -s %s -j DROP\n' % ip
		iptables += 'iptables -A FORWARD -s 0/0 -d %s -j DROP\n' % ip
	return iptables

def isSudo():
	return os.geteuid() == 0

def main():
	if not isSudo():
		print('You need to run this script as root')
		return
	os.system('iptables -F FORWARD')
	ips = load_text()
	iptables = generate_iptables(ips)
	for line in iptables.split('\n'):
		os.system(line)

print('Running iptables.py')
print('This script will block all traffic from the IPs listed in detected.ip.txt')
print('Make sure you have the correct permissions to run this script')
print('-'.center(50, '-'))
print('')
print('DEBUG: Running load_text()')
print(load_text())
print('')
print('DEBUG: Running output_wireshark_predicate() [for testing purposes]')
print(output_wireshark_predicate(load_text()))
main()


