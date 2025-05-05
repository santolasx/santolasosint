import requests
import whois
import socket
import dns.resolver

# IP Konum Sorgulama
def ip_konum_bul(ip_adresi):
    url = f"http://ipinfo.io/{ip_adresi}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"IP: {data.get('ip')}")
        print(f"Ülke: {data.get('country')}")
        print(f"Şehir: {data.get('city')}")
        print(f"Konum: {data.get('loc')}")
    else:
        print("Hata: IP bilgisi alınamadı.")

# Whois Bilgisi
def whois_bilgi(domain):
    w = whois.whois(domain)
    print(f"Domain: {domain}")
    print(f"Kayıt Sahibi: {w.get('org')}")
    print(f"Kayıt Tarihi: {w.get('creation_date')}")
    print(f"Son Güncelleme: {w.get('updated_date')}")

# DNS Bilgisi
def dns_bilgi(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"IP Adresi: {rdata.to_text()}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print("DNS Bilgisi Bulunamadı.")

# Ana Fonksiyon
def osint_araci():
    print("OSINT Aracına Hoşgeldiniz! SANTØLAS   instagram: unlywq")
    
    # Kullanıcıdan domain veya IP bilgisi alalım
    secim = input("Bir seçenek girin (1: IP Konumu, 2: Whois, 3: DNS): ")
    
    if secim == "1":
        ip_adresi = input("IP adresi girin: ")
        ip_konum_bul(ip_adresi)
    elif secim == "2":
        domain = input("Domain girin: ")
        whois_bilgi(domain)
    elif secim == "3":
        domain = input("DNS sorgulamak için domain girin: ")
        dns_bilgi(domain)
    else:
        print("Geçersiz seçenek.")

# Programı başlat
osint_araci()
