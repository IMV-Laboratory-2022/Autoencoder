# Flask REST API

<p align="center">
    <img src="https://miro.medium.com/max/828/1*FE2SydD7QgbvNqtKT7WVSA.gif"  width="640" style="vertical-align:middle">
</p>

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) [API](https://en.wikipedia.org/wiki/API)s biasanya digunakan untuk mengekspos model Machine Learning (ML) ke layanan lain.
Folder ini berisi contoh REST API yang dibuat menggunakan Flask untuk mengekspos model autoendoer dari tensorflow.

## Requirements
 
"Requirements File" adalah file yang mencantumkan library yang akan diinstal. Instal dengan:

```shell
$ pip install -r requirements.txt
```

## Run

Jalankan REST API menggunakan perintah:

```shell
$ python restapi.py
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

Anda dapat mendemonstrasikan di [POSTMAN](https://www.postman.com/) untuk mendapatkan respons dari REST API
