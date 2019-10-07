ui = input("Enter an ip address: ")
ip = ui.split('.')
if len(ip)!=4 :
    print("Wrongly formed ip address")
    exit(-9)

ip[-1] = str(int(ip[-1]) + 1)
print("Next IP: " , ".".join(ip))
#print(b)
    