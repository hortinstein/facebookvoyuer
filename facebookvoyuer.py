import pcapy
import sys
from string import whitespace
from impacket.ImpactDecoder import *
 
# list all the network devices
pcapy.findalldevs()
 
max_bytes = 1024
promiscuous = False
read_timeout = 100 # in milliseconds
pc = pcapy.open_live("eth0", max_bytes, promiscuous, read_timeout)
 
pc.setfilter('tcp')
 
# callback for received packets
def recv_pkts(hdr, data):
	
	linepot = data.split('\"')
	for i in range(len(linepot)):
		if i >= 6:
			if linepot[i] == "from" and linepot[i-1] == "},":
				fromid = linepot[i+1][1:-1]
				toid = linepot[i+3][1:-1]
				fromname = linepot[i+6]
				toname = linepot[i+10]
				msg = linepot[i-10]
				msgid = linepot[i-1]                    
				print fromname,"ID# (",fromid,") to ",toname,"ID# (",toid,")\	\"",msg,"\"\n"                              
		
  
packet_limit = -1 # infinite
pc.loop(packet_limit, recv_pkts) # capture packets
