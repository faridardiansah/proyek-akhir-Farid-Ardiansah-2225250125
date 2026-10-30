# Rencana Pengujian Proyek Akhir

## Identitas Proyek

**Judul:** Program Rekap dan Analisis Nilai Matematika Kelas  
**Nama:** Farid Ardiansah  
**NIM:** 2225250125  
**Kelas:** 3E

## Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat membaca data nilai siswa, memvalidasi nilai, menghitung statistik, menentukan ketuntasan, serta menangani kesalahan input dengan benar.

KKM yang digunakan dalam proyek ini adalah 75.

## Daftar Test Case

| ID | Skenario Pengujian | Hasil yang Diharapkan |
|---|---|---|
| TC01 | Nilai 80, 70, 90 | Rata-rata = 80 |
| TC02 | Input nilai 0 | Nilai diterima |
| TC03 | Input nilai 100 | Nilai diterima |
| TC04 | Input nilai 105 | Nilai ditolak karena melebihi 100 |
| TC05 | File input tidak ditemukan | Program menampilkan pesan kesalahan |
| TC06 | Nilai 75, 80, 90 | Semua siswa dinyatakan tuntas |
| TC07 | Input nilai `abc` | Data ditolak karena bukan angka |
| TC08 | Data nilai kosong | Program tidak mengalami error pembagian dengan nol |

## Kriteria Keberhasilan

Program dinyatakan berhasil apabila:

1. Data yang valid dapat diproses.
2. Data tidak valid dapat ditangani.
3. Perhitungan statistik menghasilkan nilai yang benar.
4. Ketuntasan siswa sesuai dengan KKM.
5. Program tidak berhenti secara tiba-tiba ketika terjadi kesalahan input.
6. Laporan hasil analisis dapat disimpan.

## Status Pengujian

**Belum diuji.**

Pengujian akan dilakukan pada Pertemuan 15 setelah implementasi program Python
