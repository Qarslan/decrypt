import os
import hashlib
import base64
import requests

# Pastikan folder download ada
DOWNLOAD_FOLDER = "download"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Fungsi hash encoding
def md5_encode(text): return hashlib.md5(text.encode()).hexdigest()
def sha1_encode(text): return hashlib.sha1(text.encode()).hexdigest()
def sha224_encode(text): return hashlib.sha224(text.encode()).hexdigest()
def sha256_encode(text): return hashlib.sha256(text.encode()).hexdigest()
def sha384_encode(text): return hashlib.sha384(text.encode()).hexdigest()
def sha512_encode(text): return hashlib.sha512(text.encode()).hexdigest()
def base64_encode(text): return base64.b64encode(text.encode()).decode()
def base64_decode(text): return base64.b64decode(text.encode()).decode()

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
            print(f"[+] Downloading: {title}")
            audio_data = requests.get(download_url, stream=True)
            with open(filename, "wb") as f:
                for chunk in audio_data.iter_content(chunk_size=1024):
                    f.write(chunk)

            print(f"[+] Download selesai! File tersimpan di: {filename}")
        else:
            print("[-] Gagal mendapatkan link download.")
    except Exception as e:
        print(f"[-] Error: {e}")

# Menu utama
def main():
    while True:
        os.system("clear")
        print("\033[91m=====================================")
        print("        ENCODE / DECODE TOOL")
        print("=====================================\033[92m")
        print("[*] CHOOSE ONE OF THE OPTIONS BELOW TO CONTINUE:\n")
        print(" A) ENCODE - MD5")
        print(" B) ENCODE - SHA1")
        print(" C) ENCODE - SHA224")
        print(" D) ENCODE - SHA256")
        print(" E) ENCODE - SHA384")
        print(" F) ENCODE - SHA512")
        print(" G) ENCODE/DECODE - BASE64")
        print(" H) DOWNLOAD YOUTUBE MP3")
        print("\n q) EXIT")
        print("\033[0m")

        choice = input("\n>>> ").strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            text = input("Enter text: ")
            if choice == 'a':
                print(f"MD5: {md5_encode(text)}")
            elif choice == 'b':
                print(f"SHA1: {sha1_encode(text)}")
            elif choice == 'c':
                print(f"SHA224: {sha224_encode(text)}")
            elif choice == 'd':
                print(f"SHA256: {sha256_encode(text)}")
            elif choice == 'e':
                print(f"SHA384: {sha384_encode(text)}")
            elif choice == 'f':
                print(f"SHA512: {sha512_encode(text)}")
            elif choice == 'g':
                encode_or_decode = input("Encode (e) or Decode (d)? ").strip().lower()
                if encode_or_decode == 'e':
                    print(f"Base64 Encoded: {base64_encode(text)}")
                elif encode_or_decode == 'd':
                    try:
                        print(f"Base64 Decoded: {base64_decode(text)}")
                    except Exception as e:
                        print(f"Error: {e}")
        elif choice == 'h':
            yt_url = input("Masukkan URL YouTube: ")
            download_ytmp3(yt_url)

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
