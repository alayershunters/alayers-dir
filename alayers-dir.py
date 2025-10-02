#!/usr/bin/env python3
import subprocess
import time
import os
import re
from colorama import Fore, Back, Style, init
import requests
import json
from urllib.parse import urljoin 

init(autoreset=True)

TELEGRAM_BOT_TOKEN = "8314104338:AAFicWVe1MuFyScNr-rwH1r2VyeD2Mxd9n0"

if os.path.islink(__file__):
    SCRIPT_PATH = os.path.abspath(os.readlink(__file__))
    SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
else:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

TELEGRAM_ID_FILE = os.path.join(SCRIPT_DIR, "telegram_chat_ids.json")

ascii_art = Fore.GREEN + r"""
     _    _                           ____  _      
    / \  | | __ _ _   _  ___ _ __ ___|  _ \(_)_ __ 
   / _ \ | |/ _` | | | |/ _ \ '__/ __| | | | | '__|
  / ___ \| | (_| | |_| |  __/ |  \__ \ |_| | | |   
 /_/   \_\_|\__,_|\__, |\___|_|  |___/____/|_|_|   
                  |___/
"""

def safe_input(prompt):
    try:
        return input(Fore.LIGHTGREEN_EX + Style.BRIGHT + prompt).strip()
    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram dihentikan. Terima kasih telah menggunakan tools kami.")
        raise SystemExit(0)

def create_output_folder():
    folder_name = safe_input(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Masukkan NAMA FOLDER untuk menyimpan semua hasil: ")
    if not folder_name:
        print(Fore.RED + "Nama folder tidak boleh kosong.")
        raise SystemExit(1)
        
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"Folder output '{folder_name}' berhasil dibuat/digunakan.")
        return folder_name
    except OSError as e:
        print(Fore.RED + f"Gagal membuat folder {folder_name}: {e}")
        raise SystemExit(1)

def load_telegram_ids():
    if not os.path.exists(TELEGRAM_ID_FILE):
        return []
    try:
        with open(TELEGRAM_ID_FILE, 'r') as f:
            content = f.read()
            if content:
                return json.loads(content)
            return []
    except (json.JSONDecodeError, Exception) as e:
        print(Fore.RED + f"[*] Peringatan: Gagal memuat ID Telegram. File mungkin rusak. ({e})")
        return []

def save_telegram_ids(ids):
    try:
        with open(TELEGRAM_ID_FILE, 'w') as f:
            json.dump(ids, f, indent=4)
        return True
    except Exception as e:
        print(Fore.RED + f"[*] Gagal menyimpan ID Telegram: {e}")
        return False

def run_telegram_settings():
    ids = load_telegram_ids()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_hacker_header()
        
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "================[ PENGATURAN ID TELEGRAM ]================")
        print(Fore.LIGHTCYAN_EX + f"ID Telegram Terdaftar (File: {TELEGRAM_ID_FILE}):")
        
        if not ids:
            print(Fore.YELLOW + Style.DIM + "    (Saat ini belum ada ID Telegram yang terdaftar)")
        else:
            for i, chat_id in enumerate(ids):
                print(Fore.LIGHTGREEN_EX + f"    [{i+1}] ID: {chat_id}")
                
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "==========================================================")
        print(Fore.LIGHTCYAN_EX + "Pilih Opsi:")
        print(Fore.CYAN + "1. Tambah ID Telegram Baru")
        print(Fore.CYAN + "2. Hapus ID Telegram (Berdasarkan nomor)")
        print(Fore.CYAN + "9. Kembali ke Menu Utama")
        
        choice = safe_input(Fore.LIGHTGREEN_EX + "Masukkan pilihan (1/2/9): ")
        
        if choice == '1':
            new_id = safe_input(Fore.LIGHTCYAN_EX + "Masukkan ID Telegram baru (hanya angka, bisa negatif): ").strip()
            if re.match(r'^-?\d+$', new_id): 
                if new_id not in ids:
                    ids.append(new_id)
                    save_telegram_ids(ids)
                    print(Fore.GREEN + f"[+] ID '{new_id}' berhasil ditambahkan.")
                else:
                    print(Fore.YELLOW + "[-] ID tersebut sudah terdaftar.")
            else:
                print(Fore.RED + "[-] Format ID tidak valid. Harus berupa angka.")
            time.sleep(2)
            
        elif choice == '2':
            if not ids:
                print(Fore.YELLOW + "[-] Tidak ada ID untuk dihapus.")
                time.sleep(2)
                continue
            
            try:
                index_to_delete = int(safe_input(Fore.LIGHTCYAN_EX + "Masukkan NOMOR [ ] ID yang akan dihapus: "))
                
                if 1 <= index_to_delete <= len(ids):
                    deleted_id = ids.pop(index_to_delete - 1)
                    save_telegram_ids(ids)
                    print(Fore.GREEN + f"[+] ID '{deleted_id}' berhasil dihapus.")
                else:
                    print(Fore.RED + "[-] Nomor pilihan tidak valid.")
            except ValueError:
                print(Fore.RED + "[-] Input harus berupa angka.")
            time.sleep(2)
            
        elif choice == '9':
            return
            
        else:
            print(Fore.RED + "[-] Pilihan tidak valid.")
            time.sleep(1)

