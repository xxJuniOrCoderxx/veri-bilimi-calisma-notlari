# 📘 Türev Kuralları: Çarpım Kuralı (Product Rule)

## 🧠 Tanım

İki fonksiyonun çarpımının türevi şu şekilde hesaplanır:

> **(f(x) · g(x))' = f(x) · g'(x) + f'(x) · g(x)**

Bu kural, iki fonksiyonun çarpımı söz konusu olduğunda türevi daha kolay ve sistematik şekilde alabilmemizi sağlar.

---

## 🧪 Örnek Üzerinden Anlatım

### Fonksiyonlar:

- **f(x) = x² - 2**
- **g(x) = x² + x**

Çarpım fonksiyonunu tanımlayalım:

```math
h(x) = f(x) · g(x)
     = (x² - 2)(x² + x)
# ⚙️ Sabit Katsayı Kuralı (Constant Multiple Rule)

## 📘 Tanım

Bir fonksiyon sabit bir sayı ile çarpılmışsa, türevi alırken bu sabiti dışarı alabiliriz:

> **(c · f(x))' = c · f '(x)**

Bu kural, aslında çarpım kuralından (product rule) türetilebilir.

---

## 🔍 Neden Bu Kural Doğrudur?

Product rule'a göre:

> **(a · f(x))' = a · f '(x) + f(x) · (a)'**

Ama sabitin türevi sıfırdır, yani **(a)' = 0**, bu nedenle:

> **(a · f(x))' = a · f '(x)**

---

## 🧪 Örnekler

### Örnek 1:

**f(x) = 3 · e^x**

```math
f '(x) = 3 · (e^x)' = 3e^x

# ➗ Bölüm Kuralı (Quotient Rule)

## 📘 Tanım

Eğer elimizde iki fonksiyonun bölümü varsa:

> **h(x) = f(x) / g(x)**

Türevi şu şekilde alınır:

> **h '(x) = [g(x) · f '(x) – f(x) · g '(x)] / [g(x)]²**

> 💡 Kuralı hatırlamak için:
> **"Alt çarpı türev üst, eksi üst çarpı türev alt, bölü altın karesi"**

---

## 🧪 Örnek

Fonksiyonumuz şu olsun:

> **h(x) = (x² – 3x) / (x² + 4)**

### 1️⃣ Adım: Tanımlı parçaları belirleyelim:

- **f(x) = x² – 3x → f '(x) = 2x – 3**
- **g(x) = x² + 4 → g '(x) = 2x**

---

### 2️⃣ Adım: Quotient Rule formülünü uygulayalım:

```math
h '(x) = [(x² + 4)(2x – 3) – (x² – 3x)(2x)] / (x² + 4)²

# 🔗 Zincir Kuralı (Chain Rule)

## 📘 Tanım

Eğer bir fonksiyon başka bir fonksiyonun içinde tanımlanmışsa ve bir üst sayıya sahipse, türevi alırken **zincir kuralı (chain rule)** kullanılır.

> **f(x) = [u(x)]ⁿ ⇒ f '(x) = n · [u(x)]ⁿ⁻¹ · u '(x)**

- **u(x)**: iç fonksiyon
- **n**: dıştaki kuvvet
- **u '(x)**: iç fonksiyonun türevi

---

## 🔍 Basit Örnek

Verilen fonksiyon:

> **f(x) = (6x + 4)^5**

Türevi:

```math
f '(x) = 5 · (6x + 4)^4 · 6 = 30 · (6x + 4)^4
