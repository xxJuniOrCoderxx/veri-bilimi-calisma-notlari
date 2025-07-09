# 📊 Math for Data Science – Course 1: Functions & Rates of Change

## ✅ What is a Function?

- A **function** is like a box: it takes **one input** and gives **one output**.
- Example: `f(x) = x² + 1`
  - `f(0) = 1`, `f(-1) = 2`, `f(1) = 2`
- Each input has **only one output**, but multiple inputs can yield the **same output**.

## 📈 Graph of a Function

- x-axis: input  
- y-axis: output  
- Example: Graph of `f(x) = x² + 1` is a **parabola** opening upwards.
- Still a function even if `f(-1) = f(1)` — because input → one output.

## ❌ Not a Function (Visually)

- If one x-value maps to **multiple y-values**, it's **not a function**.
- Use the **Vertical Line Test**: If a vertical line hits the graph more than once → not a function.
- Eğer bir girdi (x) için birden fazla çıktı (y) varsa, bu bir fonksiyon değil, sadece bir ilişkidir.

## 🧠 Key Rule

> A function assigns **exactly one output** for **each input**.

# 📘 Domain and Range of a Function

## 🔹 What is Domain?
- The **domain** is the set of **all possible valid inputs** (x-values) for a function.
- A value is **excluded** from the domain if it:
  - Causes division by zero → e.g. `f(x) = 1/x`, domain: `x ≠ 0`
  - Results in a non-real number → e.g. `f(x) = √(x + 1)`, domain: `x ≥ -1`

## 🔹 What is Range?
- The **range** is the set of **all possible outputs** (y-values) the function can produce.
- Example:
  - `f(x) = 1/x` → Range: `y ≠ 0`
  - `g(x) = √(x + 1)` → Range: `y ≥ 0`

## 🔹 Key Ideas:
- Domain → “What goes **into** the function?”
- Range → “What comes **out of** the function?”

## 🔸 Graphical Tip:
- **Domain**: Check horizontal extent (x-axis)
- **Range**: Check vertical extent (y-axis)

---
# 📘 Piecewise Functions (Parçalı Fonksiyonlar)

## 🔹 Nedir?
- **Piecewise function (parçalı fonksiyon)**: Girdi değerine göre **farklı işlemler** uygulayan fonksiyon türüdür.
- Fonksiyon farklı aralıklar için farklı kurallar tanımlar.

## 🔹 Örnek:
f(x) =  
  x² + 1  if x > 0  
  x - 1  if x ≤ 0  

### Örnek Hesaplamalar:
- f(1) = 1² + 1 = 2
- f(0) = 0 - 1 = -1
- f(-3) = -3 - 1 = -4
- f(4) = 4² + 1 = 17

## 🔹 Grafiksel Özellik:
- Her parçanın kendi **grafiksel tanımı** olur.
- Aralıklar açık veya kapalı olabilir (örneğin x > 0 → açık daire).
- **Süreksizlik (discontinuity)** oluşabilir, yani grafik "atlayabilir".

## 🔸 Ana Fikir:
- Fonksiyon kutusu, **girdi değerine göre hangi işlem uygulanacağına karar verir**.
- Aynı fonksiyon, farklı girdiler için **farklı matematiksel ifadeler** kullanabilir.