def extract_dirsearch_results(raw_output_file, base_url):
    results = set() 
    
    pattern_log = re.compile(r'^\s*\[\d{2}:\d{2}:\d{2}\]\s*\d{3}\s*-\s*[\dKBME]*\s*-\s*(.*)$', re.IGNORECASE)
    
    pattern_clean = re.compile(r'^\s*(\d{3})\s+([\d\.KBME]+)\s+(http[s]?://.*)$', re.IGNORECASE)


    try:
        with open(raw_output_file, 'r') as f:
            for line in f:
                clean_line = line.strip() 

                match_clean = pattern_clean.search(clean_line)
                if match_clean:
                    code = match_clean.group(1).strip()
                    size = match_clean.group(2).strip()
                    full_url = match_clean.group(3).strip()
                    
                    results.add(f"{code}\t{size}\t{full_url}")
                    continue 
                
                match_log = pattern_log.search(clean_line)
                if match_log:
                    raw_path = match_log.group(1).strip()
                    
                    if raw_path.startswith('/'):
                        
                        log_display_match = re.search(r'(\d{3})\s*-\s*[\dKBME]*\s*-\s*(.*)', clean_line)
                        if log_display_match:
                            code = log_display_match.group(1).strip()
                            
                            full_url = urljoin(base_url.rstrip('/') + '/', raw_path.lstrip('/'))
                            
                            results.add(f"{code}\t-\t{full_url}")

    except FileNotFoundError:
        print(Fore.RED + f"File hasil '{raw_output_file}' tidak ditemukan untuk diolah.")
    except Exception as e:
        print(Fore.RED + f"Gagal memproses hasil Dirsearch untuk Telegram: {e}")
        
    return list(results) 

def send_telegram_message(status_message, target_url=None, results_list=None, results_filepath=None):
    chat_ids = load_telegram_ids()
    if not chat_ids:
        print(Fore.YELLOW + "[-] Tidak ada ID Telegram terdaftar. Notifikasi dilewati.")
        return
    
    print(Fore.YELLOW + f"[+] Mengirim notifikasi ke {len(chat_ids)} ID Telegram...")
    
    api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    full_message = f"🚨 *[ALAYERS TOOLS REPORT - DIREKTORI]* 🚨\n\n"
    
    clean_target_url = target_url.replace("https://", "").replace("http://", "") if target_url else 'N/A'
    full_message += f"▶️ *TARGET:* `{clean_target_url}`\n"
    
    full_message += f"✅ *STATUS:* *{status_message}*\n"
    
    if results_list:
        full_message += "\n*--- HASIL DITEMUKAN (15 Teratas) ---*\n"
        
        table_message = "```\n"
        table_message += "| CODE | SIZE | URL\n"
        table_message += "|------|------|-------------------------------------\n"
        
        clickable_links = [] 
        
        for i, result_line in enumerate(results_list[:15]):
             try:
                 parts = result_line.split('\t')
                 code = parts[0].ljust(4)
                 size = parts[1].ljust(4) if parts[1] != '-' else parts[1].ljust(4)
                 url = parts[2]
                 
                 table_message += f"| {code} | {size} | {url}\n"
                 
                 clickable_links.append(f"• [{url}]({url})") 
                 
             except IndexError:
                 table_message += f"| N/A  | N/A  | {result_line} (Format Error)\n"
        
        table_message += "```\n" 
        
        full_message += table_message
        
        if clickable_links:
            full_message += "\n🔗 *LINK DAPAT DIKLIK:*\n"
            full_message += "\n".join(clickable_links) + "\n" 
        
        if len(results_list) > 15:
             full_message += f"_... dan {len(results_list) - 15} hasil lainnya. Lihat log lengkap_\n"
        full_message += "\n"
        
    if results_filepath:
         full_message += f"📝 *LOG LENGKAP:* `{os.path.abspath(results_filepath)}`"

    for chat_id in chat_ids:
        try:
            payload = {
                'chat_id': chat_id,
                'text': full_message,
                'parse_mode': 'Markdown' 
            }
            
            response = requests.post(api_url, data=payload, timeout=10)
            response.raise_for_status() 
            print(Fore.GREEN + f"[+] Notifikasi berhasil dikirim ke ID {chat_id}.")
        
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"[*] Gagal mengirim ke ID {chat_id}. Error: {e}")
        except Exception as e:
            print(Fore.RED + f"[*] Terjadi kesalahan tidak terduga saat mengirim notifikasi: {e}")

