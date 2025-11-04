# Aplikasi Rekap Absensi (Attandance Record)

[cite_start]Aplikasi ini dibuat oleh **Frendy Rikal Gerung (NIM: 20210118)** [cite: 6, 7] [cite_start]sebagai bagian dari program Magang/Praktik Kerja dari Program Studi Teknik Informatika, Fakultas Teknik, **Universitas Negeri Manado (UNIMA)**[cite: 8, 9, 10]. [cite_start]Aplikasi ini dikembangkan selama periode magang di **Dinas Pendidikan dan Kebudayaan Kabupaten Minahasa** [cite: 31, 152] [cite_start]pada tahun 2023[cite: 11].

## Latar Belakang Masalah

[cite_start]Di Dinas Pendidikan Kabupaten Minahasa, khususnya di bidang ketenagaan, proses rekapitulasi absensi harian untuk SD, SMP, dan SMA masih dilakukan secara manual[cite: 153, 154]. [cite_start]Data absensi yang diisi oleh kepala sekolah atau pengawas melalui Google Form [cite: 146, 147] [cite_start]ditampung dalam sebuah file mentah (Excel)[cite: 148].

[cite_start]Proses rekap manual ini memakan waktu yang sangat lama dan tidak efisien[cite: 150, 154]. [cite_start]Masalah utamanya adalah banyaknya kesalahan penulisan nama sekolah (inkonsistensi data), yang membuat penyusunan absensi menjadi lebih rumit dan rentan kesalahan[cite: 151].

## Solusi

Aplikasi ini dirancang untuk mengotomatisasi seluruh alur kerja rekapitulasi absensi. Aplikasi ini berfungsi untuk:
1.  **Membersihkan (Classify)** data mentah.
2.  **Memvalidasi (Repair)** nama sekolah yang salah ketik menggunakan *fuzzy logic*.
3.  **Menghasilkan (Generate)** laporan rekapitulasi akhir bulanan dalam format Excel yang rapi dan visual.

[cite_start]Tujuannya adalah untuk meningkatkan efisiensi dan ketepatan data secara signifikan[cite: 5].

## Fitur Utama

Aplikasi ini memiliki dua modul utama yang ditampilkan dalam tab: `Data Clasify` dan `Data Generate`.

### 1. Tab "Data Clasify" (Klasifikasi & Perbaikan Data)

Ini adalah modul utama untuk membersihkan dan memperbaiki data mentah.

* **Impor Data**: Memuat file absensi mentah (`.xlsx`) dan file master daftar nama sekolah (`.txt`).
* [cite_start]**Klasifikasi Otomatis**: Saat pengguna memilih bulan dan tanggal, aplikasi akan secara otomatis memproses data[cite: 278].
* **Pencocokan Cerdas (Fuzzy Logic)**: Menggunakan *library* `fuzzywuzzy`, aplikasi akan membandingkan nama sekolah di file absensi dengan daftar nama sekolah yang benar. [cite_start]Ini dapat mentolerir kesalahan ketik (misalnya, "SDN 1 Tondano" vs "SD NEGERI 1 TONDANO")[cite: 210].
* **Pemisahan Data**: Data yang diproses akan disimpan dalam dua file terpisah di folder `Result/Data/`:
    * [cite_start]`[tanggal]_identify.csv`: Data yang nama sekolahnya berhasil dikenali[cite: 411].
    * [cite_start]`[tanggal]_notidentify.csv`: Data yang nama sekolahnya tidak dikenali dan perlu perbaikan manual[cite: 411].

### 2. Menu Perbaikan (Repair Menu)

[cite_start]Panel ini (di bagian kiri bawah tab "Data Clasify") digunakan untuk memperbaiki data yang tidak teridentifikasi[cite: 387].

* [cite_start]**Tampilan Detail**: Menampilkan data yang salah satu per satu (Nama Absen Sekolah, Kecamatan, Kepsek, dll.)[cite: 389].
* [cite_start]**Rekomendasi Pencarian**: Pengguna dapat mengetik di kotak pencarian untuk mencari nama sekolah yang benar dari daftar master[cite: 389].
* [cite_start]**Perbaikan Cepat**: Pengguna dapat memilih nama yang benar dari daftar rekomendasi dan menekan tombol `Enter` untuk memperbarui data[cite: 387].
* [cite_start]**Simpan & Gabung (Merge)**: Setelah diperbaiki, pengguna dapat menyimpan perubahan dan menggabungkan file `_identify` dan `_notidentify` yang sudah diperbaiki menjadi satu file bersih di folder `Result/Fix/`[cite: 412].

