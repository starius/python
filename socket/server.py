import socket, sys, time                                    

host = ''                                     
port = int(sys.argv[1])
                                       
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
     
s.bind((host,port))

s.listen(1)

client,addr = s.accept()

while True:

    client.send("trying execute")
    
    data = client.recv(1024)
    if (data=="exit"):
        sys.exit(0)
    if (data=="sleep"):
        time.sleep(4)
        
    print "client:", data
    
s.close()

print "[+] disconnected"

