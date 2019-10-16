from hackerman import portscanner,whoup

# EX : 192.168.1.1
ip=raw_input('IP : ')
# EX : 80
port1=raw_input('PORT : ')
# EX : 3306
port2=raw_input('PORT : ')
# port scanner
# IP , START FROM port1 , STOP IN port2
portscanner(ip,port1,port2)

# Lets Show Who up in network
# EX : 192.168.1.1/24
ip=raw_input('IP : ')
whoup(ip)
