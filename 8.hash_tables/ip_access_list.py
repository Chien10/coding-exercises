"""
	Analyse the access log and quickly answer
	queries: did anybody access the service from
	this IP during the last hour? How many
	times? How many IPs were used to access
	the service during the last hour?
"""
import datetime as dt
from datetime import datetime, timedelta
from typing import List, Tuple
from collections import namedtuple

log_line = namedtuple('log_line', ('time', 'ip'))

def naive_ip2decimal(ip_address: str):
	"""
		IPv4 to decimal
	"""
	ip = ip_address.split('.')
	if len(ip) != 4:
		return None

	result = ''
	for i in ip:
		bin_ip = bin(int(i))[2:]
		bin_ip = '0' * (8 - len(bin_ip)) + bin_ip
		result += bin_ip

	return int(result, 2)

def ipv4_to_dec(ip_address: str):
	ip_address = ip_address.split('.')
	return int(ip_address[0]) * 2**24 + int(ip_address[1]) * 2**16 + \
			int(ip_address[2]) * 2**8 + int(ip_address[3])

log: List[Tuple[datetime.time, str]] = None

"""
	Requires 2**32 memory. For IPv6, the memory could be 2**128
"""
class DirectAddressingIpHashTable:
	def __init__(self, log: List[Tuple]):
		self.i = 0 #  first unprocessed log line
		self.j = 0 # first line in current 1h window
		self.log = log
		self.A = [0] * 2**32

	def ipv4_to_dec(self, ip_address: str):
		ip_address = ip_address.split('.')
		return int(ip_address[0]) * 2**24 + int(ip_address[1]) * 2**16 + \
				int(ip_address[2]) * 2**8 + int(ip_address[3])

	def accessed_last_hour(ip_address: str):
		"""
			If the `ip_address` is accessed the last hour
		"""
		return self.A[self.ipv4_to_dec(ip_address)] > 0

	def update_access_list(self):
		now = datetime.now()
		while self.log[self.i] <= now.time():
			A[self.ipv4_to_dec(self.log[i].ip)] += 1
			self.i += 1

		while self.log[self.j].time <= now - timedelta(seconds=3600):
			A[self.ipv4_to_dec(self.log[j].ip)] -= 1
			j += 1

