
# YOLOv8 - Ormanda Yatan İnsan Tespiti (Forest Human Detection)

🔗 **[Eğitilmiş Modeli İncelemek ve İndirmek İçin Hugging Face Sayfama Tıklayın](https://huggingface.co/Mahmut26662/yolov8-forest-human-detection)**

### 📂 Bu Depoda Ne Var?
Bu GitHub deposu, modelin eğitim sürecini içeren Python kodlarını (`train.py`), veri seti yapılandırmasını (`data.yaml`) ve modelin test edildiği örnek görselleri barındırmaktadır. Modelin eğitilmiş ağırlıkları (`best.pt`) dosya boyutundan dolayı Hugging Face üzerinde tutulmaktadır.

---

Bu model, ormanlık ve yeşillik alanlarda... (Senin yazdığın metnin geri kalanı buradan devam edecek)
Bu model, ormanlık ve yeşillik alanlarda yerde yatan veya kaybolan insanları havadan/yerden tespit etmek amacıyla eğitilmiş bir nesne tanıma (object detection) modelidir. Ultralytics YOLOv8 mimarisi kullanılarak sıfırdan oluşturulan özel bir veri seti ile fine-tune edilmiştir.

## Model Detayları
* **Model Tipi:** Nesne Tespiti (YOLOv8)
* **Kullanım Amacı:** Arama-kurtarma operasyonları, ormanlık alanlarda kayıp şahıs tespiti, drone veya kamera sistemleri ile entegre güvenlik taramaları.
* **Sınırlılıklar:** Model ağırlıklı olarak yeşillik ve orman dokusu üzerinde eğitilmiştir. Şehir içi ortamlarda, kapalı alanlarda veya gece görüşü (termal olmayan) kameralarında performansı test edilmemiştir. Sadece `insan` sınıfını tespit eder.

## Veri Seti (Dataset)
Modelin eğitiminde tamamen bu proje için oluşturulmuş özel bir veri seti kullanılmıştır.
* **Kaynak:** Roboflow üzerinden etiketlenmiş ve dışa aktarılmıştır ("merhaba - vdataset").
* **Boyut:** Toplam 90 adet görsel içermektedir.
* **Ön İşleme (Pre-processing):** Herhangi bir ekstra görüntü büyütme (augmentation) veya ön işleme uygulanmamıştır, ham veriler kullanılmıştır.
* **Format:** YOLOv8 formatı.

## Eğitim Detayları (Training Details)
Model, yerel donanım üzerinde aşağıdaki parametrelerle eğitilmiştir:
* **Epoch:** 100
* **Donanım:** HP Victus 16 (Intel Core i5-14500HX CPU, NVIDIA GeForce RTX 4060 GPU)
* **Kütüphane:** `ultralytics` 

## Performans ve Başarım (Evaluation)
Eğitim sonucunda elde edilen temel doğruluk (accuracy) metrikleri şöyledir:
* **mAP50:** 0.95455
* **Precision (Kesinlik):** 0.79889
* **Recall (Duyarlılık):** 0.97528

![results](https://cdn-uploads.huggingface.co/production/uploads/6a2bdd72ee6b4bccd93089eb/Nb3CZp1CjGCHCGNvjwauU.png)



## Çalışan Inference Örneği (How to Use)
Bu modeli Python ortamında test etmek için aşağıdaki kodu kullanabilirsiniz:

```python
# Gerekli kütüphaneleri yükleyin: 
# pip install ultralytics huggingface_hub
from huggingface_hub import hf_hub_download
from ultralytics import YOLO
# 1. Modeli Hugging Face üzerinden indir
model_path = hf_hub_download(repo_id="Mahmut26662/yolov8-forest-human-detection", filename="best.pt")
# 2. Modeli yükle
model = YOLO(model_path)
# 3. Test resmini ver ve tahminleme yap
results = model("test_resminizin_yolu.jpg")
# 4. Sonucu ekranda göster
results[0].show()
