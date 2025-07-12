
# 🧠 Proof by Induction (İndüksiyonla İspat)

## 🧩 Tanım
Bir ifadenin **bütün doğal sayılar için geçerli olduğunu** ispatlamak amacıyla kullanılan matematiksel tekniktir.

---

## 🔁 Adımlar

### 1. **Base Case (Temel Durum)**  
İspatlanan ifadenin küçük bir başlangıç değeri (genelde `n = 1` ya da `n = 0`) için doğru olduğunu göster.

### 2. **Induction Step (İndüksiyon Adımı)**  
Şunu varsay:  
İfade `n = k` için doğru.  
→ **Induction Hypothesis** denir.

Bu varsayımla, ifadenin `n = k + 1` için de doğru olduğunu göster.  
Bu adım genellikle cebirsel işlemler ve sadeleştirme gerektirir.

---

## 📌 Örnek:  
```math
∑_{i=1}^{n} [1 / (i(i+1))] = n / (n + 1)
# 📉 Limits (Limit Kavramı)

## 🧠 Limit Nedir?
Bir fonksiyonun, belirli bir değere **yaklaştıkça** çıktısının neye yaklaştığını gösterir. Örneğin:

- `1/n` ifadesinde `n → ∞` olduğunda:  
  **Limit = 0**  
  Çünkü `n` büyüdükçe `1/n` sıfıra yaklaşır (ama asla tam 0 olmaz).

---

## 🔁 ∞'de Limitler (Limits at Infinity)

### 📌 Temel Kurallar:

- **Üst (pay) daha hızlı büyüyorsa → ∞**  
  Örnek: `x³ / x` → ∞

- **Alt (payda) daha hızlı büyüyorsa → 0**  
  Örnek: `x / x²` = `1/x` → 0

- **Üst ve alt aynı derecedeyse → Katsayıların oranı**  
  Örnek:  
  ```math
  lim(x→∞) (2x² - 100) / (3x² + 100) = 2 / 3

# 🔁 Limits: Right, Left, and Infinite

## ✳️ 1. Tek Taraflı Limitler (One-Sided Limits)
- **Limit from the left:** `lim(x→a⁻) f(x)`
- **Limit from the right:** `lim(x→a⁺) f(x)`
- Eğer `lim(x→a⁻) ≠ lim(x→a⁺)` ise:
  - **Limit exists?** ❌ **Yok**
  - Fonksiyon tanımlı olabilir ama limit tanımsız olur.

## 🧮 Örnek:
Grafikte `f(x)`:
- Soldan 1'e yaklaşınca → `1`
- Sağdan 1'e yaklaşınca → `2`
- Sonuç: `lim(x→1) f(x)` **yok** (çünkü sağ ve sol limit farklı)

---

## 🔄 2. Sonsuza Giderken Limit (Limits at Infinity)
- `f(x) = 1/x`
  - `lim(x→∞) 1/x = 0`
  - `lim(x→−∞) 1/x = 0`
- Ama: `lim(x→0⁺) 1/x = +∞`, `lim(x→0⁻) 1/x = −∞`  
  → **Limit yok (sonsuzluk)**

---

## ❗ Limitin Olmadığı Durumlar
1. Sağ ve sol limit **eşit değilse**  
2. Fonksiyon değeri **sonsuzsa (∞ veya -∞)**  
3. Fonksiyon **tanımsızsa** (örneğin 1/0 gibi)

# 🔗 Continuity (Süreklilik)

## ✅ Sürekli Fonksiyon Nedir?
Bir fonksiyon **sürekli** ise:
- Grafiğini çizerken kalemi kaldırmana gerek yoktur.
- Yani grafik üzerinde **kopma, atlama ya da delik** yoktur.

## 🔍 Süreklilik Şartları
Bir fonksiyon `f(x)` noktası olan `x = a`'da sürekli ise:
1. `f(a)` **tanımlı** olmalı
2. `lim(x→a⁻) f(x)` ve `lim(x→a⁺) f(x)` **mevcut** ve **eşit** olmalı
3. Bu limit değeri **f(a)**'ya **eşit** olmalı

## ❌ Süreksizlik (Discontinuity) Türleri
- **Jump discontinuity (atlama):** Sağ ve sol limit farklı → örn: `lim(x→1⁻) ≠ lim(x→1⁺)`
- **Hole (delik):** Limit var ama `f(a)` tanımsız ya da farklı → grafik üzerinde boşluk
- **Asymptotic:** Örn: `f(x) = 1/x` → `x = 0`'da tanımsız (ama tanımlı olduğu yerde süreklidir)

## 📌 Not:
- Bir fonksiyonun **tüm tanım aralığında sürekli olması**, o fonksiyonun **sürekli fonksiyon** olduğunu gösterir.
- Örn: `1/x` fonksiyonu, `x ≠ 0` için sürekli ama `x = 0`'da tanımsızdır.

