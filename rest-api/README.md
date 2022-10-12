# Flask REST API

<p align="center">
    <img src="https://miro.medium.com/max/828/1*FE2SydD7QgbvNqtKT7WVSA.gif"  width="640" style="vertical-align:middle">
</p>

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) [API](https://en.wikipedia.org/wiki/API)s biasanya digunakan untuk mengekspos model Machine Learning (ML) ke layanan lain.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/', , methods=['GET', 'POST']) # endpoint("/"), HTTP Methods (GET, POST, PUT, DELETE)
def function(): # fungsi tertentu yang akan menangani logika untuk URL tersebut


    return value # mengembalikan nilai

if __name__ == '__main__':
    app.run(debug=True)
```

Anatomi utama di balik REST API terdiri dari tiga item utama:
1.  URL & endpoint
    <p align="center">
        <img src="https://user-images.githubusercontent.com/72246401/195246966-108afbe2-7474-4fa5-b541-3e5e26ec269f.png" width="540" style="vertical-align:middle">
    </p>
    
2.  HTTP Method
    <p align="center">
        <img src="https://user-images.githubusercontent.com/72246401/195247195-a0f66bfa-2ad6-4c1f-8fe4-5eed97aa4643.png" width="540" style="vertical-align:middle">
    </p>
    
    <ol type="a">
    <li>GET Request adalah jenis permintaan yang paling umum digunakan untuk `mengambil` data dari server atau database.</li>
    <li>POST Request digunakan untuk mengirim data ke API untuk `membuat` entri.</li>
    <li>PUT Request digunakan untuk mengirim data ke API untuk `memperbarui` entri, namun bersifat idempoten artinya penerapan metode ini beberapa kali dapat dilakukan tanpa mengubah hasil akhir.</li>
    <li>DELETE Request digunakan untuk `menghapus` entri tertentu dalam database.</li>
    </ol>
    
3.  Data

Kemudian terdapat [kode status HTTP](https://flask-api.github.io/flask-api/api-guide/status-codes/). Kode status HTTP yang digunakan pada pelatihan sebagai berikut.
1. 201 → kode status yang mengindikasikan `sukses` di PUT atau POST. Objek berhasil *dibuat* atau *diperbarui*.
2. 400 → kode status yang mengindikasikan adanya `kesalahan` dalam `URI permintaan, header, atau isi`. Badan respons akan berisi pesan kesalahan yang menjelaskan apa masalah spesifiknya.
3. 500 → kode status yang mengindikasikan adanya `masalah yang belum diketahui penyebabnya` pada server website.

Folder ini berisi contoh REST API yang dibuat menggunakan Flask untuk mengekspos model autoendoer dari tensorflow.

## Requirements
 
"Requirements File" adalah file yang mencantumkan library yang akan diinstal. Instal dengan:

```shell
pip install -r requirements.txt
```

## Run

Jalankan REST API menggunakan perintah:

```shell
python restapi.py
```

## REST API
- method: `POST`
- endpoint: `/predict`
- body request:
```JSON
{
    "image" : "black_white.jpg"
}
```
- body response:
```JSON
{
    "predict_image": "92d6b611-01cd-4513-a4fb-14085d024c3b.png"
}
```

Anda dapat mendemonstrasikan di [POSTMAN](https://www.postman.com/) untuk mendapatkan respons dari REST API.

# POSTMAN

<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195249800-77a2bedf-6be6-4b8b-861f-526d9dd1f052.png"  width="640" style="vertical-align:middle">
</p>

[Postman](https://www.postman.com/) adalah alat yang dapat digunakan untuk Pengujian API. Apabila Anda ingin mendownload Postman dapat [disini](https://www.postman.com/downloads/). Kita akan belajar bagaimana melakukan Pengujian API sederhana menggunakan Postman.

1. Klik pada simbol + untuk membuat `collection` untuk API.
<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195251076-18703a40-88a5-4c2c-9848-88154836e72f.png"  width="640" style="vertical-align:middle">
</p>

2. Klik pada simbol + untuk membuka tab baru.
<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195251720-ed372a9f-e73e-4bf0-a296-bc7a45c408af.png"  width="640" style="vertical-align:middle">
</p>

3. Pilih metode POST.
<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195251918-95b96d35-9676-44a8-8e40-e8d326fd7f40.png"  width="640" style="vertical-align:middle">
</p>

4. Masukkan API Endpoint (http://127.0.0.1:5000/predict) di "Enter request URL".
<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195252536-e2f4911b-ad5a-43ca-99f3-3dc39c16d899.png"  width="640" style="vertical-align:middle">
</p>

5. Kemudian pilih `body`, `raw`, dan `JSON`. Setelah itu ketikan body request.
<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195253958-4081c1bb-9753-457f-8c58-9ca8c191815e.png"  width="640" style="vertical-align:middle">
</p>

6. Kemudian klik `send`.
<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195254111-0888f246-6c77-43e8-8f95-d19095f04dc7.png"  width="640" style="vertical-align:middle">
</p>

7. Seperti yang Anda lihat pada gambar di bawah, status 201 diterima yang menyiratkan bahwa permintaan berhasil dan sumber daya telah dibuat. Informasi lebih lanjut terkait dengan panggilan API dapat ditemukan di bawah "Header".
<p align="center">
    <img src="https://user-images.githubusercontent.com/72246401/195254450-9eae9ed0-6df2-4fb9-b80a-9df3debd73ac.png"  width="640" style="vertical-align:middle">
</p>
