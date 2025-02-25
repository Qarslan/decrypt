import os
import requests

# Folder penyimpanan di Android (Download Folder)
DOWNLOAD_FOLDER = "/storage/emulated/0/Download/"

# Pastikan folder download ada
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Fungsi untuk download MP3 dari YouTube
def download_ytmp3(url):
    api_url = f"https://api.siputzx.my.id/api/d/ytmp3?url={url}"
    try:
        response = requests.get(api_url)
        data = response.json()

        if data.get("status") and "data" in data:
            title = data["data"]["title"]
            download_url = data["data"]["dl"]

            # Nama file
            filename = os.path.join(DOWNLOAD_FOLDER, f"{title}.mp3")

            # Download audio
            print(f"\n[+] Downloading: {title}")
            audio_data = requests.get(download_url, stream=True)
            with open(filename, "wb") as f:
                for chunk in audio_data.iter_content(chunk_size=1024):
                    f.write(chunk)

            print(f"\n✅ Download selesai! File tersimpan di: {filename}\n")
        else:
            print("\n❌ Gagal mendapatkan link download.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

# Menu utama
def main():
    while True:
        os.system("clear")
        print("\033[91m=====================================")
        print("▌│█║▌║▌║ 𝐓𝐎𝐎𝐋𝐒 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐑 ║▌║▌║█│▌")
        print("=====================================\033[92m")
        print("[*] PILIH SALAH SATU TOOLS DOWNLOAD:\n")
        print(" 1) Download YouTube MP3 🎵")
        print("\n q) EXIT")
        print("\033[0m")

        choice = input("\n>>> ").strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == '1':
            yt_url = input("Masukkan URL YouTube: ")
            download_ytmp3(yt_url)

        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
