
def validasi_nilai(nilai):
    try:
        angka = float(nilai)
        return 0 <= angka <= 100
    except (ValueError, TypeError):
        return False


def tentukan_status(nilai, kkm=75):
    if nilai >= kkm:
        return "Tuntas"
    else:
        return "Belum Tuntas"
