
def hitung_statistik(data_siswa):
    if not data_siswa:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": 0,
            "maksimum": 0
        }

    daftar_nilai = [siswa["nilai"] for siswa in data_siswa]

    return {
        "jumlah": len(daftar_nilai),
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai)
    }


def hitung_ketuntasan(data_siswa, kkm=75):
    jumlah_tuntas = 0

    for siswa in data_siswa:
        if siswa["nilai"] >= kkm:
            jumlah_tuntas += 1

    return {
        "tuntas": jumlah_tuntas,
        "belum_tuntas": len(data_siswa) - jumlah_tuntas
    }
