# Python'da Modülarite

Python'da **modülarite (modularity)**, bir programı daha küçük, bağımsız ve tekrar kullanılabilir parçalara (**modüllere**) ayırma ilkesidir. Bu yazılım geliştirmede çok önemli bir yaklaşımdır çünkü:

- ✅ Kodun okunabilirliğini artırır  
- 🛠️ Bakım ve hata ayıklamayı kolaylaştırır  
- ♻️ Tekrar kullanılabilirliği sağlar  

---

## 🧱 Python'da Modül Nedir?

Python'da bir **modül**, `.py` uzantılı bir Python dosyasıdır. İçinde:

- Fonksiyonlar  
- Sınıflar  
- Değişkenler  
- Diğer kodlar  

bulunabilir.

### Örnek: `math_utils.py`

```python
# math_utils.py
def kare(x):
    return x * x

def kup(x):
    return x * x * x
```

Bu bir modüldür. Başka bir dosyada bunu şöyle kullanabilirsin:

```python
from math_utils import kare, kup

print(kare(4))  # 16
print(kup(3))   # 27
```

## 📦 Modülaritenin Temel Bileşenleri

| Bileşen       | Açıklama                                                  |
|---------------|------------------------------------------------------------|
| **Modül**     | Tek bir `.py` dosyası                                     |
| **Paket**     | `__init__.py` içeren klasör, birden çok modül içerir      |
| **import**    | Başka modülleri içe aktarmak için kullanılır              |
| **namespace** | Modüller kendi ad alanlarında çalışır, çakışma önler      |

---

## 🔁 Neden Modüler Kod Yazarız?

1. **Kod tekrarını önler**: Aynı fonksiyonu birçok yerde tekrar yazmak gerekmez.  
2. **Test edilebilirlik**: Her modül ayrı ayrı test edilebilir.  
3. **Takım çalışması**: Farklı geliştiriciler farklı modüller üzerinde çalışabilir.  
4. **Okunabilirlik**: Ana program dosyası sade ve anlaşılır kalır.  
5. **Bakım kolaylığı**: Hangi modül hangi işle ilgileniyor kolayca anlaşılır ve güncellenebilir.

## 🧠 Örnek: Modüler olmayan vs modüler yaklaşım

### ❌ Modüler olmayan:

```python
x = int(input("Sayı gir: "))
print(x * x)
```

### ✅ Modüler:

```python
# utils.py
def kare(x):
    return x * x
```
```python
# main.py
from utils import kare

x = int(input("Sayı gir: "))
print(kare(x))
```

## 🧩 Sonuç

**Modülarite**, Python’da kodu yönetilebilir, okunabilir ve sürdürülebilir hale getirmenin temel taşıdır.

> "Bir sorun varsa, onu küçük parçalara ayır. Python’da bu parçalara _modül_ denir."
