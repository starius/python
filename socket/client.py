import socket, sys, time     


host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       

s.connect((host,port))

print 'connected'

let = "open"

while let != "exit":

    data = s.recv(1024)
    print "server:", data
    let = raw_input("client: ")
    s.send(let)
    
s.close()
print "[+] disconnected"