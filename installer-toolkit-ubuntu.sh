#!/bin/bash

# Membuat direktori tools jika belum ada dan masuk ke dalamnya
mkdir -p ~/tools
cd ~/tools

# Fungsi untuk menampilkan pesan dengan format yang rapi
function tampilkan_pesan() {
    echo -e "\e[1;34m[INFO] $1\e[0m"
    sleep 1
}

# Fungsi untuk menampilkan banner awal
function tampilkan_banner() {
    clear
    echo -e "\e[1;32m"
    echo "#############################################################"
    echo "#                                                           #"
    echo "#    Selamat datang di Installer Tools Otomatis             #"
    echo "#                                                           #"
    echo "#############################################################"
    echo -e "\e[0m"
    sleep 2
}

# Menampilkan banner awal
tampilkan_banner

# Memperbarui dan meningkatkan sistem
tampilkan_pesan "Memperbarui dan meningkatkan sistem..."
sudo apt update && sudo apt upgrade -y

# Menginstal dependensi yang dibutuhkan
tampilkan_pesan "Menginstal dependensi yang dibutuhkan..."
sudo apt install -y python3 golang git python3-venv pipx python3-pip openssl openssh-server libssl-dev

# Menginstal Subfinder menggunakan apt
if ! command -v subfinder &> /dev/null
then
    tampilkan_pesan "Menginstal Subfinder menggunakan apt..."
    sudo apt install -y subfinder
    echo -e "\e[1;32m[INFO] Subfinder berhasil diinstal menggunakan apt!\e[0m ✔"
    subfinder -version
else
    echo -e "\e[1;32m[INFO] Subfinder sudah terinstal!\e[0m ✔"
fi

# Menginstal HTTPX menggunakan apt
if ! command -v httpx &> /dev/null
then
    tampilkan_pesan "Menginstal HTTPX menggunakan apt..."
    sudo apt install -y httpx-toolkit
    echo -e "\e[1;32m[INFO] HTTPX berhasil diinstal menggunakan apt!\e[0m ✔"
    httpx -version
else
    echo -e "\e[1;32m[INFO] HTTPX sudah terinstal!\e[0m ✔"
fi

# Memeriksa apakah Dirsearch sudah ada
if ! command -v dirsearch &> /dev/null
then
    tampilkan_pesan "Menginstal Dirsearch..."
    git clone https://github.com/maurosoria/dirsearch.git --depth 1
    cd dirsearch
    sudo pip3 install -r requirements.txt --break-system-packages
    pipx install dirsearch
    pipx inject dirsearch setuptools
    echo -e "\e[1;32m[INFO] Dirsearch berhasil diinstal!\e[0m ✔"
    cd ~
else
    echo -e "\e[1;32m[INFO] Dirsearch sudah terinstal!\e[0m ✔"
fi

# Memeriksa apakah SQLMap sudah ada
if ! command -v sqlmap &> /dev/null
then
    tampilkan_pesan "Menginstal SQLMap..."
    sudo apt install -y sqlmap
    echo -e "\e[1;32m[INFO] SQLMap berhasil diinstal!\e[0m ✔"
else
    echo -e "\e[1;32m[INFO] SQLMap sudah terinstal!\e[0m ✔"
fi

# Memeriksa apakah ParamSpider sudah ada
if ! command -v paramspider &> /dev/null
then
    tampilkan_pesan "Menginstal ParamSpider..."
    sudo apt install -y paramspider
    echo -e "\e[1;32m[INFO] ParamSpider berhasil diinstal!\e[0m ✔"
else
    echo -e "\e[1;32m[INFO] ParamSpider sudah terinstal!\e[0m ✔"
fi

# Memeriksa apakah alayers-dir sudah ada
if ! command -v alayers-dir &> /dev/null
then
    tampilkan_pesan "Menginstal alayers-dir..."
    git clone https://github.com/alayershunters/alayers-dir.git
    cd alayers-dir
    sudo python3 installer.py
    echo -e "\e[1;32m[INFO] alayers-dir berhasil diinstal!\e[0m ✔"
    cd ~
else
    echo -e "\e[1;32m[INFO] alayers-dir sudah terinstal!\e[0m ✔"
fi

# Menginstal DalFox dengan cara baru
if ! command -v dalfox &> /dev/null
then
    tampilkan_pesan "Menginstal DalFox..."
    git clone https://github.com/hahwul/dalfox.git
    cd dalfox
    go install
    # Menambahkan PATH ke ~/.bashrc secara otomatis
    echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
    source ~/.bashrc
    echo -e "\e[1;32m[INFO] DalFox berhasil diinstal dan PATH telah ditambahkan secara otomatis!\e[0m ✔"
    dalfox -v
else
    echo -e "\e[1;32m[INFO] DalFox sudah terinstal!\e[0m ✔"
fi

# Menambahkan direktori ~/go/bin ke PATH untuk DalFox
tampilkan_pesan "Menambahkan direktori ~/go/bin ke PATH untuk DalFox..."
echo 'export PATH="$HOME/go/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
echo -e "\e[1;32m[INFO] Direktori ~/go/bin berhasil ditambahkan ke PATH!\e[0m ✔"

# Menambahkan direktori tools ke PATH agar bisa dijalankan dari mana saja
tampilkan_pesan "Menambahkan direktori ~/tools ke PATH..."
echo 'export PATH="$HOME/tools:$PATH"' >> ~/.bashrc
source ~/.bashrc
echo -e "\e[1;32m[INFO] Direktori ~/tools berhasil ditambahkan ke PATH!\e[0m ✔"

# Menginstal alat tambahan: slowhttptest, wapiti, nmap, dirb
tampilkan_pesan "Menginstal slowhttptest, wapiti, nmap, dirb..."
sudo apt install -y slowhttptest wapiti nmap dirb
echo -e "\e[1;32m[INFO] slowhttptest, wapiti, nmap, dirb berhasil diinstal!\e[0m ✔"

# Menginstal Nuclei menggunakan apt
tampilkan_pesan "Menginstal Nuclei menggunakan apt..."
sudo apt install -y nuclei
echo -e "\e[1;32m[INFO] Nuclei berhasil diinstal menggunakan apt!\e[0m ✔"

# Memberikan izin eksekusi pada semua alat yang terinstal di ~/tools
chmod -R +x ~/tools/*

# Menyelesaikan proses instalasi dan memberikan pengecekan alat yang terinstal
echo -e "\e[1;33mProses instalasi selesai! Semua tools sudah berhasil diinstal dan siap digunakan.\e[0m"
echo -e "\e[1;31m[#] Instalasi berhasil, tools dapat dijalankan dari mana saja! ✔\e[0m"

# Menampilkan daftar alat yang telah berhasil diinstal
echo -e "\n[INFO] Daftar Tools yang Terinstal:"

tools=("Subfinder" "HTTPX" "Dirsearch" "SQLMap" "ParamSpider" "alayers-dir" "DalFox" "slowhttptest" "wapiti" "nmap" "dirb" "Nuclei")

for tool in "${tools[@]}"; do
    if command -v "${tool,,}" &> /dev/null; then
        echo -e "[✔] $tool"
    else
        echo -e "[✘] $tool"
    fi
done
