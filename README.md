# **Alayers Dir** 🔥🕵️‍♂️

**Alayers Dir** is a set of tools designed to help find hidden directories and files on websites. This tool uses popular utilities such as `Subfinder`, `Httpx-toolkit`, and `Dirsearch` to perform scanning.

---

## **Usage Requirements**

Before using **Alayers Dir**, make sure you have installed a few required tools:

1. **Subfinder**: Used to find subdomains of a domain.
2. **Httpx-toolkit**: Used to verify the active subdomains discovered.
3. **Dirsearch**: Used to find hidden directories and files on websites.

You can install these tools by following the instructions below:

### **1. Install Subfinder**
Follow the instructions on the Subfinder GitHub page for installation:  
[Subfinder GitHub](https://github.com/projectdiscovery/subfinder)

### **2. Install Httpx-toolkit**
Install using Go:

```bash
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
```

### **3. Install Dirsearch**
Clone the Dirsearch repository and install its dependencies:

```bash
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
pip install -r requirements.txt
```

---

## **Installing Alayers Dir**

To install **Alayers Dir** on your system, follow these steps:

### **1. Clone the Repository**

Clone the **Alayers Dir** repository using `git`:

```bash
git clone https://github.com/alayershunters/alayers-dir.git
cd alayers-dir
```

### **2. Install Dependencies**

Make sure you have Python 3.x installed on your system, then install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### **3. Install Subfinder, Httpx, and Dirsearch**

As mentioned before, ensure that you have **Subfinder**, **Httpx-toolkit**, and **Dirsearch** installed.

---

## **How to Run Alayers Dir**

Once the installation is complete, you can run **Alayers Dir** as follows:

### **1. Running the Tools**

To run **Alayers Dir**, simply execute the Python file `alayers.py` in the directory where you cloned the repository. You can run it using the following command:

```bash
python3 alayers.py
```

The program will display an interactive menu with the following options:

- **Find Subdomains and Hidden Directories on a Website**
- **Map Hidden Directories via a List of URLs**
- **Scan Hidden Directories on a Specific URL**

### **2. Providing Input**

After selecting one of the options, you will be prompted to enter the URL and output file for the scan results. The tool will automatically execute other tools such as **Subfinder**, **Httpx-toolkit**, and **Dirsearch** to perform the scan and save the results in the output file you specify.

---

## **Running Alayers Dir Anywhere (Linux)** 

To run **Alayers Dir** from anywhere in the terminal on Linux, you need to install it first using the `installer.py` file provided.

### **Steps:**

1. **Clone the Repository to Your Desired Directory**

   Clone the **Alayers Dir** repository into the directory you prefer:

   ```bash
   git clone https://github.com/alayershunters/alayers-dir.git
   cd alayers-dir
   ```

2. **Run the Installer for Global Installation**

   Once inside the **Alayers Dir** directory, run the `installer.py` file using the following command to install **Alayers Dir** so you can run it from anywhere:

   ```bash
   python3 installer.py
   ```

   This command will automatically add **Alayers Dir** to your **PATH environment variable**, allowing you to access it from any terminal location.

3. **Run the Tool from Anywhere**

   After installation is complete, you can now run **Alayers Dir** from any terminal by simply typing:

   ```bash
   alayers-dir
   ```

4. **Manually Add Path (Optional)**

   If you prefer to manually add the path, you can do so by adding the directory of **Alayers Dir** to your **PATH environment variable**:

   Add the following line to your `~/.bashrc` or `~/.zshrc` file (depending on which shell you're using):

   ```bash
   export PATH="$PATH:/path/to/alayers-dir"
   ```

   Replace `/path/to/alayers-dir` with the actual path to your **Alayers Dir** directory.

5. **Activate Changes**

   After adding the path to your shell configuration file, activate the changes by running:

   ```bash
   source ~/.bashrc    # If you're using bash
   source ~/.zshrc     # If you're using zsh
   ```

---

## **Contact**

- LinkedIn: [alwialhadad](https://id.linkedin.com/in/alwialhadad)
- Instagram: [@alwi_alpariamani](https://www.instagram.com/alwi_alpariamani)


---

# **Alayers Dir** 🔥🕵️‍♂️

**Alayers Dir** adalah sekumpulan alat yang dirancang untuk membantu menemukan direktori dan file tersembunyi di situs web. Tools ini menggunakan beberapa alat populer seperti `Subfinder`, `Httpx-toolkit`, dan `Dirsearch` untuk melakukan pemindaian.

---

## **Syarat Penggunaan**

Sebelum menjalankan **Alayers Dir**, pastikan Anda telah menginstal beberapa alat yang dibutuhkan:

1. **Subfinder**: Digunakan untuk menemukan subdomain dari sebuah domain.
2. **Httpx-toolkit**: Digunakan untuk memverifikasi subdomain yang ditemukan.
3. **Dirsearch**: Digunakan untuk menemukan direktori dan file tersembunyi pada website.

Anda bisa menginstal ketiga alat ini dengan cara berikut:

### **1. Install Subfinder**
Ikuti petunjuk di GitHub untuk instalasi Subfinder:  
[Subfinder GitHub](https://github.com/projectdiscovery/subfinder)

### **2. Install Httpx-toolkit**
Install menggunakan Go:

```bash
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
```

### **3. Install Dirsearch**
Clone repository Dirsearch dan install dependensinya dengan cara berikut:

```bash
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
pip install -r requirements.txt
```

---

## **Instalasi Alayers Dir**

Untuk menginstal **Alayers Dir** di sistem Anda, ikuti langkah-langkah berikut:

### **1. Clone Repository**

Clone repository **Alayers Dir** menggunakan `git`:

```bash
git clone https://github.com/alayershunters/alayers-dir.git
cd alayers-dir
```

### **2. Install Dependencies**

Pastikan Anda memiliki Python 3.x yang terinstal di sistem Anda, lalu instal dependencies yang dibutuhkan menggunakan `pip`:

```bash
pip install -r requirements.txt
```

### **3. Install Subfinder, Httpx, dan Dirsearch**

Seperti disebutkan sebelumnya, pastikan Anda menginstal **Subfinder**, **Httpx-toolkit**, dan **Dirsearch**.

---

## **Cara Menjalankan Alayers Dir**

Setelah instalasi selesai, Anda dapat menjalankan **Alayers Dir** dengan cara berikut:

### **1. Menjalankan Tools**

Untuk menjalankan **Alayers Dir**, cukup jalankan file Python `alayers.py` di direktori tempat Anda meng-clone repository. Anda bisa menjalankannya menggunakan perintah:

```bash
python3 alayers.py
```

Program akan menampilkan menu interaktif dengan pilihan untuk:

- **Pencarian Subdomain dan Direktori Tersembunyi pada Website**
- **Pemetaan Direktori Tersembunyi melalui Daftar URL**
- **Pemindaian Direktori Tersembunyi pada URL Tertentu**

### **2. Memasukkan Input**

Setelah memilih salah satu opsi, Anda akan diminta untuk memasukkan URL dan file output untuk hasil pemindaian. Alat ini akan secara otomatis mengeksekusi alat lain seperti **Subfinder**, **Httpx-toolkit**, dan **Dirsearch** untuk melakukan pemindaian dan menyimpan hasilnya dalam file output yang Anda tentukan.

---

---

## **Menjalankan Alayers Dir di Mana Saja (Linux)**

Agar **Alayers Dir** bisa dijalankan dari mana saja di terminal Linux, Anda perlu menginstalnya terlebih dahulu menggunakan file `installer.py` yang sudah disediakan.

### **Langkah-langkah:**

1. **Clone Repository ke Direktori yang Diinginkan**

   Clone repository **Alayers Dir** ke dalam direktori yang Anda inginkan:

   ```bash
   git clone https://github.com/alayershunters/alayers-dir.git
   cd alayers-dir
   ```

2. **Jalankan Installer untuk Instalasi Global**

   Setelah Anda berada di dalam direktori **Alayers Dir**, jalankan `installer.py` dengan perintah berikut untuk menginstal **Alayers Dir** agar dapat dijalankan dari mana saja:

   ```bash
   python3 installer.py
   ```

   Perintah ini akan menambahkan **Alayers Dir** ke dalam **PATH environment variable**, sehingga Anda dapat mengaksesnya dari terminal mana saja tanpa perlu berada di dalam direktori tersebut.

3. **Menjalankan Tools dari Mana Saja**

   Setelah instalasi berhasil, Anda sekarang dapat menjalankan **Alayers Dir** di terminal manapun dengan mengetikkan perintah:

   ```bash
   alayers.py
   ```

4. **Menambahkan Path Secara Manual (Opsional)**

   Jika Anda lebih suka menambahkan path secara manual, Anda bisa menambahkan direktori **Alayers Dir** ke dalam **PATH environment variable** dengan cara berikut:

   Tambahkan baris berikut ke dalam file `~/.bashrc` atau `~/.zshrc` (tergantung shell yang Anda gunakan):

   ```bash
   export PATH="$PATH:/path/to/alayers-dir"
   ```

   Gantilah `/path/to/alayers-dir` dengan path yang sesuai dengan lokasi direktori **Alayers Dir** Anda.

5. **Aktifkan Perubahan**

   Setelah menambahkan path ke dalam file konfigurasi shell, aktifkan perubahan dengan menjalankan perintah berikut:

   ```bash
   source ~/.bashrc    # Jika Anda menggunakan bash
   source ~/.zshrc     # Jika Anda menggunakan zsh
   ```

---


## **Kontak**

- LinkedIn: [alwialhadad](https://id.linkedin.com/in/alwialhadad)
- Instagram: [@alwi_alpariamani](https://www.instagram.com/alwi_alpariamani)

