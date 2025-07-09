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
3. adım: Seçtiğimiz satırdaki tüm değerler için  $$(-1)^{i+j} \cdot det(A_{ij}) \cdot X_{ij}$$ hesaplayıp bu değerleri topladığımızda 3x3 matrisiçin determinantı elde etmiş oluruz.

Örnek:


..........

## Özdeğer ve Özvektör (Eigenvalue/Eigenvector)

$$
\begin{align*}
\det\begin{pmatrix} 
A - \lambda \cdot I
\end{pmatrix} 
=0 
\end{align*}
$$

eşitliğini sağlayan $\lambda$ değerlerine **özdeğer** denir.

Örneğin:

$$
\begin{bmatrix}
1 & 6 \\
5 & 2
\end{bmatrix}
$$

matrisi için özdeğerler _7_ ve _-4_ olur. Fark edileceği üzere $$A - \lambda \cdot I$$ matrisinde özdeğerlerden birini yerine koyduğumuzda iki sütun da birbirinin katı olur. Yani sütunları vektör olarak ele alırsak vektörlerin doğrultuları aynı olur. Bu sütunlardan birisini birinci özvektör olarak düşünebiliriz. Diğeri özdeğer için de aynısını yaptığımızda diğer özvektörü bulmuş oluruz. Bu değerleri koyduktan sonra bulacağımız iki matris aşağıdaki gibidir:

$$
\begin{align*}
\begin{bmatrix}
-6 & 6 \\
5 & -5
\end{bmatrix}
&&&ve&&&
\begin{bmatrix}
5 & 6 \\
5 & 6
\end{bmatrix}
\end{align*}
$$

Buradan da özvektörler aşağıdaki gibi olur:

$$
\begin{align*}
\begin{bmatrix}
-6  \\
5 
\end{bmatrix}
&&&ve&&&
\begin{bmatrix}
1  \\
1 
\end{bmatrix}
\end{align*}
$$

Bir matris için verilen vektörün özvektör olup olmadığını $$A \cdot v = \lambda \cdot v$$ formülüyle de hesaplayabiliriz. Örneğimize bakarsak:

$$
\begin{align*}
\begin{bmatrix}
1 & 6 \\
5 & 2
\end{bmatrix}
\cdot
\begin{bmatrix}
-6  \\
5 
\end{bmatrix}
= (-4)
\cdot
\begin{bmatrix}
-6  \\
5 
\end{bmatrix}
\end{align*}
$$

Burada ilginç bir şey var ki üstteki örnekte baktığımız özvektörü oluşturmak için 7 özdeğerini kullandık ama bu denklemde eşitliği -4 özdeğeri sağlıyor. Aynısını diğer vektörle deneseydik bu denklemde bu sefer 7 özdeğerini kullanmış olacaktık. Değinmek istedim. Ayrıca konuyla ilgilenenler [şu videoya](https://www.youtube.com/watch?v=1sDBruay100) da göz atabilir.

Bu arada aşağıdaki yöntemi de inceleyebilirsiniz:
![image](https://github.com/user-attachments/assets/4927bbec-3aba-4726-8147-b4f895c8923d)

## Transpoz ve İç çarpım(Inner Product/Dot Product)

Aşağıdaki A matrisine göz atalım:

$$
\begin{bmatrix}
1 & 6 & 3\\
5 & 2 & 4
\end{bmatrix}
$$

Bu matrisi transpoze etmek için satırları sütun, sütunları satır gibi yazarız. Diğer bir deyişle sol üst köşe sabit olacak şekilde matrisi ters yüz ederiz. Yani yukarıdaki matrisin transpozu aşağıdaki gibi olur ve $A^T$ diye gösterilir.

$$
\begin{bmatrix}
1 & 5\\
6 & 2 \\
3 & 4
\end{bmatrix}
$$

İç çaprım da iki vektörün aynı değerlerinin çarpım-toplamının yapıldığı işlemdir. Yani:

$$
\begin{align*}
\begin{bmatrix}
1 \\
6 \\
3 
\end{bmatrix}
\cdot
\begin{bmatrix}
4 \\
5 \\
2 
\end{bmatrix}
= 1 \cdot 4 + 6 \cdot 5 + 3 \cdot 2
= 40 &yapar :)
\end{align*}
$$

İç çarpımı ilk vektörün transpozu ile ikinci vektörün matris çarpımı şeklinde de düşünebiliriz. Yani:

$$
\begin{align*}
\begin{bmatrix}
1 &
6 &
3 
\end{bmatrix}
\cdot
\begin{bmatrix}
4 \\
5 \\
2 
\end{bmatrix}
= 1 \cdot 4 + 6 \cdot 5 + 3 \cdot 2
= 40 &yapar :D
\end{align*}
$$

## Vektörün Normu(Uzunluğu)

Vektörün uzunluğu, vektörün kendisiyle iç çarpımının kareköküdür. Mesela A matrisi aşağıdaki gibi olsun:

$$
\begin{bmatrix}
1 \\
6 \\
3
\end{bmatrix}
$$

Bunun uzunluğu aşağıdaki gibi olur:

$$
\begin{align*}
\begin{Vmatrix}
A
\end{Vmatrix}
= \sqrt{1^2 + 6^2 + 3^2}
= \sqrt{46}
\end{align*}
$$

**Not:** Vektörle aynı doğrultuda birim vektör oluşturmak için vektörün kendisini vektörün uzunluğuna böleriz. Yani: $$\frac{A}{\begin{Vmatrix}
A
\end{Vmatrix}}$$ olmuş olur.
