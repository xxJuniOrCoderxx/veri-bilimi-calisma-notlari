## Determinant

Matrisin karakteristiği hakkında çok fazla şey söyleyen, belli hesaplamalar sonucu bulunan sayıdır.

### 2x2 matris için determinant hesaplama
Aşağıdaki gibi bir matris verilsin:

$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

Bu matrisin determinantını şu şekilde hesaplayabiliriz:

$$
\begin{align*}
\begin{vmatrix}
a & b \\
c & d \\
\end{vmatrix}
= \det\begin{pmatrix} 
a & b \\
c & d
\end{pmatrix}
= (a \cdot d) - (b \cdot c)
\end{align*}
$$

Örnek:

$$
\begin{align*}
\begin{vmatrix}
1 & 2 \\
3 & 4 \\
\end{vmatrix}
= (1 \cdot 4) - (2 \cdot 3)
= -2
\end{align*}
$$

### 3x3 matris için determinant hesaplama

2x2'ye benzer ama biraz daha karmaşık. 
1. adım: Satırlardan veya sütunlardan bir tanesini seçin. determinantını hesaplayacağımız 3x3 matrisin adı X olsun.
2. adım: Seçtiğiniz bu satır (veya sütun) üzerindeki değerlerin her biri için bulunduğu satır ve sütundaki değerleri çıkararak yeni 2x2'lik matris oluşturup determinantını alın. i satırının j sütunu için oluşturulan bu yeni matrise $A_{ij}$ diyelim.
3. adım: Seçtiğimiz satırdaki tüm değerler için <span style="background-color: #FFFF00"> $$(-1)^{i+j} \cdot det(A_{ij}) \cdot A_{ij}$$ </span> değerini hesaplayıp bu değerleri topladığımızda 3x3 matrisiçin determinantı elde etmiş oluruz.

Örnek:

..........

