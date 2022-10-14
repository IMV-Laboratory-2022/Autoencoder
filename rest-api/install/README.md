<h1 align="center"> Instalasi </h1>

Sebelum menjalankan training melalui supercomputer/google colabs, apabila ingin menjalankan model yang sudah ditraining memerlukan instalasi beberapa aplikasi dan library python.

A. Anaconda

Anaconda berfungsi membuat virtual environment untuk aplikasi yang dibuat menggunakan Python. Virtual environment ini akan menampung semua dependencies/library yang dibutuhkan pada aplikasi Python.

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195620820-5cfaa5c9-f047-4fab-91e0-7ca907020cd8.png" alt="anaconda" width="480" style="vertical-align:middle">
</p>

**Install Anaconda untuk Laptop dan PC (Windows)**

1. Download `installer Anaconda` [di sini](https://www.anaconda.com/products/distribution). Sesuaikan bit dari sistem operasi perangkat Anda (32bit atau 64bit)
2. Buka file installer yang sudah didownload, klik `Next` pada halaman awal.
3. Baca *licensing terms* dan klik `I Agree`.
4. Pilih `Just for me` pada pilihan install for, lalu klik `Next`.
5. Pilih **folder tujuan install Anaconda**, lalu klik `Next`.

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195620988-001bb0ca-5266-4ac8-a032-072dc84b217b.png" alt="anaconda set up" width="480" style="vertical-align:middle">
</p>

6. Centang `Register Anaconda3 as my default Python 3.7`, lalu klik `Install`.
7. Setelah install selesai, Anda akan diberikan saran untuk menginstall PyCharm melalui link, klik `Next` untuk tidak menginstall PyCharm.

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195621091-5f2198fa-0cce-468d-bea9-d401af688ea1.png" alt="anaconda set up" width="480" style="vertical-align:middle">
</p>

7. Install selesai, matikan centang pada 2 pilihan yang diberikan jika Anda tidak ingin diarahkan ke website **Anaconda**, lalu klik `Finish` untuk menutup installer.

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195621286-83896ebc-f3ae-4e76-a177-000611955a09.png" alt="anaconda set up" width="480" style="vertical-align:middle">
</p>

**Siapkan Virtual Environment**

1. Buka Anaconda Navigator.
2. Pilih "Environment" di sisi kiri.

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195831908-812f1240-754b-4f90-98ab-f9c428fafdd3.png" width="640" style="vertical-align:middle">
</p>

3. Pilih "Create" di bagian bawah

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195832152-82923bc4-9596-4293-9b71-ac37ebde5d9a.png" width="640" style="vertical-align:middle">
</p>

4. Dalam munculan:
   - Beri nama: autoencoder
   - Pilih python versi 3.8
   - Tekan "Create" (NB: Ini mungkin memakan waktu cukup lama karena perlu mengunduh Python)

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195832521-1899fafe-482c-433d-8338-f943fecc1f4d.png" width="640" style="vertical-align:middle">
</p>

**Memasuki Virtual Environment Anda**
Untuk memasuki virtual environment:

1. Buka Anaconda Navigator.
2. Pilih "Environment" di sisi kiri.

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195831908-812f1240-754b-4f90-98ab-f9c428fafdd3.png" width="640" style="vertical-align:middle">
</p>

3. Tekan panah ">" di sebelah environment **autoencoder** Anda dan pilih "Open Terminal"

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195833440-1204a8ae-0f9b-4d1a-8340-a68741a5dab4.png" width="640" style="vertical-align:middle">
</p>

**Terminal Environment**

1. Terdapat beberapa library python yang diperlukan seperti.
   - flask
   - tensorflow-cpu
   - numpy
   - uuid
   - os

2. Kemudian terdapat dua opsi dengan `pip install <nama-library>` atau dengan `pip install -r requirements.txt`. Untuk requirements.txt bisa di download [disini](https://github.com/IMV-Laboratory-2022/Autoencoder/blob/main/rest-api/install/requirements.txt).

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195835056-dc41c978-0271-48fa-8d2c-c6c5d250ced9.png" width="640" style="vertical-align:middle">
</p>

B. POSTMAN

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195249800-77a2bedf-6be6-4b8b-861f-526d9dd1f052.png"  width="640" style="vertical-align:middle">
</p>

[Postman](https://www.postman.com/) adalah alat yang dapat digunakan untuk Pengujian API. Apabila Anda ingin mendownload Postman dapat [disini](https://www.postman.com/downloads/).

*[Instalasi Postman di Windows](https://github.com/postmanlabs/postman-docs/blob/develop/src/pages/docs/getting-started/installation-and-updates.md)*

Postman tersedia untuk Windows 7 dan yang lebih baru.

1. [Unduh](https://www.postman.com/downloads/) versi Postman terbaru.
2. Pilih dan jalankan file .exe untuk menginstal Postman.
> Postman v9.4 adalah versi terakhir dari Postman yang mendukung Windows 32-bit dan 64-bit. Semua versi Postman setelah v9.4 hanya akan bekerja pada Windows 64-bit. Anda dapat terus menggunakan Postman v9.4 dan sebelumnya pada Windows 32-bit.
