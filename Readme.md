# PacmanEatingSomeColor - Python Uygulaması

## Herkese Selamlar

Bu proje, Python ile kodlanmış bir görüntü işleme uygulamasıdır. 

Bu projeyi yapmamdaki amaç; OpenCV kütüphanesini kullanarak laptop kamerasından alınan canlı görüntüye farklı bir görüntü ekleyerek ana görüntü üzerinde değişiklikler yapmak ve bu süreç içerisinde yaşanabilecek sorunları görmekti.

Canlı bir görüntü üzerine farklı bir görsel ekleyerek bu eklenen görselin eylemlerine göre ana görüntüde değişiklikler yapmayı denemek istedim. Sonuç olarak böyle bir uygulama ortaya çıktı.

## İçindekiler

0. [Herkese Selamlar](#herkese-selamlar)
1. [Uygulama Hakkında](#uygulama-hakkında)
2. [Yüklenmesi Gereken Kütüphaneler](#yuklenmesi-gereken-kutuphaneler)
3. [Eklenecek veya Düzenlenecek Kısımlar](#eklenecek-veya-duzenlenecek-kısımlar)
4. [Youtube Linki](#youtube-linki)

## Uygulama Hakkında

Uygulama çalıştırıldığı andan itibaren Pacman görseli canlı kamera görüntüsü üzerine eklenerek gösterilir. Kameraya ayarlanan renkte bir nesne gösterildiği zaman Pacman görseli o rengin konumuna doğru ilerler. Çıkış yapmak için Q tuşuna basmak yeterlidir.

![](./examples/image.gif)

Laptop kamera görüntüsü aşağıdaki kod parçacığındaki **VideoCapture(0)** ile alınmaktadır. Başka bir kamera eklemek isterseniz 0 değerini değiştirmeniz gerekir. Uygulama çalıştırıldığın da kamera açılmazsa kameranızın ulaşılabilirliğinin açık olduğundan emin olun.

```
cap = cv2.VideoCapture(0)

```
Alttaki kod parçasının olduğu kısımdan algılanmak istenen rengin değerleri girilerek farklı renklerde veya mavi rengin farklı tonlarında bir renk ayarı yapılabilir.

```
lower_blue = np.array([100,115,0])
upper_blue = np.array([140,255,255])

```


## Yuklenmesi Gereken Kutuphaneler

- Opencv kütüphanesi

```
pip install opencv-python

```
- Numpy kütüphanesi

```
pip install numpy

```

## Eklenecek veya Duzenlenecek Kısımlar

- Pacman görseli üzerinde zamanla oluşan bulanıklık giderilecek.
- Birden fazla ayarlanan renkte görüntülendiğinde tek bir çerçeve oluşuyor. Bu durum düzenlenerek birden fazla çerçeve oluşturulacak.
- Pacman görseli algılanan nesnenin üzerine gittiği zaman nesnenin rengi aynı şekilde kalıyor. Bu durum düzenlenerek rengin grileşmesi sağlanacak.

## Youtube Linki

Youtube üzerinden paylaştığım uygulama videosuna [bu linkten](https://youtu.be/tYKFwauHWc4) ulaşabilirsiniz.
