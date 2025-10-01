#!/bin/bash

# --- A L A Y E R S - D I R   U P D A T E R ---
# Script ini bertujuan untuk mencari dan mengganti alayers-dir.py 
# yang lama dengan versi terbaru (V2.1 - Telegram Ready)

# URL untuk mengunduh script Python updater utama
# Menggunakan struktur raw GitHub dari repository Anda: https://github.com/alayershunters/alayers-dir.git
PYTHON_UPDATER_URL="https://raw.githubusercontent.com/alayershunters/alayers-dir/main/updater.py"

echo "=========================================="
echo "  ALAYERS TOOLS: Memulai Pembaruan V2.1"
echo "=========================================="

# Cek apakah pengguna memiliki izin root (diperlukan jika file berada di /usr/local/bin)
if [ "$EUID" -ne 0 ]; then
  echo "[-] Peringatan: Anda tidak berjalan sebagai root. Pembaruan hanya akan berhasil di direktori yang dapat ditulisi."
fi

# 1. Cari lokasi file alayers-dir.py yang lama
echo "[-] Mencari lokasi instalasi alayers-dir.py..."
# Mencari di PATH dan di direktori saat ini
TOOL_PATH=$(which alayers-dir.py 2>/dev/null)
if [ -z "$TOOL_PATH" ] && [ -f "./alayers-dir.py" ]; then
    TOOL_PATH=$(readlink -f "./alayers-dir.py")
fi

if [ -z "$TOOL_PATH" ]; then
    echo "[X] ERROR: alayers-dir.py tidak ditemukan di PATH atau direktori saat ini."
    echo "Pembaruan GAGAL. Pastikan tools terinstal dengan benar."
    exit 1
fi

TOOL_DIR=$(dirname "$TOOL_PATH")
echo "[+] Tools ditemukan di: $TOOL_PATH"
echo "[+] Direktori Kerja Pembaruan: $TOOL_DIR"

# 2. Unduh dan Jalankan Updater Python
echo "[-] Mengunduh script pembaruan Python..."

# Pindah ke direktori tools agar file ditimpa di lokasi yang benar
cd "$TOOL_DIR"

# Unduh updater.py ke direktori kerja tools
curl -s "$PYTHON_UPDATER_URL" -o updater.py

if [ $? -ne 0 ]; then
    echo "[X] ERROR: Gagal mengunduh updater.py."
    exit 1
fi

# 3. Jalankan script Python updater
echo "[-] Menjalankan pembaruan dependencies dan menimpa file..."
python3 updater.py

# 4. Hapus script pembaruan sementara
rm updater.py

echo "=========================================="
echo "Pembaruan berhasil! Tools V2.1 (Telegram Ready) telah terinstal."
echo "=========================================="
