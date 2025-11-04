# 📋 Aplikasi Rekap Absensi (Attandance Record)

Aplikasi ini dibuat oleh 👨‍💻 **Frendy Rikal Gerung (NIM: 20210118)** sebagai bagian dari program Magang/Praktik Kerja dari Program Studi Teknik Informatika, Fakultas Teknik, 🎓 **Universitas Negeri Manado (UNIMA)**.

Aplikasi ini dikembangkan selama periode magang di 🏛️ **Dinas Pendidikan dan Kebudayaan Kabupaten Minahasa** pada tahun 2023.

## 🧐 Latar Belakang Masalah

Di Dinas Pendidikan Kabupaten Minahasa, khususnya di bidang ketenagaan, proses rekapitulasi absensi harian untuk SD, SMP, dan SMA masih dilakukan secara manual. Data absensi yang diisi oleh kepala sekolah atau pengawas melalui Google Form ditampung dalam sebuah file mentah (Excel).

Proses rekap manual ini memakan waktu yang sangat lama dan tidak efisien. Masalah utamanya adalah banyaknya **kesalahan penulisan nama sekolah** (inkonsistensi data), yang membuat penyusunan absensi menjadi lebih rumit dan rentan kesalahan.

## 💡 Solusi

Aplikasi ini dirancang untuk mengotomatisasi seluruh alur kerja rekapitulasi absensi. Aplikasi ini berfungsi untuk:
1.  **Membersihkan (Classify)** data mentah.
2.  **Memvalidasi (Repair)** nama sekolah yang salah ketik menggunakan *fuzzy logic*.
3.  **Menghasilkan (Generate)** laporan rekapitulasi akhir bulanan dalam format Excel yang rapi dan visual.

Tujuannya adalah untuk **meningkatkan efisiensi dan ketepatan data** secara signifikan.

---

## ✨ Fitur Utama

Aplikasi ini memiliki dua modul utama yang ditampilkan dalam tab: `Data Clasify` dan `Data Generate`.

### 1. 🗂️ Tab "Data Clasify" (Klasifikasi & Perbaikan Data)

Ini adalah modul utama untuk membersihkan dan memperbaiki data mentah.

* **Impor Data**: Memuat file absensi mentah (`.xlsx`) dan file master daftar nama sekolah (`.txt`).
* **Klasifikasi Otomatis**: Saat pengguna memilih bulan dan tanggal, aplikasi akan secara otomatis memproses data.
* **Pencocokan Cerdas (Fuzzy Logic)**: Menggunakan *library* `fuzzywuzzy`, aplikasi akan membandingkan nama sekolah di file absensi dengan daftar nama sekolah yang benar. Ini dapat mentolerir kesalahan ketik (misalnya, "SDN 1 Tondano" vs "SD NEGERI 1 TONDANO").
* **Pemisahan Data**: Data yang diproses akan disimpan dalam dua file terpisah di folder `Result/Data/`:
    * `[tanggal]_identify.csv`: Data yang nama sekolahnya berhasil dikenali.
    * `[tanggal]_notidentify.csv`: Data yang nama sekolahnya tidak dikenali dan perlu perbaikan manual.

### 2. 🛠️ Menu Perbaikan (Repair Menu)

Panel ini (di bagian kiri bawah tab "Data Clasify") digunakan untuk memperbaiki data yang tidak teridentifikasi.

* **Tampilan Detail**: Menampilkan data yang salah satu per satu (Nama Absen Sekolah, Kecamatan, Kepsek, dll.).
* **Rekomendasi Pencarian**: Pengguna dapat mengetik di kotak pencarian untuk mencari nama sekolah yang benar dari daftar master.
* **Perbaikan Cepat**: Pengguna dapat memilih nama yang benar dari daftar rekomendasi dan menekan tombol `Enter` untuk memperbarui data.
* **Simpan & Gabung (Merge)**: Setelah diperbaiki, pengguna dapat menyimpan perubahan dan menggabungkan file `_identify` dan `_notidentify` yang sudah diperbaiki menjadi satu file bersih di folder `Result/Fix/`.

