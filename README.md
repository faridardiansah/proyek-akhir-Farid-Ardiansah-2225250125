# Proyek Akhir - Analisis Nilai Matematika Kelas

**Nama:** Farid Ardiansah  
**NIM:** 2225250125  
**Kelas:** 3E  
**Mata Kuliah:** Algoritma dan Pemrograman

## Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas merupakan proyek sederhana berbasis Python yang bertujuan membantu guru matematika dalam mengolah data nilai siswa secara otomatis.

Program dirancang untuk membaca data nilai, melakukan validasi, menghitung statistik kelas, menentukan ketuntasan belajar, dan menyimpan hasil analisis ke dalam file teks.

## Tujuan

1. Mempermudah pengolahan data nilai matematika.
2. Menghitung rata-rata, nilai minimum, dan maksimum.
3. Menentukan jumlah siswa tuntas dan belum tuntas.
4. Mengurangi kesalahan perhitungan manual.
5. Menerapkan konsep Python dalam bidang pendidikan matematika.

## Fitur Program

- Membaca data nilai siswa dari file.
- Memvalidasi nilai antara 0 sampai 100.
- Menghitung rata-rata nilai kelas.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah siswa tuntas dan belum tuntas.
- Menyimpan laporan hasil analisis.

## Struktur Folder

```text
proyek-akhir-farid-2225250125/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

## Persyaratan

- Python 3
- Visual Studio Code
- Git dan GitHub

## Cara Menjalankan

Buka terminal VS Code pada folder utama proyek, kemudian jalankan:

```bash
python3 src/main.py
```

*Catatan: Program akan diimplementasikan dan diuji pada Pertemuan 15.*

## Rencana Pengujian

Pengujian akan dilakukan menggunakan beberapa kondisi, yaitu:

1. Data nilai normal.
2. Nilai batas minimum 0.
3. Nilai batas maksimum 100.
4. Nilai tidak valid di atas 100.
5. File input tidak ditemukan.
6. Semua siswa mencapai batas ketuntasan.

## Tahapan Pengembangan

**Pertemuan 14:** Perancangan proyek, penyusunan proposal, algoritma, struktur folder, dan test case.

**Pertemuan 15:** Implementasi kode Python, pengujian, perbaikan bug, dan dokumentasi hasil.

**Pertemuan 16:** Presentasi dan demonstrasi proyek akhir.

## Pengembang

Farid Ardiansah  
2225250125  
Kelas 3E - Pendidikan Matematika

## Status Proyek

## Hasil Implementasi Pertemuan 15

Program Rekap dan Analisis Nilai Matematika Kelas telah diimplementasikan menggunakan Python dengan pendekatan modular.

### Modul Program

- `src/main.py`: Mengatur alur utama program.
- `src/data_io.py`: Membaca data siswa dan menyimpan laporan.
- `src/analisis.py`: Menghitung statistik nilai dan ketuntasan.
- `src/utilitas.py`: Memvalidasi nilai dan menentukan status siswa.

### Hasil Program

Berdasarkan 10 data siswa pada `data/nilai_contoh.txt`, diperoleh hasil:

| Keterangan | Hasil |
|---|---|
| Jumlah siswa | 10 |
| Rata-rata nilai | 77,50 |
| Nilai terendah | 55 |
| Nilai tertinggi | 100 |
| KKM | 75 |
| Siswa tuntas | 6 |
| Siswa belum tuntas | 4 |

Hasil analisis disimpan secara otomatis ke dalam file `output/hasil_rekap.txt`.

### Pengujian Program

Pengujian dilakukan menggunakan delapan test case yang mencakup data normal, nilai batas, input tidak valid, file tidak ditemukan, seluruh siswa tuntas, dan data kosong.

Hasil pengujian yang telah dilaksanakan dicatat pada `tests/test_case.md`.

### Catatan Debugging

Pada proses implementasi ditemukan kesalahan `ImportError` ketika fungsi `baca_data` belum dapat diimpor dari modul `data_io.py`.

Kesalahan diperbaiki dengan melengkapi fungsi pada modul tersebut.

Selain itu, ditemukan masalah nama file input yang memiliki tanda titik tambahan. Masalah diperbaiki dengan menyesuaikan nama file menjadi `nilai_contoh.txt`.

### Kontribusi Pengembang

Proyek dikerjakan secara individu oleh Farid Ardiansah (2225250125), meliputi perancangan, implementasi, pengujian, debugging, dan dokumentasi.

### Status Proyek

Implementasi program selesai. Program utama telah berhasil dijalankan, menghasilkan analisis nilai yang sesuai, dan menyimpan laporan ke file teks.