### 3. Tab "Data Generate" (Pembuatan Laporan Excel)

[cite_start]Modul ini digunakan untuk membuat laporan akhir Excel dari data yang sudah bersih[cite: 413, 425].

* [cite_start]**Koleksi Data**: Pengguna dapat menekan tombol `Tambah` untuk memilih file-file absensi harian yang sudah bersih (dari folder `Result/Fix/`) yang ingin dimasukkan ke dalam rekap bulanan[cite: 425].
* [cite_start]**Visualisasi Laporan**: Menghasilkan file Excel (`.xlsx`)[cite: 312].
* [cite_start]**Kode Warna Otomatis**: Laporan Excel yang dihasilkan secara otomatis memberi warna pada sel kehadiran[cite: 465, 467]:
    * [cite_start]**Hijau**: Absen Pagi [cite: 468]
    * [cite_start]**Biru**: Absen Sore [cite: 468]
    * **Merah/Oranye**: Tidak Hadir / Absen

## Alur Kerja Penggunaan

1.  Jalankan `main.py`.
2.  Pastikan folder `Result/Data/` dan `Result/Fix/` ada.
3.  **Langkah 1 (Satu kali)**: Buka menu `File` > `Open Sekolah`. Pilih file `.txt` yang berisi daftar master semua nama sekolah.
4.  **Langkah 2**: Buka menu `File` > `Open Attendance`. Pilih file absensi mentah `.xlsx` yang diunduh dari Google Form.
5.  **Langkah 3 (Tab Data Clasify)**:
    * [cite_start]Pilih bulan di *listbox* kiri (misal: "April")[cite: 343].
    * [cite_start]Pilih tanggal di *listbox* tengah (misal: "17 Senin")[cite: 353].
    * Tekan tombol `Enter` pada keyboard.
    * [cite_start]Aplikasi akan membuat file di `Result/Data/` dan menampilkannya di *listbox* kanan atas (misal: `April_17_identify.csv` dan `April_17_notidentify.csv`)[cite: 392, 393].
6.  **Langkah 4 (Perbaikan)**:
    * Klik pada file `_notidentify.csv` di *listbox* kanan atas.
    * [cite_start]Panel "Repair Menu" di kiri bawah akan aktif[cite: 386].
    * Gunakan tombol panah `Kiri`/`Kanan` pada keyboard untuk menavigasi data yang salah.
    * Ketik nama sekolah yang benar di kotak pencarian.
    * Klik nama yang benar di *listbox* rekomendasi di bawahnya.
    * Tekan `Enter` untuk menyimpan perubahan data tersebut.
    * Ulangi untuk semua data yang salah.
7.  **Langkah 5 (Simpan & Gabung)**:
    * Setelah semua data diperbaiki, klik kanan di area panel perbaikan.
    * Pilih `Save` untuk menyimpan perubahan ke file `_notidentify.csv`.
    * [cite_start]Klik kanan lagi, pilih `Merge` untuk menggabungkan data `identify` dan `notidentify` yang sudah diperbaiki ke dalam satu file bersih di folder `Result/Fix/` (misal: `April 17.csv`)[cite: 399, 405].
8.  **Langkah 6 (Tab Data Generate)**:
    * [cite_start]Pindah ke tab `Data Generate`[cite: 413].
    * Klik tombol `Tambah`. [cite_start]Pilih semua file `.csv` dari folder `Result/Fix/` yang ingin Anda rekap (misal: `April 11.csv`, `April 12.csv`, dst.)[cite: 401, 402].
    * File akan muncul sebagai *card* di dalam tab.
    * Klik kanan di mana saja di dalam tab, pilih `Generate`.
    * Simpan file Excel (`.xlsx`) Anda. [cite_start]Laporan akhir yang sudah diwarnai berhasil dibuat[cite: 465].

## Teknologi yang Digunakan

* [cite_start]**Bahasa**: Python 3 [cite: 180]
* **Antarmuka (GUI)**: Tkinter
* **Pembacaan/Penulisan Excel**: Openpyxl
* **Pencocokan Nama**: Fuzzywuzzy
* **Kalender/Tanggal**: Tkcalendar

