def add_book(books):
    title = input("Masukkan judul buku: ").strip()
    author = input("Masukkan nama penulis: ").strip()
    year = input("Masukkan tahun terbit: ").strip()

    book = {
        "title": title,
        "author": author,
        "year": year
    }

    books.append(book)
    print("✅ Buku berhasil ditambahkan.\n")
    return books
