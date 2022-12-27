# получить ответ от  ресурса с такими данными 
#   host = 'time.nist.gov'
#   port = 13
#  послать нужно пустую строку в запросе
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = 'time.nist.gov'
    port = 13

    s.connect((host, port))

    m_str = "HEAD / HTTP/1.1\r\nHost: {}\nAccept: text/html\r\n\r\n".format(host)
    msg = bytearray(m_str.encode())

    s.sendall(msg)
    answ = s.recv(1024)
    print(answ.decode('utf8'))