import random
import timeit
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan array dengan elemen unik atau tidak unik
def buat_array(n, nilai_maks, seed=42):
    random.seed(seed)
    return [random.randint(1, nilai_maks) for _ in range(n)]

# Fungsi untuk memeriksa apakah semua elemen dalam array unik
def apakah_unik(array):
    return len(array) == len(set(array))

# Fungsi untuk menghitung waktu rata-rata dan terburuk menggunakan timeit
def hitung_waktu(nilai_n, nilai_maks):
    waktu_kasus_terburuk = []
    waktu_kasus_rata2 = []

    for n in nilai_n:
        array = buat_array(n, nilai_maks)

        # Mengukur waktu kasus terburuk (dengan pengecekan berulang)
        waktu_terburuk = timeit.timeit(lambda: apakah_unik(array), number=100) / 100
        waktu_kasus_terburuk.append(waktu_terburuk)

        # Mengukur waktu rata-rata (dengan eksekusi tunggal)
        waktu_rata2 = timeit.timeit(lambda: apakah_unik(array), number=50) / 50
        waktu_kasus_rata2.append(waktu_rata2)

    return waktu_kasus_terburuk, waktu_kasus_rata2

# Fungsi untuk menyimpan hasil ke file teks
def simpan_hasil_ke_file(nama_file, nilai_n, kasus_terburuk, kasus_rata2):
    try:
        with open(nama_file, "w") as file:
            file.write("n, Kasus Terburuk (s), Kasus Rata-rata (s)\n")
            for n, buruk, rata in zip(nilai_n, kasus_terburuk, kasus_rata2):
                file.write(f"{n}, {buruk:.6f}, {rata:.6f}\n")
    except IOError as e:
        print(f"Kesalahan saat menyimpan file: {e}")

# Fungsi untuk membuat plot grafik
def buat_grafik(nilai_n, kasus_terburuk, kasus_rata2, nama_file_output):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(nilai_n, kasus_terburuk, label="Kasus Terburuk", marker="o", color="red")
        plt.plot(nilai_n, kasus_rata2, label="Kasus Rata-rata", marker="o", color="blue")
        plt.title("Analisis Kompleksitas Waktu")
        plt.xlabel("n (Jumlah Elemen)")
        plt.ylabel("Waktu (s)")
        plt.legend()
        plt.grid()
        plt.savefig(nama_file_output)
        plt.show()
    except Exception as e:
        print(f"Kesalahan saat membuat grafik: {e}")

if __name__ == "__main__":
    try:
        # Masukkan digit terakhir stambuk
        tiga_digit_terakhir_stambuk = int(input("Masukkan 3 digit terakhir stambuk Anda: "))
        nilai_maks = 250 - tiga_digit_terakhir_stambuk

        if nilai_maks <= 0:
            raise ValueError("Nilai maksimum dari stambuk harus lebih besar dari 0.")

        # Nilai n untuk pengujian
        nilai_n = [100, 150, 200, 250, 300, 350, 400, 500]

        # Hitung waktu untuk kasus terburuk dan rata-rata
        kasus_terburuk, kasus_rata2 = hitung_waktu(nilai_n, nilai_maks)

        # Simpan hasil ke file teks
        simpan_hasil_ke_file("worst_avg.txt", nilai_n, kasus_terburuk, kasus_rata2)

        # Buat dan simpan grafik
        buat_grafik(nilai_n, kasus_terburuk, kasus_rata2, "time_complexity_analysis.jpg")

        print("Program selesai dijalankan. Periksa 'worst_avg.txt' dan 'time_complexity_analysis.jpg'.")
    except ValueError as ve:
        print(f"Input tidak valid: {ve}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
