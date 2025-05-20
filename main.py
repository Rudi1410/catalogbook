from save_load import load_books, save_books
from add_book import add_book
from list_book import list_books
from search_book import search_book

def main():
    books = load_books()

    while True:
        print("\n=== MENU KATALOG BUKU ===")
        print("1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Cari Buku")
        print("4. Keluar dan Simpan")

        pilihan = input("Pilih menu (1/2/3/4): ").strip()

        if pilihan == "1":
            books = add_book(books)
        elif pilihan == "2":
            list_books(books)
        elif pilihan == "3":
            search_book(books)
        elif pilihan == "4":
            save_books(books)
            print("📚 Katalog disimpan. Terima kasih!")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
