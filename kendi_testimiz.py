from ultralytics import YOLO

# 1. Hazır modeli değil, KENDİ eğittiğimiz modeli yüklüyoruz!
# Eğer senin modelin train2 veya train3 içindeyse aşağıdaki yolu ona göre düzelt.
model = YOLO("runs/detect/train/weights/best.pt") 

# 2. Test resmimizi modele verip tahmini kaydediyoruz
sonuclar = model.predict(source="test_resimlerim", save=True, conf=0.1)