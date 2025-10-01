#!/usr/bin/env python3
import subprocess
import time
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)

ascii_art = Fore.GREEN + r"""
     _    _                           ____  _      
    / \  | | __ _ _   _  ___ _ __ ___|  _ \(_)_ __ 
   / _ \ | |/ _` | | | |/ _ \ '__/ __| | | | | '__|
  / ___ \| | (_| | |_| |  __/ |  \__ \ |_| | | |   
 /_/   \_\_|\__,_|\__, |\___|_|  |___/____/|_|_|   
                  |___/   
"""

def print_hacker_header():
    print(ascii_art)
    print(Fore.RED + "_______________________________________________")
    print(Fore.YELLOW + "|          Alayers Tools - Tools sederhana     |")
    print(Fore.YELLOW + "|    Menemukan Direktori dan File Tersembunyi  |")
    print(Fore.RED + "|______________________________________________|")
    print("\n")
    time.sleep(2)
    
    warning_message = """
    ┌────────────────────────────────────────────┐
    │ Gunakan alat ini dengan bijak dan tanggung │
    │ jawab.                                     │
    │ Jika ada tindakan yang salah atau melanggar│
    │ hukum, kami tidak bertanggung jawab atas   │
    │ akibatnya.                                 │
    │ Instagram: @alwi_alpariamani               │
    └────────────────────────────────────────────┘
    """
    print(Fore.YELLOW + warning_message)

def run_dirsearch(url, output_file):
    try:
        exclude_status_codes = ','.join(str(code) for code in range(300, 601))

        with open(output_file, 'a') as f:
            f.write(ascii_art)
            f.write(Fore.CYAN + f"\n# Pencarian dimulai untuk URL {url} pada {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(Fore.CYAN + "Mencari direktori dan file tersembunyi.\n\n")
        
        subprocess.run(['dirsearch', '-u', url, '--exclude-status', exclude_status_codes, '-o', output_file], check=True)
        
        with open(output_file, 'a') as f:
            f.write(Fore.GREEN + f"\nProses selesai untuk URL {url}. Hasil disimpan di {output_file}\n\n")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Gagal menjalankan dirsearch untuk {url}: {e}")
        with open(output_file, 'a') as f:
            f.write(Fore.RED + f"Gagal menjalankan dirsearch untuk {url}: {e}\n")
    except KeyboardInterrupt:
        print(Fore.RED + "\nProses dihentikan oleh pengguna. Program berhenti.")
        exit(0)

def run_subfinder_httpx(url, subfinder_output, httpx_output):
    try:
        print(Fore.CYAN + f"Menjalankan Subfinder untuk URL {url}...")
        subprocess.run(['subfinder', '-d', url, '-o', subfinder_output], check=True)
        
        print(Fore.CYAN + f"Menjalankan httpx-toolkit untuk subdomain yang ditemukan...")
        subprocess.run(['httpx-toolkit', '-l', subfinder_output, '-o', httpx_output, '-mc', '200'], check=True)
        
        print(Fore.GREEN + f"Proses selesai. Hasil disimpan di {httpx_output}")
        
        run_on_urls_from_file(httpx_output, dirsearch_output)
        
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Gagal menjalankan Subfinder atau httpx-toolkit: {e}")
    except KeyboardInterrupt:
        print(Fore.RED + "\nProses dihentikan oleh pengguna. Program berhenti.")
        exit(0)

def safe_input(prompt):
    try:
        return input(Fore.YELLOW + prompt).strip()
    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram dihentikan. Terima kasih telah menggunakan tools kami.")
        exit(0)

def run_on_urls_from_file(file_path, output_file):
    try:
        with open(output_file, 'w') as f:
            f.write(ascii_art)
            f.write(Fore.RED + "_______________________________________________\n")
            f.write(Fore.YELLOW + "|          Hacker Tool - DIRSEARCH            |\n")
            f.write(Fore.YELLOW + "|    Menemukan Direktori dan File Tersembunyi  |\n")
            f.write(Fore.RED + "|______________________________________________|\n\n")

        with open(file_path, 'r') as file:
            urls = file.readlines()
        
        urls = [url.strip() for url in urls]
        
        for url in urls:
            run_dirsearch(url, output_file)
    except FileNotFoundError:
        print(Fore.RED + f"File {file_path} tidak ditemukan!")
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    print_hacker_header()

    print(Fore.CYAN + "Pilih salah satu opsi berikut:")
    print(Fore.YELLOW + "1. Pencarian Subdomain dan Direktori Tersembunyi pada Website")
    print(Fore.YELLOW + "2. Pemetaan Direktori Tersembunyi melalui Daftar URL")
    print(Fore.YELLOW + "3. Pemindaian Direktori Tersembunyi pada URL Tertentu")

    choice = safe_input(Fore.CYAN + "Masukkan pilihan (1/2/3): ")

    if choice == "1":
        url = safe_input(Fore.GREEN + "Masukkan URL (misalnya: example.com): ")
        subfinder_output = safe_input(Fore.GREEN + "Masukkan nama file output untuk subdomain (misalnya: subdomain.txt): ")
        httpx_output = safe_input(Fore.GREEN + "Masukkan nama file output untuk sub domain aktif (misalnya: aktif.txt): ")
        dirsearch_output = safe_input(Fore.GREEN + "Masukkan nama file output untuk hasil pencarian direktori (misalnya: hasil.txt): ")
        
        run_subfinder_httpx(url, subfinder_output, httpx_output)

    elif choice == "2":
        file_path = safe_input(Fore.GREEN + "Masukkan nama file yang berisi URL (misalnya: urls.txt): ")
        output_file = safe_input(Fore.GREEN + "Masukkan nama file output (misalnya: hasil.txt): ")
        
        run_on_urls_from_file(file_path, output_file)

    elif choice == "3":
        url = safe_input(Fore.GREEN + "Masukkan URL (misalnya: https://example.com): ")
        output_file = safe_input(Fore.GREEN + "Masukkan nama file output (misalnya: hasil.txt): ")
        
        run_dirsearch(url, output_file)

    else:
        print(Fore.RED + "Pilihan tidak valid. Program dihentikan.")
        exit(1)
