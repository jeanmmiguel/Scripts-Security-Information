from socket import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket IPv4, conexão tcp/ip

host = " " # host e porta para rodar a conexão
porta = 8259

msg = "jean cliente" #mensagem p/ cliente qdo se conectar na maquina

s.blid((host,porta)) # ativar escuta em host e portas acima
s.listen(1) #maximo de conexões recebidas ao mesmo tempo

while true: #laço p/ deixar o servidor sempre em escuta
c,e = s.accept()        #conexão e endereço, aceitando coneão

print("conectado com",e) #mostra ip do cliente conectado
c.send(msg.encode('ascii'))  #enviar a mensagem que passa em bytes pela rede, faz em code para ASCII

c.close() #fecha conexão
