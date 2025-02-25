import os

def main():
    while True:
        os.system("clear")  # Membersihkan layar terminal
        print("\033[91m")  # Warna merah untuk header
        print("=====================================")
        print("        ENCODE / DECODE TOOL")
        print("=====================================")
        print("\033[92m")  # Warna hijau untuk teks menu
        print("[*] CHOOSE ONE OF THE OPTIONS BELOW TO CONTINUE:\n")
        print(" A) ENCODE - MD5")
        print(" B) ENCODE - SHA1")
        print(" C) ENCODE - SHA224")
        print(" D) ENCODE - SHA256")
        print(" E) ENCODE - SHA384")
        print(" F) ENCODE - SHA512")
        print(" G) ENCODE/DECODE - BASE64")
        print(" H) ENCODE/DECODE - BINARY")
        print(" I) ENCODE/DECODE - HEXADECIMAL")
        print(" J) ENCODE/DECODE - CIPHER OF CESAR")
        print(" K) REVERSE - TEXT")
        print(" L) REVERSE - WORDS")
        print("\n q) EXIT")
        print("\033[0m")  # Mengembalikan warna ke normal
        
        choice = input("\n>>> ").strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'g':
            text = input("Enter text to encode in Base64: ")
            encoded = text.encode("utf-8").hex()
            print(f"Encoded: {encoded}")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
