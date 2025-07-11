## Matris Temelleri

**Matris Toplama:** Toplama yapılacak iki matrisin de aynı $m \times n$ boyutlarında olması gerekir. Karşılıklı gelen $x_{ij}$ değerleri toplanır. 

**Matris Skalerle Çarpma (Scale):** Matrisin tüm değerleri skalerle çarpılır.

**Matris Çarpımı:** $A_{m \times n}$ ve $B_{n \times p}$ matrislerinin çarpımı için A matrisinin satırı ile B matrisinin sütunlarını çarpım-toplam yaparız.

**Birim Matris:** $I_{ii}$ değerleri 1, diğerleri 0 olan matris.

## Lineer Denklemlerin Matris Çözümü

...

## Modül 3

...

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

matrisi için özdeğerler _7_ ve _-4_ olur. Fark edileceği üzere $$A - \lambda \cdot I$$ matrisinde özdeğerlerden birini yerine koyduğumuzda iki sütun da birbirinin katı olur. ~~Yani sütunları vektör olarak ele alırsak vektörlerin doğrultuları aynı olur. Bu sütunlardan birisini birinci özvektör olarak düşünebiliriz. Diğeri özdeğer için de aynısını yaptığımızda diğer özvektörü bulmuş oluruz.~~ _(Hemen alttaki ['Ekleme'](https://github.com/xxJuniOrCoderxx/veri-bilimi-calisma-notlari/blob/main/MuratAtaToyran_Expressway_to_Data_Science_Essential_Math/Essential_Linear_Algebra/readme.md#ekleme) kısmına bakın)_ Bu $\lambda$ değerlerini koyduktan sonra bulacağımız iki matris aşağıdaki gibidir:

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

------------------------------
#### *Ekleme:*
Ama bu yapı 3x3 matrislerde sağlanmıyor. Aşağıdaki örneğe bakın:

$$
\begin{bmatrix}
12 & -8 & 3 \\
20 & -4 & 0 \\
34 & -12 & 3
\end{bmatrix}
$$

Bunlar için özdeğerler 1, 4 ve 6 olur. Ama yerine koyduğumuzda özvektörleri elde edemiyoruz ve sütunlar birbirinin katı olmuyor. Özvektörler aşağıdaki gibidir:

$$
\begin{align*}
\begin{bmatrix}
1  \\
4  \\
7
\end{bmatrix}
&&&ve&&&
\begin{bmatrix}
2  \\
5  \\
8
\end{bmatrix}
&&&ve&&&
\begin{bmatrix}
3  \\
6  \\
10
\end{bmatrix}
\end{align*}
$$

-------------------------------------
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

Özdeğeri bilinen bir matrisin özvektörünü bulmak için $$[A - \lambda \cdot I] \cdot v = 0$$ eşitliğini sağlayan vektörü lineer denklemlerin matrislerle çözümü sayesinde bulabiliriz.


😂Burada ilginç bir şey var ki üstteki örnekte baktığımız özvektörü oluşturmak için 7 özdeğerini kullandık ama bu denklemde eşitliği -4 özdeğeri sağlıyor. Aynısını diğer vektörle deneseydik bu denklemde bu sefer 7 özdeğerini kullanmış olacaktık. Değinmek istedim _(_ $$A \cdot v = \lambda \cdot v$$ _kısmından bahsediyorum ama işlerin biraz farklı olduğunu üstte eklemiş olduğum ['Ekleme'](https://github.com/xxJuniOrCoderxx/veri-bilimi-calisma-notlari/blob/main/MuratAtaToyran_Expressway_to_Data_Science_Essential_Math/Essential_Linear_Algebra/readme.md#ekleme) kısmında anlattım)_.😂 Ayrıca konuyla ilgilenenler [şu videoya](https://www.youtube.com/watch?v=1sDBruay100) da göz atabilir.

Ayrıca aşağıdaki yöntemi de inceleyebilirsiniz:
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

***Not:*** Vektörle aynı doğrultuda birim vektör oluşturmak için vektörün kendisini vektörün uzunluğuna böleriz. Yani: 

$$\frac{A}{\begin{Vmatrix}
A
\end{Vmatrix}}$$ 

şeklinde birim vektör olmuş olur.

## İki Vektör Arasındaki Uzaklık

İki vektör arasındaki uzaklığı bulmak için iki vektörün farkının normunu alırız. Yani:

$$
\begin{align*}
dist(u, v) =
\begin{Vmatrix}
u-v
\end{Vmatrix}
\end{align*}
$$

Örnek:

$$
\begin{align*}
\begin{bmatrix}
6  \\
9 
\end{bmatrix}
&ve&
\begin{bmatrix}
7  \\
5 
\end{bmatrix}
&arasındaki&uzaklık& \sqrt{(-1)^2 + 4^2} =\sqrt{17} & olur.
\end{align*}
$$

## Dik Vektörler(Orthogonal Vectors)

1. Eğer u ve v vektörleri dikse iç çarpımları 0 olur.
2. Eğer u ve v vektörleri dikse $$norm(u+v)^2=norm(u)^2+norm(v)^2$$ olur.
3. 2 ve 3 boyutlu uzayda u ve v vektörlerinin iç çarpımları, vektörlerin normlarının çarpımının aralarındaki açının kosinüsüyle çarpımıdır.

## Dik Yansıtmalar(Orthogonal Projections)

_y vektörünün u vektörü üzerine yansıtılması örneğini aşağıda görebilirsiniz:_

![IMG_1899](https://github.com/user-attachments/assets/d10b2a54-b46a-4321-847e-ead8893a5069)

## En Küçük Kareler Metodu

...