def format_dirsearch_output(raw_output_file, url):
    try:
        with open(raw_output_file, 'r') as f:
            content = f.read()

        alayers_ascii = ascii_art.replace(Fore.GREEN, '')
        
        header = f"{alayers_ascii}\n# --- Alayers Tools - DIRSEARCH Results ---\n# Target URL: {url}\n# Tanggal: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        result_pattern = re.compile(r'^\s*\[.+\]\s*(\d{3})\s*-\s*(\d+B?|\d+K?|\d+M?)\s*-\s*(.*)$', re.IGNORECASE)

        lines = content.split('\n')
        new_content_lines = [header]
        
        for line in lines:
            line_stripped = line.strip()
            if result_pattern.search(line_stripped) or 'Dirsearch started' in line_stripped:
                new_content_lines.append(line_stripped)
            elif re.search(r'^\s*(\d{3})\s+([\d\.KBME]+)\s+(http[s]?://.*)$', line_stripped, re.IGNORECASE):
                 new_content_lines.append(line_stripped)
                 
        final_content = "\n".join(new_content_lines)
        with open(raw_output_file, 'w') as f:
            f.write(final_content)
        
    except Exception as e:
        print(Fore.RED + f"Gagal memproses output file untuk arsip: {e}")


def run_dirsearch(url, output_file):
    try:
        if not url.startswith('http'):
            print(Fore.YELLOW + f"[*] URL '{url}' tidak memiliki skema (http/https). Mengasumsikan 'https://'.")
            url = f"https://{url}"

        exclude_status_codes = ','.join(str(code) for code in range(300, 601))
        
        print(Fore.CYAN + f"Memulai Dirsearch untuk URL {url}...")
        
        subprocess.run(['dirsearch', '-u', url, '--exclude-status', exclude_status_codes, '-o', output_file], check=True)

        format_dirsearch_output(output_file, url)
        
        results = extract_dirsearch_results(output_file, url)
        
        status_message = f"BERHASIL ({len(results)} hasil ditemukan)"
        send_telegram_message(status_message, url, results, output_file)
        
        print(Fore.GREEN + f"Proses selesai untuk URL {url}. Hasil diformat dan disimpan di {output_file}")
    
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Gagal menjalankan dirsearch untuk {url}: {e}. Pastikan dirsearch terinstal.")
        error_message = f"GAGAL. Pastikan Dirsearch terinstal & URL Benar. Error: {e.returncode}"
        send_telegram_message(error_message, url, None, output_file) 
    except KeyboardInterrupt:
        print(Fore.RED + "\nProses dihentikan oleh pengguna. Program berhenti.")
        raise SystemExit(0)
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan umum pada run_dirsearch: {e}")
        send_telegram_message(f"GAGAL Kritis. Error: {e}", url, None, output_file)


