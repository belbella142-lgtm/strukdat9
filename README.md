Algoritma Backtracking – Program Python Lengkap

Program Python yang menggabungkan 3 algoritma backtracking rekursif dalam satu file:
1. N-Queens (N-Ratu)
2. Knight's Tour (Tur Kuda)
3. Knapsack (Tas Ransel)

PERSYARATAN

- Python 3.7+ (tidak memerlukan library eksternal)

Cek versi Python:
  python --version


CARA MENJALANKAN

  python backtracking_all.py

Setelah dijalankan, muncul menu utama:

  
     ALGORITMA BACKTRACKING - MENU UTAMA
  
    1. N-Queens (N-Ratu)
    2. Knight's Tour (Tur Kuda)
    3. Knapsack (Tas Ransel)
    0. Keluar
  

Ketik nomor pilihan lalu Enter.
Setelah selesai, otomatis kembali ke menu.
Ketik 0 untuk keluar.

PENJELASAN PROGRAM

[1] N-QUEENS
  Tujuan  : Tempatkan N ratu di papan N×N tanpa saling menyerang
  Input   : Ukuran papan (N)
  Cara    : Backtracking per baris, cek keamanan kolom & diagonal

[2] KNIGHT'S TOUR
  Tujuan  : Kuda mengunjungi setiap petak tepat 1 kali
  Input   : Ukuran papan (N), posisi awal kuda (baris & kolom)
  Cara    : Backtracking + Warnsdorff's Rule (pilih kotak
            dengan paling sedikit kelanjutan)
  Tips    : Gunakan N >= 5 agar lebih cepat

[3] KNAPSACK
  Tujuan  : Pilih kombinasi barang dengan total berat = target
  Input   : Data barang & berat, berat target
  Cara    : Rekursif masukkan/lewati setiap barang + pruning
  Bonus   : Jika tidak ada solusi tepat, tampilkan yang
            paling mendekati target

KOMPLEKSITAS WAKTU
  N-Queens     : O(N!)       → berkurang dengan pruning
  Knight's Tour: O(8^(N²))   → cepat dengan Warnsdorff
  Knapsack     : O(2^N)      → berkurang dengan pruning berat

STRUKTUR FILE
  .
  ├── backtracking_all.py   ← satu file semua program
  └── README.md             ← dokumentasi ini