### 3. 📊 Tab "Data Generate" (Pembuatan Laporan Excel)

Modul ini digunakan untuk membuat laporan akhir Excel dari data yang sudah bersih.

* **Koleksi Data**: Pengguna dapat menekan tombol `Tambah` untuk memilih file-file absensi harian yang sudah bersih (dari folder `Result/Fix/`) yang ingin dimasukkan ke dalam rekap bulanan.
* **Visualisasi Laporan**: Menghasilkan file Excel (`.xlsx`).
* **Kode Warna Otomatis**: Laporan Excel yang dihasilkan secara otomatis memberi warna pada sel kehadiran:
    * 🟢 **Hijau**: Absen Pagi
    * 🔵 **Biru**: Absen Sore
    * 🔴 **Merah/Oranye**: Tidak Hadir / Absen

---

## 🚀 Alur Kerja Penggunaan

1.  Jalankan `main.py`.
2.  Pastikan folder `Result/Data/` dan `Result/Fix/` ada.
3.  **Langkah 1 (Satu kali)**: Buka menu `File` > `Open Sekolah`. Pilih file `.txt` yang berisi daftar master semua nama sekolah.
4.  **Langkah 2**: Buka menu `File` > `Open Attendance`. Pilih file absensi mentah `.xlsx` yang diunduh dari Google Form.
5.  **Langkah 3 (Tab Data Clasify)**:
    * Pilih bulan di *listbox* kiri (misal: "April").
    * Pilih tanggal di *listbox* tengah (misal: "17 Senin").
    * Tekan tombol `Enter` pada keyboard.
    * Aplikasi akan membuat file di `Result/Data/` dan menampilkannya di *listbox* kanan atas.
6.  **Langkah 4 (Perbaikan)**:
    * Klik pada file `_notidentify.csv` di *listbox* kanan atas.
    * Panel "Repair Menu" di kiri bawah akan aktif.
    * Gunakan tombol panah `Kiri`/`Kanan` pada keyboard untuk menavigasi data yang salah.
    * Ketik nama sekolah yang benar di kotak pencarian.
    * Klik nama yang benar di *listbox* rekomendasi di bawahnya.
    * Tekan `Enter` untuk menyimpan perubahan data tersebut.
7.  **Langkah 5 (Simpan & Gabung)**:
    * Setelah semua data diperbaiki, klik kanan di area panel perbaikan.
    * Pilih `Save` untuk menyimpan perubahan.
    * Klik kanan lagi, pilih `Merge` untuk menggabungkan data ke dalam satu file bersih di folder `Result/Fix/`.
8.  **Langkah 6 (Tab Data Generate)**:
    * Pindah ke tab `Data Generate`.
    * Klik tombol `Tambah`. Pilih semua file `.csv` dari folder `Result/Fix/` yang ingin Anda rekap.
    * File akan muncul sebagai *card* di dalam tab.
    * Klik kanan di mana saja di dalam tab, pilih `Generate`.
    * Simpan file Excel (`.xlsx`) Anda. Laporan akhir yang sudah diwarnai berhasil dibuat.

## 💻 Teknologi yang Digunakan

* **Bahasa**: Python 3
* **Antarmuka (GUI)**: Tkinter
* **Pembacaan/Penulisan Excel**: Openpyxl
* **Pencocokan Nama**: Fuzzywuzzy
* **Kalender/Tanggal**: Tkcalendar

## 🔧 Instalasi & Kebutuhan

Pastikan Anda memiliki Python 3 dan `pip` terinstal.

1.  **Instalasi Tkinter (jika belum ada, khusus Linux):**
    ```bash
    sudo apt-get update
    sudo apt-get install python3-tk
    ```

2.  **Instalasi Library Python:**
    ```bash
    pip install openpyxl fuzzywuzzy python-Levenshtein tkcalendar
    ```
    *(Disarankan menginstal `python-Levenshtein` untuk mempercepat proses fuzzywuzzy)*

3.  **Jalankan Aplikasi:**
    ```bash
    python3 main.py
    ```