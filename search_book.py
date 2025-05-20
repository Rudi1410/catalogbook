def search_book(books):
    print("\n=== PENCARIAN BUKU ===")
    print("1. Berdasarkan Judul")
    print("2. Berdasarkan Penulis")
    print("3. Berdasarkan Tahun Terbit")

    choice = input("Pilih metode pencarian (1/2/3): ").strip()

    if choice == "1":
        keyword = input("Masukkan judul buku: ").strip().lower()
        results = [book for book in books if keyword in book['title'].lower()]
    elif choice == "2":
        keyword = input("Masukkan nama penulis: ").strip().lower()
        results = [book for book in books if keyword in book['author'].lower()]
    elif choice == "3":
        keyword = input("Masukkan tahun terbit: ").strip()
        results = [book for book in books if book['year'] == keyword]
    else:
        print("❌ Pilihan tidak valid.")
        return

    if results:
        print(f"\nDitemukan {len(results)} buku:")
        for idx, book in enumerate(results, 1):
            print(f"{idx}. {book['title']} oleh {book['author']} ({book['year']})")
    else:
        print("❌ Tidak ada buku yang cocok dengan pencarian.\n")
