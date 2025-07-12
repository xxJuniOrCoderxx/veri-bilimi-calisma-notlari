# 🧮 Maxima ve Minima: Türevin Uygulamaları

## 📌 Tanımlar

- **Maksimum (Maximum):** Fonksiyonun ulaştığı en yüksek değer.
- **Minimum (Minimum):** Fonksiyonun ulaştığı en düşük değer.
- **Mutlak (Absolute) Maksimum/Minimum:** Fonksiyonun tanım aralığında ulaştığı en büyük/küçük değer.
- **Bağıl (Relative/Local) Maksimum/Minimum:** Fonksiyonun belli bir çevresinde ulaştığı en büyük/küçük değer.

---

## 🎯 Türev ve Ekstremum Noktaları

- Bir fonksiyonun **tepe noktalarında (max/min)** türevi sıfır olur.
  
```math```
f'(x) = 0 → \text{kritik nokta (candidate for max/min)}

# 🔄 Rates of Change (Değişim Hızı)

## 📌 Türev = Değişim Hızı

Türev, bir fonksiyonun **değişim hızını** ifade eder. Yani, **y'nin x'e göre ne kadar hızlı değiştiğini** gösterir.

Bu kavram farklı şekillerde yazılabilir:

- `dy/dx` → y'nin x'e göre türevi  
- `y'` → y fonksiyonunun türevi  
- `f'(x)` → f fonksiyonunun türevi

Hepsi aynı şeyi ifade eder: **x değiştikçe y ne kadar değişiyor?**

---

## 🧮 Oranlar

- Ortalama değişim:  
  \[
  \frac{\Delta y}{\Delta x}
  \]

- Anlık değişim (türev):  
  \[
  \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \frac{dy}{dx}
  \]

---

## 🚗 Gerçek Hayattan Örnekler

### 1. **Hız (Velocity)**  
- Tanım: Mesafenin zamana göre değişim hızı  
- Birimler: km/saat, m/s gibi  
- Matematiksel gösterim:  
  \[
  v = \frac{ds}{dt}
  \]

### 2. **İvme (Acceleration)**  
- Tanım: Hızın zamana göre değişim hızı  
- Birimler: m/s², km/s² gibi  
- Matematiksel gösterim:  
  \[
  a = \frac{dv}{dt} = \frac{d^2s}{dt^2}
  \]

Bu, **ikinci türev** ile ifade edilir ve bazen şu şekilde yazılır:

```math
\frac{d^2y}{dx^2}