def run_subfinder_httpx(url, subfinder_output, httpx_output, dirsearch_output):
    if not url.startswith('http'):
        url = f"https://{url}"
        
    try:
        print(Fore.LIGHTCYAN_EX + f"Menjalankan Subfinder untuk URL {url}...")
        subprocess.run(['subfinder', '-d', url, '-o', subfinder_output], check=True)

        print(Fore.LIGHTCYAN_EX + f"Menjalankan httpx-toolkit untuk subdomain yang ditemukan...")
        subprocess.run(['httpx-toolkit', '-l', subfinder_output, '-o', httpx_output, '-mc', '200'], check=True)

        print(Fore.LIGHTGREEN_EX + f"Proses Subdomain & HTTPX selesai. Subdomain aktif disimpan di {httpx_output}")
        print(Fore.YELLOW + "Melanjutkan ke pemetaan direktori tersembunyi...")

        run_on_urls_from_file(httpx_output, dirsearch_output)
        
        summary_message = f"Rantai Subdomain/Dirsearch SELESAI.\nTarget Awal: {url}\nSemua hasil Dirsearch terperinci telah dikirim secara individual."
        send_telegram_message(summary_message, url, None, dirsearch_output) 

    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Gagal menjalankan Subfinder atau httpx-toolkit: {e}. Pastikan kedua tools terinstal.")
        error_message = f"Rantai Pemindaian GAGAL!\nTarget Awal: {url}\nError: Subfinder/httpx gagal. {e.returncode}"
        send_telegram_message(error_message, url) 
    except KeyboardInterrupt:
        print(Fore.RED + "\nProses dihentikan oleh pengguna. Program berhenti.")
        raise SystemExit(0)

def run_on_urls_from_file(file_path, output_file):
    try:
        with open(output_file, 'w') as f:
            f.write('')
            
        with open(file_path, 'r') as file:
            urls = file.readlines()

        urls = [url.strip() for url in urls if url.strip()] 

        print(Fore.LIGHTCYAN_EX + f"Memulai pemindaian direktori untuk {len(urls)} URL...")

        for i, url in enumerate(urls):
            print(Fore.BLUE + f"[{i+1}/{len(urls)}] Memindai: {url}")
            run_dirsearch(url, output_file)

    except FileNotFoundError:
        print(Fore.RED + f"File input {file_path} tidak ditemukan!")
        error_message = f"Pemindaian Daftar URL GAGAL!\nError: File input '{file_path}' tidak ditemukan."
        send_telegram_message(error_message) 
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan: {e}")
        error_message = f"Pemindaian Daftar URL GAGAL KRITIS!\nError: {e}"
        send_telegram_message(error_message)

def print_hacker_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "===============================================")
    print(ascii_art)
    print(Fore.LIGHTGREEN_EX + " " * 15 + Style.BRIGHT + ":: V.2.1 - AlayersHunt ::")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "===============================================")
    
    print(Fore.LIGHTGREEN_EX + "|     " + Back.BLACK + Style.BRIGHT + " A L A Y E R S   T O O L S " + Style.RESET_ALL + Fore.LIGHTGREEN_EX + "             |")
    print(Fore.LIGHTCYAN_EX + "|  Pencarian Direktori & Subdomain Otomatis   |")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "===============================================")
    
    warning_message = f"""
    {Fore.LIGHTCYAN_EX + Style.BRIGHT}┌────────────────────────────────────────────────┐
    │ {Fore.RED + Style.BRIGHT}PERINGATAN ETIKA PENGGUNAAN:{Fore.LIGHTCYAN_EX + Style.BRIGHT}                   │
    │ Gunakan alat ini dengan {Fore.RED + Style.BRIGHT}bijak dan bertanggung{Fore.LIGHTCYAN_EX + Style.BRIGHT}  │
    │ {Fore.RED + Style.BRIGHT}jawab{Fore.LIGHTCYAN_EX + Style.BRIGHT}. Tindakan ilegal adalah tanggung jawab   │
    │ pribadi Anda. Kami {Fore.RED + Style.BRIGHT}TIDAK BERTANGGUNG JAWAB{Fore.LIGHTCYAN_EX + Style.BRIGHT}     │
    │ atas penyalahgunaan alat ini.                  │
    │ {Fore.LIGHTYELLOW_EX}Instagram: @alwi_alpariamani{Fore.LIGHTCYAN_EX + Style.BRIGHT}                   │
    └────────────────────────────────────────────────┘
    """
    print(warning_message)
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "===============================================")
    print(Fore.LIGHTCYAN_EX + "Pilih salah satu opsi berikut:")
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "1. Pencarian Subdomain dan Direktori Tersembunyi pada Website")
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "2. Pemetaan Direktori Tersembunyi melalui Daftar URL")
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "3. Pemindaian Direktori Tersembunyi pada URL Tertentu")
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "4. Settings ID Telegram")
    print(Style.BRIGHT + Fore.LIGHTRED_EX + "9. Keluar")
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "===============================================")
    print("\n")

