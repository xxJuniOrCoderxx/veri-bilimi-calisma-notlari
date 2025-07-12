## 📌 11. Türev Nedir?

### 🎯 Türev (Derivative) Tanımı:
- Türev, bir fonksiyonun **bir noktadaki değişim oranını (eğimini)** bulma yöntemidir.
- Geometrik olarak, bir eğrinin bir noktasındaki **teğet doğrunun eğimi** anlamına gelir.
- Bu eğimi bulmak için iki nokta alınır:  
  - Birisi `x`, diğeri `x + h`.  
  - Bu iki noktadan geçen doğrunun eğimi:  
    ```
    [f(x + h) - f(x)] / h
    ```

### ➗ Limit Yaklaşımı:
- Bu orana, `h` değeri sıfıra **yaklaştırıldığında** (limit alınarak) elde edilen değer:  
  - **Türev** budur.
  - Yani:  
    ```
    f'(x) = lim(h→0) [f(x + h) - f(x)] / h
    ```

### 📐 Grafiksel Anlamı:
- `x` noktasındaki teğet eğimi, `x + h` noktasına gittikçe daha da yaklaşan **sekant doğruların** eğimiyle yaklaşık bulunur.
- `h → 0` oldukça sekant doğrusu, teğet doğrusuna dönüşür.

### 📘 Notasyonlar:
- `f'(x)` → "f'in türevi"
- "f'nin x noktasındaki anlık değişim hızı" veya "teğet eğimi"

---

## 2. Örnek: f(x) = x² için Türev
- f(x + h) = (x + h)² = x² + 2xh + h²
- f'(x) = lim(h→0) [(x² + 2xh + h² - x²) / h] = lim(h→0) [2x + h] = **2x**

## 3. Türevin Yorumu
- f'(1) = 2 → x = 1 noktasındaki eğim 2
- f'(0) = 0 → minimum nokta
- f'(-1) = -2 → x = -1 noktasında negatif eğim

## 4. Türev Alma Kuralları

### a. Sabit Fonksiyon
- f(x) = c ⇒ f'(x) = 0

### b. Polinomlar
- f(x) = xⁿ ⇒ f'(x) = n·xⁿ⁻¹
- Örnek: f(x) = -x² + 3x ⇒ f'(x) = -2x + 3

### c. Üstel Fonksiyonlar
- f(x) = eˣ ⇒ f'(x) = eˣ
- Tanım üzerinden:  
eˣ⁺ʰ - eˣ = eˣ(eʰ - 1)  
lim(h→0) (eʰ - 1)/h = 1 ⇒ f'(x) = eˣ

### d. Toplam/Türev Toplamı
- f(x) = u(x) + v(x) ⇒ f'(x) = u'(x) + v'(x)

## 5. Türevin Uygulamaları
- Eğimin pozitif/negatif/0 olması, fonksiyonun artan/azalan/sabit olduğu anlamına gelir.
- Maksimum ve minimum noktalar türev = 0 olduğu yerlerde olabilir.

# 📘 Türev Kuralları: Çarpım ve Zincir Kuralı

## ✅ 1. Çarpım Kuralı (Product Rule)

İki fonksiyonun çarpımının türevi şu şekilde alınır:
(f(x) · g(x))' = f'(x) · g(x) + f(x) · g'(x)

## 🔁 2. Zincir Kuralı (Chain Rule)

İç içe geçmiş fonksiyonlarda (bileşik fonksiyonlarda) türev alınırken kullanılır.

(f(g(x)))' = f'(g(x)) · g'(x)
