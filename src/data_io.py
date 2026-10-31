
from utilitas import validasi_nilai


def baca_data(nama_file):
    data_siswa = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(f"Baris {nomor}: format tidak valid")
                    continue

                nama = bagian[0].strip()
                nilai_teks = bagian[1].strip()

                if not nama or not validasi_nilai(nilai_teks):
                    print(f"Baris {nomor}: data tidak valid")
                    continue

                data_siswa.append({
                    "nama": nama,
                    "nilai": float(nilai_teks)
                })

    except FileNotFoundError:
        print("Error: File data tidak ditemukan.")
    except OSError as error:
        print(f"Error membaca file: {error}")

    return data_siswa


def simpan_laporan(nama_file, isi_laporan):
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write(isi_laporan)

        print(f"\nLaporan berhasil disimpan ke {nama_file}")

    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
