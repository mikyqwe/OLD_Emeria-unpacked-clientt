import app

app.ServerName = None

STATE_NONE = '...'
		
STATE_DICT = {
	0 : '....',
	1 : 'NORM',
	2 : 'BUSY',
	3 : 'FULL'	}

SERVER1_CHANNEL_DICT = {
	1:{'key':11,'name':'Channel1','ip':'XXXXXXXXX','tcp_port':13101,'udp_port':13101,'state':STATE_NONE,},
	2:{'key':12,'name':'Channel2','ip':'XXXXXXXXX','tcp_port':14070,'udp_port':14070,'state':STATE_NONE,},
	3:{'key':13,'name':'Channel3','ip':'XXXXXXXXX','tcp_port':15070,'udp_port':15070,'state':STATE_NONE,},
	4:{'key':14,'name':'Channel4','ip':'XXXXXXXXX','tcp_port':16070,'udp_port':16070,'state':STATE_NONE,},
	5:{'key':14,'name':'Channel5','ip':'XXXXXXXXX','tcp_port':17070,'udp_port':17070,'state':STATE_NONE,},
}

REGION_NAME_DICT = {
	0 : 'GERMANY',
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { 'ip':'XXXXXXXXX', 'port':11232, }, 
		
		}	
}

REGION_DICT = {
	0 : {
		1 : { 'name' : 'Elendosfiles', 'channel' : SERVER1_CHANNEL_DICT, },
		},
}

MARKADDR_DICT = {
	10 : { 'ip' : 'XXXXXXXXX', 'tcp_port' : 15000, 'mark' : '10.tga', 'symbol_path' : '10', },
	}

TESTADDR = { 'ip' : 'XXXXXXXXX', 'tcp_port' : 50000, 'udp_port' : 50000, }

#DONE
