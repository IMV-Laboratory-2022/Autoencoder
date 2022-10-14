<h1 align="center"> Instalasi </h1>

Sebelum menjalankan training melalui supercomputer/google colabs, apabila ingin menjalankan model yang sudah ditraining memerlukan instalasi beberapa aplikasi dan library python.

1. Anaconda

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

3. Pilih "Create" di bagian bawah
4. Dalam munculan:
   - Beri nama: autoencoder
   - Pilih python versi 3.8
   - Tekan "Create" (NB: Ini mungkin memakan waktu cukup lama karena perlu mengunduh Python)

```python
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```

2. POSTMAN

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195249800-77a2bedf-6be6-4b8b-861f-526d9dd1f052.png"  width="640" style="vertical-align:middle">
</p>

[Postman](https://www.postman.com/) adalah alat yang dapat digunakan untuk Pengujian API. Apabila Anda ingin mendownload Postman dapat [disini](https://www.postman.com/downloads/).
