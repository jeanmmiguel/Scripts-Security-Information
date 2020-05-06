import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket IPv4, conexão tcp/ip

host = " " # host e porta para rodar a conexão
porta = 8259

s.connect((host,porta))
dados = s.recv(1024)  #receber dados do servidor
pritn(dados.decode('ascii'))
