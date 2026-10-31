
from pathlib import Path

from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik, hitung_ketuntasan
from utilitas import tentukan_status


def main():
    kkm = 75

    folder_proyek = Path(__file__).resolve().parent.parent
    file_data = folder_proyek / "data" / "nilai_contoh.txt"
    file_laporan = folder_proyek / "output" / "hasil_rekap.txt"

    print("====================================")
    print(" PROGRAM ANALISIS NILAI MATEMATIKA")
    print("====================================")

    data_siswa = baca_data(file_data)

    if not data_siswa:
        print("Tidak ada data siswa valid untuk dianalisis.")
        return

    statistik = hitung_statistik(data_siswa)
    ketuntasan = hitung_ketuntasan(data_siswa, kkm)

    laporan = []
    laporan.append("HASIL ANALISIS NILAI MATEMATIKA")
    laporan.append("=" * 35)

    for siswa in data_siswa:
        nama = siswa["nama"]
        nilai = siswa["nilai"]
        status = tentukan_status(nilai, kkm)

        laporan.append(f"{nama}: {nilai:g} - {status}")

    laporan.append("")
    laporan.append(f"Jumlah Siswa     : {statistik['jumlah']}")
    laporan.append(f"Rata-rata Nilai  : {statistik['rata_rata']:.2f}")
    laporan.append(f"Nilai Terendah   : {statistik['minimum']:g}")
    laporan.append(f"Nilai Tertinggi  : {statistik['maksimum']:g}")
    laporan.append(f"KKM              : {kkm}")
    laporan.append(f"Jumlah Tuntas    : {ketuntasan['tuntas']}")
    laporan.append(f"Belum Tuntas     : {ketuntasan['belum_tuntas']}")

    isi_laporan = "\n".join(laporan)

    print()
    print(isi_laporan)

    file_laporan.parent.mkdir(parents=True, exist_ok=True)
    simpan_laporan(file_laporan, isi_laporan)


if __name__ == "__main__":
    main()
