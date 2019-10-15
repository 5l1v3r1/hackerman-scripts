from hackerman import xss,slow_print,ssti,sqli,headers
import sys,os
def logo():
        os.system('''figlet -f slant WEBSCANNER ''')

target='http://leettime.net/xsslab1/chalg1.php?name=5*&submit=Search'
logo()
# slow_print ('Your Word',Fast Number of MOde)
# EX:V
#    V
slow_print('[+] This Script Example for hackerman module \nNow we will start web scanner on http://leettime.net/xsslab1/chalg1.php?name=5*&submit=Search .. Good Luck :) ',1)
# Start The Scanner
# Xss Reflacted
xss(target)
# SQL INJECTION
sqli(target)
# TEMPLATE INJECTION
ssti(target)
# Get All HTTP HEADERS
print('\n\n')
headers(target)
