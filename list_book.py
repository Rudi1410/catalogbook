def list_books(books):
    if not books:
        print("Belum ada buku dalam katalog.")
    else:
        print("\nDaftar Buku:")
        for idx, book in enumerate(books, start=1):
            print(f"{idx}. Judul: {book['title']} | Penulis: {book['author']} | Tahun: {book['year']}")
