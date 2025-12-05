# TODO Найдите количество книг, которое можно разместить на дискете

diskette_size_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

bytes_per_kb = 1024
kb_per_mb = 1024

total_chars_per_book = pages_per_book * lines_per_page * chars_per_line
book_size_bytes = total_chars_per_book * bytes_per_char

diskette_size_bytes = diskette_size_mb * kb_per_mb * bytes_per_kb

books_on_diskette = int(diskette_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", books_on_diskette)