def run_on_user_input():
    
    print_hacker_header()

    choice = safe_input(Fore.LIGHTGREEN_EX + "Masukkan pilihan (1/2/3/4/9): ")

    default_files = {
        'subfinder': 'subdomain.txt',
        'httpx': 'aktif-subdomain.txt',
        'dirsearch': 'hasil.txt'
    }
    
    subfinder_file, httpx_file, dirsearch_file = None, None, None
    if choice in ["1", "2", "3"]:
        print("\n" + Fore.LIGHTYELLOW_EX + "Apakah Anda ingin menggunakan nama file output default? (Y/T)")
        print(Fore.YELLOW + f"  Default Hasil Dir: {default_files['dirsearch']}")
        use_default = safe_input(Fore.LIGHTGREEN_EX + "Pilihan (Y/T): ").lower()
        
        if use_default == 'y':
            dirsearch_file = default_files['dirsearch']
            subfinder_file = default_files['subfinder']
            httpx_file = default_files['httpx']
            print(Fore.CYAN + "Menggunakan nama file default.")


    if choice == "1":
        url = safe_input(Fore.LIGHTCYAN_EX + "Masukkan URL target (misalnya: example.com): ")
        folder_name = create_output_folder()

        if subfinder_file is None:
            subfinder_file = safe_input(Fore.LIGHTCYAN_EX + "Masukkan nama file output untuk subdomain (misalnya: subdomain.txt): ")
            httpx_file = safe_input(Fore.LIGHTCYAN_EX + "Masukkan nama file output untuk sub domain aktif (misalnya: aktif.txt): ")
            dirsearch_file = safe_input(Fore.LIGHTCYAN_EX + "Masukkan nama file output untuk hasil pencarian direktori (misalnya: hasil_dir.txt): ")

        subfinder_output = os.path.join(folder_name, subfinder_file)
        httpx_output = os.path.join(folder_name, httpx_file)
        dirsearch_output = os.path.join(folder_name, dirsearch_file)

        run_subfinder_httpx(url, subfinder_output, httpx_output, dirsearch_output)

    elif choice == "2":
        folder_name = create_output_folder()
        file_path = safe_input(Fore.LIGHTCYAN_EX + "Masukkan NAMA FILE input yang berisi daftar URL (misalnya: urls.txt): ")

        if dirsearch_file is None:
            dirsearch_file = safe_input(Fore.LIGHTCYAN_EX + "Masukkan nama file output untuk hasil direktori (misalnya: hasil_dir.txt): ")

        output_file = os.path.join(folder_name, dirsearch_file)
        
        run_on_urls_from_file(file_path, output_file)

    elif choice == "3":
        url = safe_input(Fore.LIGHTCYAN_EX + "Masukkan URL target lengkap (misalnya: https://example.com): ")
        folder_name = create_output_folder()

        if dirsearch_file is None:
            dirsearch_file = safe_input(Fore.LIGHTCYAN_EX + "Masukkan nama file output untuk hasil direktori (misalnya: hasil_dir.txt): ")

        output_file = os.path.join(folder_name, dirsearch_file)
        
        run_dirsearch(url, output_file)

    elif choice == "4":
        run_telegram_settings()
    
    elif choice == "9":
        print(Fore.RED + "\nProgram dihentikan. Terima kasih telah menggunakan tools kami.")
        raise SystemExit(0)

    else:
        print(Fore.RED + "Pilihan tidak valid. Program dihentikan.")
        time.sleep(1)


if __name__ == "__main__":
    while True:
        try:
            run_on_user_input()
        except SystemExit:
            break
        except Exception as e:
            print(Fore.RED + f"\nTerjadi kesalahan kritis tak terduga: {e}")
            break
        
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n\n===============================================")
        cont = safe_input(Fore.LIGHTYELLOW_EX + "Operasi selesai. Tekan ENTER untuk kembali ke menu utama, atau ketik 'q' untuk keluar: ").lower()
        if cont == 'q':
            print(Fore.RED + "\nProgram dihentikan. Terima kasih telah menggunakan tools kami.")
            break
