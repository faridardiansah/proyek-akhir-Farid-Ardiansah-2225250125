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

## Hasil Pengujian Pertemuan 15

Pengujian dilakukan untuk memastikan program dapat memproses data nilai matematika dengan benar serta menangani input yang tidak valid.

| ID | Pengujian | Hasil | Status |
|---|---|---|---|
| TC01 | Data 10 siswa | Rata-rata 77,50 sesuai perhitungan | PASS |
| TC04 | Nilai 105 | Data ditolak, 10 siswa valid tetap diproses | PASS |

## Catatan Debugging

Pada saat implementasi ditemukan kesalahan `ImportError` karena fungsi `baca_data` tidak dapat diimpor dari modul `data_io.py`.

Perbaikan dilakukan dengan memeriksa dan melengkapi fungsi `baca_data` pada file `data_io.py`.

Setelah diperbaiki, program berhasil dijalankan dan laporan disimpan ke `output/hasil_rekap.txt`.

## Pengujian Lanjutan

Test case TC02, TC03, TC05, TC06, TC07, dan TC08 masih perlu diuji untuk memastikan seluruh kondisi normal, batas, dan invalid dapat ditangani dengan baik.


| TC02 | Nilai 0 | Diterima sebagai nilai valid | PASS |
| TC03 | Nilai 100 | Diterima sebagai nilai valid | PASS |


| TC07 | Input nilai abc | Data tidak valid ditolak | PASS |

| TC05 | File tidak ditemukan | Pesan kesalahan ditampilkan tanpa program crash | PASS |

| TC06 | Semua nilai memenuhi KKM | 5 siswa tuntas, 0 belum tuntas | PASS |
