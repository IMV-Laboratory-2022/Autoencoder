<h1 align="center"> Autoencoder </h1>

<p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" style="vertical-align:middle">
    <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" style="vertical-align:middle">
    <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white" style="vertical-align:middle">
</p>

----

# Pengantar Autoencoder

<p align="center">
    <img src="contents/Auto Encoder.png"  width="360" style="vertical-align:middle">
</p>

- Autoencoder adalah model neural network yang memiliki input dan output yang sama.
- Autoencoder digunakan untuk mengurangi dimensi dari features (Dimensionality Reduction).

# Implementasi Autoencoder

1. Image Colorization

<p align="center">
    <img src="contents/Image Colorization.png"  width="360" style="vertical-align:middle">
</p>

2. Image Denoising

<p align="center">
    <img src="contents/Image Denoising.png"  width="360" style="vertical-align:middle">
</p>

3. Image Compression

<p align="center">
    <img src="contents/Image Compression.png"  width="360" style="vertical-align:middle">
</p>

4. Super Resolution

<p align="center">
    <img src="contents/Super Resolution.png"  width="360" style="vertical-align:middle">
</p>

5. Shadow Removal 

<p align="center">
    <img src="contents/Shadow Removal.png"  width="360" style="vertical-align:middle">
</p>

# Arsitektur Autoencoder (U-Net)

<p align="center">
    <img src="contents/U-NET.png"  width="840" style="vertical-align:middle">
</p>

UNET adalah arsitektur jaringan encoder-decoder berbentuk U, yang terdiri dari empat blok encoder dan empat blok decoder yang dihubungkan melalui sebuah jembatan (bridge).

1. Encoder
   Jaringan Encoder terdiri dari beberapa layer sebagai berikut.
   - Convolution (Conv2D): ektraksi ciri (feature extraction).
   - Batch Normalization: mengurangi pergeseran kovarian atau menyamakan distribusi setiap nilai input yang selalau berubah karena perubahan pada layer sebelumnya selama proses training.
   - Max Pooling: mengurangi dimensi (downsampling).
   
   Fungsi aktivasi ReLU (non-linearitas) membantu dalam generalisasi yang lebih baik dari data pelatihan. Karena membuat pembatas pada bilangan nol, artinya apabila x ≤ 0 maka x = 0 dan apabila x > 0 maka x = x.
   
   ```
   def encoder_block(input, num_filters):
      x = layers.Conv2D(num_filters, 3, padding='same')(input)
      bn = layers.BatchNormalization()(x)
      relu = layers.Activation('relu')(bn)

      x = layers.Conv2D(num_filters, 3, padding='same')(relu)
      bn = layers.BatchNormalization()(x)
      relu = layers.Activation('relu')(bn)

      p = layers.MaxPool2D(2, 2)(relu)

      return x, p
   ```
   

2. Bridge (Convolutional Block)
   Jembatan menghubungkan encoder dan jaringan decoder dan melengkapi aliran informasi.
   ```
   def conv_block(input, num_filters):
      x = layers.Conv2D(num_filters, 3, padding='same')(input)
      bn = layers.BatchNormalization()(x)
      relu = layers.Activation('relu')(bn)

      return relu
   ```

3. Decoder
   Jaringan Decoder terdiri dari beberapa layer sebagai berikut.
   - Up Sampling: menambah dimensi.
   - Concatenate: menggabungkan 2 array (tensor).
   
   Skip connection / skip feature memberikan informasi tambahan yang membantu dekoder menghasilkan fitur output yang lebih baik. Skip connection / skip feature bertindak sebaagai koneksi jalan pintas yang membantu aliran gradien yang lebih baik saat back propagation, yang pada gilirannya membantu jaringan untuk mempelajari representasi yang lebih baik.
   
   ```
   def decoder_block(input, skip_features, num_filters):
      u = layers.UpSampling2D(size=(2, 2))(input)

      c = layers.Concatenate()([skip_features, u])
      bn = layers.BatchNormalization()(c)
      relu = layers.Activation('relu')(bn)

      y = layers.Conv2D(num_filters, 3, padding='same')(relu)
      bn = layers.BatchNormalization()(y)
      relu = layers.Activation('relu')(bn)

      return relu
   ```

4. Output

   Output dari decoder terakhir melewati konvolusi 1x1 dengan aktivasi sigmoid. Fungsi aktivasi sigmoid memberikan topeng segmentasi yang mewakili klasifikasi berdasarkan piksel.
   ```
   layers.Conv2D(3, 1, activation='sigmoid', padding='same')
   ```

# Evaluasi Model Autoencoder
Pada Autoencoder terdapat beberapa metrik yang dijadikan sebagai parameter dalam evaluasi sebuah model sebagai berikut.

- PSNR (Peak Signal-to-Noise Ratio)
  
  PSNR digunakan untuk memeriksa kesamaan atau perbedaan dua gambar.
  
  ```
  def psnr(pred, gt):
    return tf.image.psnr(pred, gt, max_val=1.0)
  ```

- SSIM
  
  SSISM digunakan untuk menilai kualitas gambar dari visibilitas kesalahan hingga kesamaan struktural.(Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004))
  
   ```
   def ssim(pred, gt):
     return tf.image.ssim(pred, gt, max_val=1.0)
   ```


---
Referensi:
- https://github.com/aayush9753/ColorIt
- https://medium.com/geekculture/u-net-implementation-from-scratch-using-tensorflow-b4342266e406
- https://colab.research.google.com/drive/1JwPCesJ2J6_QRai99_uDwH0qlHnwEo0U?usp=sharing
- https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-build-a-u-net-for-image-segmentation-with-tensorflow-and-keras.md
- https://idiotdeveloper.com/unet-implementation-in-tensorflow-using-keras-api/
- https://idiotdeveloper.com/what-is-unet/
- http://amroamroamro.github.io/mexopencv/opencv/image_similarity_demo.html
- https://www.tensorflow.org/api_docs/python/tf/image/psnr
- https://www.tensorflow.org/api_docs/python/tf/image/ssim
