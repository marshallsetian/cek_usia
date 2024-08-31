from datetime import datetime, timedelta
from colorama import Fore, Style, init
import time,os,sys,requests
from urllib import request
import time


def format_waktu_indonesia():
    sekarang = datetime.now()

    # Nama bulan dalam bahasa Indonesia
    nama_bulan = {
        "January": "Januari", "February": "Februari", "March": "Maret",
        "April": "April", "May": "Mei", "June": "Juni",
        "July": "Juli", "August": "Agustus", "September": "September",
        "October": "Oktober", "November": "November", "December": "Desember"
    }
    
    

    # Mendapatkan bulan dalam bahasa Inggris
    bulan = sekarang.strftime("%B")

    # Terjemahkan ke bahasa Indonesia
    bulan_indonesia = nama_bulan[bulan]

    # Format tanggal: Hari Bulan Tahun
    tanggal = sekarang.strftime(f"%d {bulan_indonesia} %Y")
    # Format waktu: Jam:Menit:Detik
    waktu = sekarang.strftime("%H:%M:%S")
    
    return f"{tanggal} {waktu}"

# Contoh penggunaan
waktu_indonesia = format_waktu_indonesia()
#print("Waktu saat ini (Indonesia):", waktu_indonesia)


def format_waktu_indonesia():
    sekarang = datetime.now()
    # Format tanggal: Hari-Bulan-Tahun
    tanggal = sekarang.strftime("%d-%m-%Y")
    # Format waktu: Jam:Menit:Detik
    waktu = sekarang.strftime("%H:%M:%S")
    return f"{tanggal} {waktu}"

ip=requests.get('https://api.ipify.org').text

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

hijau="\033[0;92m "
putih="\033[0;97m"
abu="\033[0;90m"
kuning="\033[0;93m"
ungu="\033[0;95m"
merah="\033[0;91m"
biru="\033[0;96m"

# Inisialisasi colorama
def ketik_berjalan(teks, kecepatan=0.05):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(kecepatan)

init(autoreset=True)




def hitung_usia_lengkap(tanggal_lahir):
    today = datetime.today()
    
    usia_tahun = today.year - tanggal_lahir.year
    ulang_tahun = tanggal_lahir.replace(year=today.year)

    if today < ulang_tahun:
        usia_tahun -= 1

    if today >= ulang_tahun:
        usia_bulan = today.month - tanggal_lahir.month
        usia_hari = today.day - tanggal_lahir.day
    else:
        if today.month > tanggal_lahir.month:
            usia_bulan = today.month - tanggal_lahir.month - 1
        else:
            usia_bulan = 11 + (today.month - tanggal_lahir.month)
        usia_hari = (today - ulang_tahun + timedelta(days=1)).days

    if today >= ulang_tahun:
        ulang_tahun_berikutnya = ulang_tahun.replace(year=today.year + 1)
    else:
        ulang_tahun_berikutnya = ulang_tahun
    hari_sampai_ulang_tahun = (ulang_tahun_berikutnya - today).days

    return usia_tahun, usia_bulan, usia_hari, hari_sampai_ulang_tahun

def tampilkan_banner():
    
    print(f"""

{putih}[{B}•{putih}] {biru}Developer{hijau}: MarshallSetian
{putih}[{B}•{putih}] {ungu}Instagram {putih}: @marshall_setian
{W}[{B}•{W}] Ip Kamu {putih}  :{Y} {ip}
{W}[{B}•{W}] Waktu/Jam {putih}:{merah} {waktu_indonesia}""")
    banner ="""\n==============================
PENGHITUNG USIA TINGKAT LANJUT
==============================
    """
    print(Fore.CYAN + banner)
    time.sleep(1)

def main():
    tampilkan_banner()
    
    print(putih + "Silakan Input Data Kelahiran Anda\n")
    
    nama = input(f"Masukkan nama Anda          : {Fore.GREEN}")
    try:
        tanggal = int(input(Fore.GREEN + f"{Fore.WHITE}Masukkan tanggal lahir (dd) :{Fore.GREEN} "))
        
        bulan = int(input(Fore.GREEN + f"{Fore.WHITE}Masukkan bulan lahir   (mm) :{Fore.GREEN} "))
        
        tahun = int(input(Fore.GREEN + f"{Fore.WHITE}Masukkan tahun lahir (yyyy) :{Fore.GREEN} "))

        print(Fore.CYAN + f"\nMenghitung usia...")
        time.sleep(5)  # Memberi kesan proses sedang berjalan

        tanggal_lahir = datetime(tahun, bulan, tanggal)
        usia_tahun, usia_bulan, usia_hari, hari_sampai_ulang_tahun = hitung_usia_lengkap(tanggal_lahir)
        
        print(f"\nHallo {Fore.GREEN}{nama}")
        print(Fore.WHITE + f"Usiamu saat ini : {Fore.GREEN}{usia_tahun} tahun,")
        print(Fore.WHITE + f"Jumlah hari sampai ulang tahun berikutnya : {Fore.GREEN}{hari_sampai_ulang_tahun} hari\n")

    except ValueError as e:
        print(Fore.RED + "\nData yang dimasukkan tidak valid. Harap masukkan format yang benar.") 
    time.sleep(15)
    os.system("clear")
    return main()
   

if __name__ == "__main__":
    main()
