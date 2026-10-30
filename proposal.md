# Proposal Proyek Akhir

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas

## 2. Latar Belakang
Pengolahan nilai siswa merupakan salah satu kegiatan penting dalam pembelajaran matematika. Penghitungan nilai secara manual membutuhkan waktu dan berisiko mengalami kesalahan. Oleh karena itu, dibuat program sederhana menggunakan Python untuk membantu menghitung dan menganalisis nilai siswa secara otomatis.

## 3. Pengguna dan Tujuan
Pengguna utama program adalah guru matematika.

Tujuan proyek ini adalah mempermudah guru dalam mengolah nilai siswa, menghitung statistik kelas, menentukan ketuntasan belajar, dan menyimpan laporan hasil analisis.

## 4. Ruang Lingkup
Fitur utama program:
1. Membaca data nilai siswa dari file.
2. Memvalidasi nilai dalam rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan maksimum.
4. Menentukan jumlah siswa tuntas dan belum tuntas.
5. Menyimpan hasil analisis ke file teks.

Program berbasis terminal dan tidak menggunakan antarmuka grafis.

## 5. Kebutuhan Program

**Kebutuhan fungsional:**
- Membaca data nilai siswa.
- Memvalidasi input.
- Menghitung statistik nilai.
- Menentukan status ketuntasan berdasarkan KKM.
- Menyimpan laporan hasil.

**Kebutuhan nonfungsional:**
- Mudah dijalankan melalui VS Code.
- Menggunakan Python 3.
- Memiliki kode yang mudah dipahami.
- Menampilkan pesan kesalahan yang jelas.

## 6. Input, Proses, Output

**Input:** File teks berisi nama siswa dan nilai matematika.

**Proses:** Membaca data, memvalidasi nilai, menghitung statistik, dan menentukan ketuntasan.

**Output:** Rata-rata, nilai minimum, nilai maksimum, jumlah siswa tuntas, jumlah siswa belum tuntas, dan file laporan.

## 7. Algoritma dan Pseudocode Program

Algoritma program dirancang untuk mengolah data nilai matematika siswa secara otomatis, mulai dari membaca data, memvalidasi nilai, menghitung statistik kelas, menentukan ketuntasan berdasarkan KKM 75, hingga menyimpan laporan hasil analisis.

**Pseudocode:**

```text
MULAI

KKM = 75
Baca file nilai_contoh.txt

JIKA file tidak ditemukan
    Tampilkan pesan kesalahan
    SELESAI
AKHIR JIKA

Siapkan daftar siswa kosong

UNTUK setiap baris data
    Baca nama dan nilai siswa

    JIKA nilai berupa angka DAN 0 <= nilai <= 100
        Simpan data siswa
    JIKA TIDAK
        Tampilkan pesan data tidak valid
    AKHIR JIKA
SELESAI PERULANGAN

JIKA daftar siswa kosong
    Tampilkan pesan tidak ada data valid
    SELESAI
AKHIR JIKA

Hitung jumlah siswa
Hitung rata-rata nilai
Cari nilai tertinggi
Cari nilai terendah

UNTUK setiap siswa
    JIKA nilai >= KKM
        Status = Tuntas
    JIKA TIDAK
        Status = Belum Tuntas
    AKHIR JIKA
SELESAI PERULANGAN

Hitung jumlah siswa tuntas
Hitung jumlah siswa belum tuntas

Tampilkan hasil analisis
Simpan laporan ke output/hasil_rekap.txt

SELESAI
```

Pseudocode tersebut menggambarkan alur kerja program yang nantinya akan diimplementasikan menggunakan Python pada Pertemuan 15.
8. Struktur Program

Program dirancang menggunakan beberapa modul:

main.py: Menjalankan alur utama program.

data_io.py: Membaca data dan menyimpan laporan.

analisis.py: Menghitung statistik nilai.

utilitas.py: Memvalidasi nilai dan menentukan ketuntasan.

9. Struktur Data

Program menggunakan list untuk menyimpan kumpulan data siswa, dictionary untuk menyimpan nama dan nilai, serta string untuk menyusun laporan.

10. Rencana Test Case

ID

Kondisi

Hasil yang Diharapkan

TC01

Nilai 80, 70, 90

Rata-rata 80

TC02

Nilai 0

Diterima

TC03

Nilai 100

Diterima

TC04

Nilai 105

Ditolak

TC05

File tidak tersedia

Pesan error ditampilkan

TC06

Semua nilai memenuhi KKM

Semua siswa dinyatakan tuntas

11. Pembagian Tugas

Proyek dikerjakan secara individu.

Nama: Farid Ardiansah
NIM: 2225250125
Kelas: 3E

Seluruh proses perancangan, pemrograman, pengujian, dokumentasi, dan pengelolaan GitHub menjadi tanggung jawab individu.

12. Jadwal Pengerjaan

Pertemuan 14: Penyusunan proposal, algoritma, struktur folder, dan test case.

Pertemuan 15: Implementasi program, pengujian, debugging, dan dokumentasi.

Pertemuan 16: Presentasi dan demonstrasi proyek akhir.

13. Repository GitHub

Nama repository yang direncanakan:

proyek-akhir-farid-2225250125

URL repository akan dicantumkan setelah repository dibuat di GitHub.
