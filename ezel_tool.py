
import socket
import time
import os

def banner():
    os.system('clear')
    print("="*40)
    print("     EZEL TOOL - PORT TARAMA ARACI")
    print("="*40)
    time.sleep(0.5)

def tarama(ip, baslangic, bitis):
    print(f"\nHedef IP: {ip}")
    print(f"Portlar: {baslangic}-{bitis}")
    print("-" * 30)
    for port in range(baslangic, bitis + 1):
        try:
            soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soket.settimeout(0.5)
            sonuc = soket.connect_ex((ip, port))
            if sonuc == 0:
                print(f"[+] Port {port} AÇIK")
            soket.close()
        except:
            pass

banner()
hedef_ip = input("Hedef IP adresini girin: ")
tarama(hedef_ip, 1, 100)
