import os
import sys
import shutil

def install_script():
    script_name = 'alayers-dir.py'
    script_path = os.path.abspath(script_name)
    symlink_path = '/usr/local/bin/alayers-dir'
    
    if not os.path.exists(script_path):
        print(f"Script {script_name} tidak ditemukan di direktori ini.")
        sys.exit(1)

    with open(script_path, 'r') as file:
        content = file.readlines()
    
    if not content[0].startswith('#!'):
        content.insert(0, '#!/usr/bin/env python3\n')
        with open(script_path, 'w') as file:
            file.writelines(content)

    os.chmod(script_path, 0o755)

    if os.path.exists(symlink_path):
        print(f"Symlink {symlink_path} sudah ada. Menghapus dan membuat yang baru.")
        os.remove(symlink_path)
    
    os.symlink(script_path, symlink_path)
    print(f"Instalasi selesai! Anda dapat menjalankan script dengan perintah 'alayers-dir' dari manapun.")

if __name__ == "__main__":
    install_script()