## Instalasi & Kebutuhan

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
    ```# Aplikasi Rekap Absensi (Attandance Record)

[cite_start]Aplikasi ini dibuat oleh **Frendy Rikal Gerung (NIM: 20210118)** [cite: 6, 7] [cite_start]sebagai bagian dari program Magang/Praktik Kerja dari Program Studi Teknik Informatika, Fakultas Teknik, **Universitas Negeri Manado (UNIMA)**[cite: 8, 9, 10]. [cite_start]Aplikasi ini dikembangkan selama periode magang di **Dinas Pendidikan dan Kebudayaan Kabupaten Minahasa** [cite: 31, 152] [cite_start]pada tahun 2023[cite: 11].

## Latar Belakang Masalah

[cite_start]Di Dinas Pendidikan Kabupaten Minahasa, khususnya di bidang ketenagaan, proses rekapitulasi absensi harian untuk SD, SMP, dan SMA masih dilakukan secara manual[cite: 153, 154]. [cite_start]Data absensi yang diisi oleh kepala sekolah atau pengawas melalui Google Form [cite: 146, 147] [cite_start]ditampung dalam sebuah file mentah (Excel)[cite: 148].

[cite_start]Proses rekap manual ini memakan waktu yang sangat lama dan tidak efisien[cite: 150, 154]. [cite_start]Masalah utamanya adalah banyaknya kesalahan penulisan nama sekolah (inkonsistensi data), yang membuat penyusunan absensi menjadi lebih rumit dan rentan kesalahan[cite: 151].

## Solusi

Aplikasi ini dirancang untuk mengotomatisasi seluruh alur kerja rekapitulasi absensi. Aplikasi ini berfungsi untuk:
1.  **Membersihkan (Classify)** data mentah.
2.  **Memvalidasi (Repair)** nama sekolah yang salah ketik menggunakan *fuzzy logic*.
3.  **Menghasilkan (Generate)** laporan rekapitulasi akhir bulanan dalam format Excel yang rapi dan visual.

[cite_start]Tujuannya adalah untuk meningkatkan efisiensi dan ketepatan data secara signifikan[cite: 5].

## Fitur Utama

Aplikasi ini memiliki dua modul utama yang ditampilkan dalam tab: `Data Clasify` dan `Data Generate`.

### 1. Tab "Data Clasify" (Klasifikasi & Perbaikan Data)

Ini adalah modul utama untuk membersihkan dan memperbaiki data mentah.

* **Impor Data**: Memuat file absensi mentah (`.xlsx`) dan file master daftar nama sekolah (`.txt`).
* [cite_start]**Klasifikasi Otomatis**: Saat pengguna memilih bulan dan tanggal, aplikasi akan secara otomatis memproses data[cite: 278].
* **Pencocokan Cerdas (Fuzzy Logic)**: Menggunakan *library* `fuzzywuzzy`, aplikasi akan membandingkan nama sekolah di file absensi dengan daftar nama sekolah yang benar. [cite_start]Ini dapat mentolerir kesalahan ketik (misalnya, "SDN 1 Tondano" vs "SD NEGERI 1 TONDANO")[cite: 210].
* **Pemisahan Data**: Data yang diproses akan disimpan dalam dua file terpisah di folder `Result/Data/`:
    * [cite_start]`[tanggal]_identify.csv`: Data yang nama sekolahnya berhasil dikenali[cite: 411].
    * [cite_start]`[tanggal]_notidentify.csv`: Data yang nama sekolahnya tidak dikenali dan perlu perbaikan manual[cite: 411].

### 2. Menu Perbaikan (Repair Menu)

[cite_start]Panel ini (di bagian kiri bawah tab "Data Clasify") digunakan untuk memperbaiki data yang tidak teridentifikasi[cite: 387].

* [cite_start]**Tampilan Detail**: Menampilkan data yang salah satu per satu (Nama Absen Sekolah, Kecamatan, Kepsek, dll.)[cite: 389].
* [cite_start]**Rekomendasi Pencarian**: Pengguna dapat mengetik di kotak pencarian untuk mencari nama sekolah yang benar dari daftar master[cite: 389].
* [cite_start]**Perbaikan Cepat**: Pengguna dapat memilih nama yang benar dari daftar rekomendasi dan menekan tombol `Enter` untuk memperbarui data[cite: 387].
* [cite_start]**Simpan & Gabung (Merge)**: Setelah diperbaiki, pengguna dapat menyimpan perubahan dan menggabungkan file `_identify` dan `_notidentify` yang sudah diperbaiki menjadi satu file bersih di folder `Result/Fix/`[cite: 412].

### 3. Tab "Data Generate" (Pembuatan Laporan Excel)

[cite_start]Modul ini digunakan untuk membuat laporan akhir Excel dari data yang sudah bersih[cite: 413, 425].

* [cite_start]**Koleksi Data**: Pengguna dapat menekan tombol `Tambah` untuk memilih file-file absensi harian yang sudah bersih (dari folder `Result/Fix/`) yang ingin dimasukkan ke dalam rekap bulanan[cite: 425].
* [cite_start]**Visualisasi Laporan**: Menghasilkan file Excel (`.xlsx`)[cite: 312].
* [cite_start]**Kode Warna Otomatis**: Laporan Excel yang dihasilkan secara otomatis memberi warna pada sel kehadiran[cite: 465, 467]:
    * [cite_start]**Hijau**: Absen Pagi [cite: 468]
    * [cite_start]**Biru**: Absen Sore [cite: 468]
    * **Merah/Oranye**: Tidak Hadir / Absen

## Alur Kerja Penggunaan

1.  Jalankan `main.py`.
2.  Pastikan folder `Result/Data/` dan `Result/Fix/` ada.
3.  **Langkah 1 (Satu kali)**: Buka menu `File` > `Open Sekolah`. Pilih file `.txt` yang berisi daftar master semua nama sekolah.
4.  **Langkah 2**: Buka menu `File` > `Open Attendance`. Pilih file absensi mentah `.xlsx` yang diunduh dari Google Form.
5.  **Langkah 3 (Tab Data Clasify)**:
    * [cite_start]Pilih bulan di *listbox* kiri (misal: "April")[cite: 343].
    * [cite_start]Pilih tanggal di *listbox* tengah (misal: "17 Senin")[cite: 353].
    * Tekan tombol `Enter` pada keyboard.
    * [cite_start]Aplikasi akan membuat file di `Result/Data/` dan menampilkannya di *listbox* kanan atas (misal: `April_17_identify.csv` dan `April_17_notidentify.csv`)[cite: 392, 393].
6.  **Langkah 4 (Perbaikan)**:
    * Klik pada file `_notidentify.csv` di *listbox* kanan atas.
    * [cite_start]Panel "Repair Menu" di kiri bawah akan aktif[cite: 386].
    * Gunakan tombol panah `Kiri`/`Kanan` pada keyboard untuk menavigasi data yang salah.
    * Ketik nama sekolah yang benar di kotak pencarian.
    * Klik nama yang benar di *listbox* rekomendasi di bawahnya.
    * Tekan `Enter` untuk menyimpan perubahan data tersebut.
    * Ulangi untuk semua data yang salah.
7.  **Langkah 5 (Simpan & Gabung)**:
    * Setelah semua data diperbaiki, klik kanan di area panel perbaikan.
    * Pilih `Save` untuk menyimpan perubahan ke file `_notidentify.csv`.
    * [cite_start]Klik kanan lagi, pilih `Merge` untuk menggabungkan data `identify` dan `notidentify` yang sudah diperbaiki ke dalam satu file bersih di folder `Result/Fix/` (misal: `April 17.csv`)[cite: 399, 405].
8.  **Langkah 6 (Tab Data Generate)**:
    * [cite_start]Pindah ke tab `Data Generate`[cite: 413].
    * Klik tombol `Tambah`. [cite_start]Pilih semua file `.csv` dari folder `Result/Fix/` yang ingin Anda rekap (misal: `April 11.csv`, `April 12.csv`, dst.)[cite: 401, 402].
    * File akan muncul sebagai *card* di dalam tab.
    * Klik kanan di mana saja di dalam tab, pilih `Generate`.
    * Simpan file Excel (`.xlsx`) Anda. [cite_start]Laporan akhir yang sudah diwarnai berhasil dibuat[cite: 465].

## Teknologi yang Digunakan

* [cite_start]**Bahasa**: Python 3 [cite: 180]
* **Antarmuka (GUI)**: Tkinter
* **Pembacaan/Penulisan Excel**: Openpyxl
* **Pencocokan Nama**: Fuzzywuzzy
* **Kalender/Tanggal**: Tkcalendar

## Instalasi & Kebutuhan

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