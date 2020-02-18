import sys

def dec_to_bin(ip_dec):
    ip_bin = ""
    for x in ip_dec.split("."):
        oktet = ""
        check = bin(int(x))[2:]
        if len(check) < 8:
            for h in range(0,8-len(check)):
                oktet += "0"
        oktet += bin(int(x))[2:]
        ip_bin += oktet+"."
        
    ip_bin = ip_bin[:-1] #w celu usunięcia ostatniej kropki
    return ip_bin

def bin_to_dec(ip_bin):
    ip_dec = ""
    for x in ip_bin.split("."):
        ip_dec += str(int(x,2))+"."
    ip_dec = ip_dec[:-1] #w celu usunięcia ostatniej kropki
    return ip_dec

def network_address_bin(ip_bin,mask_bin):
    ip = ip_bin.split(".")
    mask = mask_bin.split(".")
    network_address = ""
    for x in range(0,4):
        for y in range(0,8):
            if mask[x][y] == "1":
                network_address += ip[x][y]
            else:
                network_address += "0"
        network_address += "."
    network_address = network_address[:-1]
    return network_address

def broadcast_bin(ip_bin,mask_bin):
    ip = ip_bin.split(".")
    mask = mask_bin.split(".")
    broadcast_address = ""
    for x in range(0,4):
        for y in range(0,8):
            if mask[x][y] == "1":
                broadcast_address += ip[x][y]
            else:
                broadcast_address += "1"
        broadcast_address += "."
    broadcast_address = broadcast_address[:-1]
    return broadcast_address
    
        
print("Przykład: 192.168.0.1 24\n")
adres = input("Wprowadź adres IP oraz liczbę bitów maski oddzielone spacją: ")

# Sprawdzenie czy wprowadzony adres IP oraz ilość bitów maski są poprawne

ip_dec = adres.split()[0]

try:
    adres.split()[0]
    adres.split()[1]
    ip_dec.split(".")[0]
    ip_dec.split(".")[1]
    ip_dec.split(".")[2]
    ip_dec.split(".")[3]
except:
    input("Wprowadzono nieprawidłowe dane. Wciśnij ENTER aby wyjść z programu")
    sys.exit()    
        

if int(adres.split()[1]) > 32 or int(adres.split()[1]) < 0:
    print("Liczba bitów maski jest nieprawidłowa. Musi być zawarta w przedziale 0 - 32")
    input("Wciśnij ENTER aby zamknąć program")
    sys.exit()

if int(ip_dec.split(".")[0]) > 255 or int(ip_dec.split(".")[0]) < 0:
    print("Adres IP jest nieprawidłowy. Każdy z oktetów musi być w zakresie 0 - 255")
    input('Wciśnij ENTER aby zamknąć program')
    sys.exit()
    
if int(ip_dec.split(".")[1]) > 255 or int(ip_dec.split(".")[1]) < 0:
    print("Adres IP jest nieprawidłowy. Każdy z oktetów musi być w zakresie 0 - 255")
    input('Wciśnij ENTER aby zamknąć program')
    sys.exit()
    
if int(ip_dec.split(".")[2]) > 255 or int(ip_dec.split(".")[2]) < 0:
    print("Adres IP jest nieprawidłowy. Każdy z oktetów musi być w zakresie 0 - 255")
    input('Wciśnij ENTER aby zamknąć program')
    sys.exit()
    
if int(ip_dec.split(".")[3]) > 255 or int(ip_dec.split(".")[3]) < 0:
    print("Adres IP jest nieprawidłowy. Każdy z oktetów musi być w zakresie 0 - 255")
    input('Wciśnij ENTER aby zamknąć program')
    sys.exit()


ip_bin = dec_to_bin(ip_dec)

mask_bity = int(adres.split()[1])

#maska_bin = ("1" * mask_bity)+("0" * (32 - mask_bity))
maska_bin = ""
for i in range(1,33):
    if i <= mask_bity:
        maska_bin += "1"
    else:
        maska_bin += "0"

    if i%8==0:
        maska_bin += "."
maska_bin = maska_bin[:-1] #w celu usunięcia ostatniej kropki


maska_dec = bin_to_dec(maska_bin)

network_address_bin = network_address_bin(ip_bin,maska_bin)
network_address_dec = bin_to_dec(network_address_bin)

broadcast_address_bin = broadcast_bin(ip_bin,maska_bin)
broadcast_address_dec = bin_to_dec(broadcast_address_bin)

pierwszy_adres_hosta_bin = network_address_bin[:-1] + "1"
pierwszy_adres_hosta_dec = bin_to_dec(pierwszy_adres_hosta_bin)

ostatni_adres_hosta_bin = broadcast_address_bin[:-1] + "0"
ostatni_adres_hosta_dec = bin_to_dec(ostatni_adres_hosta_bin)

print("                        \t dziesiętnie: \t\t binarnie:")
print("Adres IP:               \t {}           \t\t {}".format(ip_dec,ip_bin))
print("Maska:                  \t {}           \t\t {}".format(maska_dec,maska_bin))
print("Adres sieci:            \t {}           \t\t {}".format(network_address_dec,network_address_bin))
print("Adres rozgłoszeniowy:   \t {}           \t {}".format(broadcast_address_dec,broadcast_address_bin))
print("Adres pierwszego hosta: \t {}           \t\t {}".format(pierwszy_adres_hosta_dec,pierwszy_adres_hosta_bin))
print("Adres ostatniego hosta: \t {}           \t {}".format(ostatni_adres_hosta_dec,ostatni_adres_hosta_bin))

input('Wciśnij ENTER aby zamknąć program')
