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

   | Convolution (Conv2D) | Max Pooling |
   | ---                  | ---         |
   |<img src="contents/Conv Block.png">|<img src="contents/Max Pool.png">|
   
   Jaringan Encoder terdiri dari beberapa layer sebagai berikut.
   - Convolution (Conv2D): ektraksi ciri (feature extraction).
     ```
     layers.Conv2D(num_filters, kernel_size, padding)
     ```
   - Batch Normalization: mengurangi pergeseran kovarian atau menyamakan distribusi setiap nilai input yang selalau berubah karena perubahan pada layer sebelumnya selama proses training.
     ```
     layers.BatchNormalization()
     ```
   - Max Pooling: mengurangi dimensi (downsampling).
     ```
     layers.MaxPool2D(strides)
     ```
     
   Fungsi aktivasi ReLU (non-linearitas) membantu dalam generalisasi yang lebih baik dari data pelatihan. Karena membuat pembatas pada bilangan nol, artinya apabila x ≤ 0 maka x = 0 dan apabila x > 0 maka x = x.
   
   <p align="center">
     <img src="contents/Relu.png"  width="256" style="vertical-align:middle">
   </p>
   
   ```
   layers.Activation('relu')
   ```
   
   Dibawah ini merupakan blok encoder.
   
   ```
   def encoder_block(input, num_filters):
      x = layers.Conv2D(num_filters, 3, padding='same')(input)
      x = layers.BatchNormalization()(x)
      x = layers.Activation('relu')(x)

      x = layers.Conv2D(num_filters, 3, padding='same')(x)
      x = layers.BatchNormalization()(x)
      x = layers.Activation('relu')(x)

      p = layers.MaxPool2D(2, 2)(x)

      return x, p
   ```
   

2. Bridge
   <p align="center">
    <img src="contents/Bridge.png"  width="256" style="vertical-align:middle">
   </p>

   Jembatan menghubungkan encoder dan jaringan decoder dan melengkapi aliran informasi.
   
   Dibawah ini merupakan bridge.
   
   ```
   def conv_block(input, num_filters):
      x = layers.Conv2D(num_filters, 3, padding='same')(input)
      x = layers.BatchNormalization()(x)
      x = layers.Activation('relu')(x)

      return x
   ```

3. Decoder

   | Conv2DTranspose | Concatenate |
   | ---                  | ---         |
   |<img src="contents/Up Conv.png">|<img src="contents/Concatenate.png">|

   Jaringan Decoder terdiri dari beberapa layer sebagai berikut.
   - Conv2DTranspose: menambah dimensi (up sampling) dan konvolusi.
     ```
     layers.Conv2DTranspose(num_filters, kernel_size, strides, padding)
     ```
   - Concatenate: menggabungkan 2 array (tensor).
     ```
     layers.Concatenate()([skip_features, upconv])
     ```
   
   Skip connection / skip feature memberikan informasi tambahan yang membantu dekoder menghasilkan fitur output yang lebih baik. Skip connection / skip feature bertindak sebaagai koneksi jalan pintas yang membantu aliran gradien yang lebih baik saat back propagation, yang pada gilirannya membantu jaringan untuk mempelajari representasi yang lebih baik.
   
   Dibawah ini merupakan blok decoder.
   
   ```
   def decoder_block(input, skip_features, num_filters):
      upconv = layers.Conv2DTranspose(num_filters, 3, strides=(2, 2), padding="same")(input)
      upconv = layers.BatchNormalization()(upconv)
      upconv = layers.Activation('relu')(upconv)

      c = layers.Concatenate()([skip_features, upconv])

      y = layers.Conv2D(num_filters, 3, padding='same')(c)
      y = layers.BatchNormalization()(y)
      y = layers.Activation('relu')(y)
      
      y = layers.Conv2D(num_filters, 3, padding='same')(y)
      y = layers.BatchNormalization()(y)
      y = layers.Activation('relu')(y)

      return relu
   ```

4. Output

   <p align="center">
    <img src="contents/Conv 1x1.png"  width="256" style="vertical-align:middle">
   </p>
   
   Output dari decoder terakhir melewati konvolusi 1x1 dengan aktivasi sigmoid. Fungsi aktivasi sigmoid memberikan topeng segmentasi yang mewakili klasifikasi berdasarkan piksel.
   
   ```
   layers.Conv2D(num_filter/channels, kernel_size, activation='sigmoid', padding='same')
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
- https://colab.research.google.com/drive/1_X3bvVTqXenRf-7Uz6lLxc3dOuDmxzd7?usp=sharing
- https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-build-a-u-net-for-image-segmentation-with-tensorflow-and-keras.md
- https://idiotdeveloper.com/unet-implementation-in-tensorflow-using-keras-api/
- https://idiotdeveloper.com/what-is-unet/
- http://amroamroamro.github.io/mexopencv/opencv/image_similarity_demo.html
- https://www.tensorflow.org/api_docs/python/tf/image/psnr
- https://www.tensorflow.org/api_docs/python/tf/image/ssim
