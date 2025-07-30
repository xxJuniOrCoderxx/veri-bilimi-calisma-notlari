## Matrisin Temel İşlemleri

**Matris Toplama:** İki matrisin toplanabilmesi için boyutlarının aynı, yani her ikisinin de $m \times n$ boyutlarında olması gerekir. Toplama işlemi, karşılıklı gelen elemanların ($x_{ij}$) toplanmasıyla gerçekleştirilir. 

**Matris Skalerle Çarpma (Scale):** Bir matrisin tüm elemanları, sabit bir skaler sayı ile çarpılır. Bu işlem, matrisin boyutunu değiştirmez.

**Matris Çarpımı:** $A_{m \times n}$ ve $B_{n \times p}$ boyutlarında iki matrisin çarpımı, $A$ matrisinin satırları ile $B$ matrisinin sütunlarının skaler çarpım-toplamı alınarak elde edilir.

**Birim Matris:** Diagonal (köşegen) elemanları 1, diğer tüm elemanları 0 olan kare matrise birim matris ($I$) denir. $I_{ii} = 1$ ve $I_{ij} = 0$ (i ≠ j).

**Matrisin Tersi:** Kare bir matris olan $A$'nın tersi $A^{-1}$ ile gösterilir ve şu özelliği sağlar: $A \cdot A^{-1} = A^{-1} \cdot A = I$ 

## Lineer Denklem Sistemlerinin Matrisle Gösterimi ve Çözümü

Verilen lineer denklem sistemi:

```
1x + 2y - 3z = 0
4x + 5y - 7z = 2
6x + 8y - 9z = 5
```
Bu sistem, matris formunda $A \cdot x = b$ biçiminde gösterilir:

$$
\begin{align*}
\begin{bmatrix}
1 & 2 & -3 \\
4 & 5 & -7 \\
6 & 8 & -9
\end{bmatrix}
\cdot 
\begin{bmatrix} 
x \\
y \\
z
\end{bmatrix}
= \begin{bmatrix} 
0 \\
2 \\
5
\end{bmatrix}
\end{align*}
$$

### Çözüm Yöntemi

Bu sistemin çözümü için genişletilmiş matris (augmented matrix) kullanılır:

$$
\begin{bmatrix}
1 & 2 & -3 & | & 0 \\
4 & 5 & -7 & | & 2 \\
6 & 8 & -9 & | & 5
\end{bmatrix}
$$

Bu matrise, Gauss-Jordan eliminasyonuna benzer biçimde satır işlemleri uygulanır:

- Satırların yer değiştirilmesi
- Satırların bir sabit ile çarpılması
- Satırların birbirinin katlarıyla toplanması

-> Amaç, matrisin köşegenindeki elemanlar dışındaki tüm değerleri sıfırlamaktır. Örnekteki sistemin çözümü $x=1$, $y=1$, $z=1$ olarak bulunur.

📌 **Not:** Bir lineer denklem sisteminin ya hiç çözümü yoktur, ya bir tekil (tek) çözümü vardır ya da sonsuz sayıda çözüm içerir.

## Vektörler

Satır vektörleri ve sütun vektörleri olmak üzere iki tane vektör çeşidi vardır. Sütun vektörleri $(m \times 1)$ formatındadır, satır vektörleri ise $(1 \times n)$ formatındadır.

### Lineer Kombinasyonlar

Bir $y$ vektörünün, verilen $v_1, v_2, ..., v_n$ vektörlerinin doğrusal birleşimi (lineer kombinasyonu) şu şekilde ifade edilmektedir:

$y = c_1 \cdot v_1 + c_2 \cdot v_2 + ... + c_n \cdot v_n$ 

Burada $c_1, c_2, ..., c_n$ bilgileri `lineer kombinasyon katsayıları` olarak tanımlanmaktadır.

**Örnek:**

$$
\begin{align*}
v_1 =
\begin{bmatrix}
1\\
4\\
6
\end{bmatrix}
&  &
v_2 =
\begin{bmatrix}
2\\
5\\
8
\end{bmatrix}
& &ve& &
y =
\begin{bmatrix}
7\\
4\\
3
\end{bmatrix}
\end{align*}
$$

Bu durumda:

$$
1c_1 + 2c_2 = 7 \\
4c_1 + 5c_2 = 4 \\
6c_1 + 8c_2 = 3
$$

verilen sistem, aşağıdaki genişletilmiş matris ile ifade edilmekte;

$$
\begin{bmatrix}
v_1 & v_2 & | & y
\end{bmatrix}
$$

ardından bu matris formunu çözümleyerek $c$ değerleri bulunmaktadır.

### Genişletme (Span)

Bir $y$  vektörü, $v_1, v_2, ..., v_n$ vektörlerinin lineer kombinasyonu şeklinde yazılabiliyorsa, yani $y = c_1 \cdot v_1 + c_2 \cdot v_2 + ... + c_n \cdot v_n$ eşitliğini sağlayan skaler $c$ değerleri bulunabiliyorsa; bu durumda $y$ vektörü, _Span_{$v_1, v_2, ..., v_n$} kümesi içerisinde yer alır. Başka bir deyişle, $y$ vektörü $v$ vektörlerinin lineer birleşimi ile elde edebilmektedir.

### Lineer Bağımsızlık

Eğer 

$c_1 \cdot v_1 + c_2 \cdot v_2 + ... + c_n \cdot v_n = 0$ 

denkleminde yalnızca $c_1 = c_2 = \cdots = c_n = 0$ çözümü varsa, vektörler lineer bağımsızdır. Bu koşul sağlanmıyorsa, vektörler lineer bağımlıdır.

## Determinant

Bir matrisin determinantı, matrisin çeşitli özellikleri hakkında bilgi veren skaler bir değerdir.

### 2×2 Matrisin Determinantının Hesaplanması

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

### 3×3 Matrisin Determinantının Hesaplanması

Adımlar:

1. $X$ olarak tanımlanan 3x3 matrisin, herhangi bir satırı veya sütunu seçilir. 
2. Seçilen bu satır (veya sütun) üzerindeki değerlerin her biri için bulunduğu satır ve sütundaki değerleri çıkararak yeni 2x2'lik matris kalacak şekilde oluşan yeni yapının determinantı alınır. i satırının j sütunu için oluşturulan bu yeni matris $A_{ij}$ formatında oluşur.
3. Seçilen satırdaki tüm değerler için  $$(-1)^{i+j} \cdot det(A_{ij}) \cdot X_{ij}$$ hesaplanır ve bu değerleri toplandığında $X$ matrisi için determinant hesaplanmış olur.


## Özdeğer ve Özvektör (Eigenvalue/Eigenvector)

$$
\begin{align*}
\det\begin{pmatrix} 
A - \lambda \cdot I
\end{pmatrix} 
=0 
\end{align*}
$$

eşitliğini sağlayan $\lambda$ değerleri **özdeğer** olarak tanımlanmaktadır.

Örnek:

$$
\begin{bmatrix}
1 & 6 \\
5 & 2
\end{bmatrix}
$$

matrisi için özdeğerler _7_ ve _-4_ olur. Burada $$A - \lambda \cdot I$$ matrisinde özdeğerlerden biri, diğerinin yerine konulduğunda sütunlar birbirinin katı formunda olur. Başka bir deyişle, sütunlar vektör olarak değerlendirildiğinde; vektörlerin doğrultuları aynı olur.

Bu matris için özdeğerlerden biri yerine konulduğunda, $A - \lambda I$ ifadesiyle elde edilen matrisin sütunları lineer bağımlı hâle gelmektedir. Bu sütunlardan biri, ilgili özdeğere karşılık gelen özvektörün doğrultusunu temsil edebilir. Benzer şekilde, diğer özdeğer için aynı işlem uygulanarak ikinci özvektör elde edilebilir; ancak **bu durum yalnızca 2 × 2 matrisler için geçerlidir.** _(Aşağıdkai ['Ekleme'](https://github.com/xxJuniOrCoderxx/veri-bilimi-calisma-notlari/blob/main/MuratAtaToyran_Expressway_to_Data_Science_Essential_Math/Essential_Linear_Algebra/readme.md#ekleme) kısmına bakınız)_ Bu özdeğerler $\lambda$ yerine konulduğunda elde edilen iki matris aşağıda gösterilmiştir:

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

Buradan da özvektörler aşağıdaki gibi elde edilir:

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

-------------------------------------
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

Bir matris için verilen vektörün; özvektör olup olmadığı $$A \cdot v = \lambda \cdot v$$ formülüyle de hesaplanabilmektedir. Örneğin:

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

Özdeğeri bilinen bir matrisin özvektörünü bulmak için, 

$$[A - \lambda \cdot I] \cdot v = 0$$ 

eşitliğini sağlayan $v$ vektörü, lineer denklem sistemlerinin matris temelli çözümleri aracılığıyla elde edilebilir.
Dikkat çekici bir durum ise, önceki örnekte özvektörlerden birinin oluşturulmasında $\lambda = 7$ özdeğeri üzerinden işlem yapılmış olmasına rağmen,

$$A \cdot v = \lambda \cdot v$$ 

eşitliğini bu özvektör için $\lambda = -4$ değeri sağlamaktadır. Benzer şekilde, diğer özvektör için bu denklem $\lambda = 7$ ile sağlanırdı.
Bu farklılık, özvektörlerin her özdeğere özgü olduğunu ve doğru eşleşmenin yalnızca ilgili özdeğerle yapılması gerektiğini göstermektedir. Konuyla ilgili detaylı açıklama, yukarıda belirtilen ['Ekleme'](https://github.com/xxJuniOrCoderxx/veri-bilimi-calisma-notlari/blob/main/MuratAtaToyran_Expressway_to_Data_Science_Essential_Math/Essential_Linear_Algebra/readme.md#ekleme) bölümünde sunulmuştur. Ayrıca, konuya ilgi duyanlar [bu videoyu](https://www.youtube.com/watch?v=1sDBruay100) da inceleyebilir.

Ayrıca aşağıdaki yöntemi de inceleyebilirsiniz:
![image](https://github.com/user-attachments/assets/4927bbec-3aba-4726-8147-b4f895c8923d)

## Transpoz ve İç Çarpım (Inner Product/Dot Product)

- Bir matrisin transpozesini elde etmek için satırlar sütun, sütunlar ise satır olarak yeniden yazılır. Diğer bir ifadeyle, matrisin sol üst köşesi sabit kalacak şekilde elemanlar simetrik olarak yer değiştirir. Bu işlem sonucunda elde edilen matris, $A^T$ biçiminde gösterilir:

Örneğin $A$: 

$$
\begin{bmatrix}
1 & 6 & 3\\
5 & 2 & 4
\end{bmatrix}
$$

buna göre $A^T$: 

$$
\begin{bmatrix}
1 & 5\\
6 & 2 \\
3 & 4
\end{bmatrix}
$$

- İç çarpım işlemi iki vektörün aynı konumdaki bileşenlerinin çarpılıp toplanmasıyla elde edilir. Örneğin:

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

İç çarpım işlemi, ilk vektörün transpozu ile ikinci vektörün matris çarpımı biçiminde de ifade edilebilir:

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

## Vektörün Normu (Uzunluğu)

Bir vektörün normu, yani uzunluğu, vektörün kendisiyle iç çarpımının karekökü alınarak bulunur. Örneğin aşağıdaki vektör ele alındığında:

$$
\begin{bmatrix}
1 \\
6 \\
3
\end{bmatrix}
$$

Normu şu şekilde hesaplanır:

$$
\begin{align*}
\begin{Vmatrix}
A
\end{Vmatrix}
= \sqrt{1^2 + 6^2 + 3^2}
= \sqrt{46}
\end{align*}
$$

📌 **Not:** Bir vektörle aynı doğrultuda ancak birim uzunlukta (normu 1 olan) bir vektör elde etmek için, vektörün her bir bileşeni kendi normuna bölünür:

$$\frac{A}{\begin{Vmatrix}
A
\end{Vmatrix}}$$ 

Bu işlem sonucunda elde edilen vektör, ilgili birim vektördür.

## İki Vektör Arasındaki Uzaklık

İki vektör arasındaki Öklidyen uzaklık:

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
&arasındaki&uzaklık& \sqrt{(-1)^2 + 4^2} =\sqrt{17} & şeklinde bulunur.
\end{align*}
$$

## Dik Vektörler (Orthogonal Vectors)

1. Eğer $u$ ve $v$ vektörleri dik ise iç çarpımları 0 olur.
2. Eğer $u$ ve $v$ vektörleri dik ise $$norm(u+v)^2=norm(u)^2+norm(v)^2$$ olur.
3. İki vektörün iç çarpımı, normlarının çarpımı ile aralarındaki açının kosinüsünün çarpımına eşittir.

$u \cdot v = ||u|| \cdot ||v|| \cdot cos(θ)$

## Dik Yansıtmalar(Orthogonal Projections)

_y vektörünün u vektörü üzerine yansıtılması örneğini aşağıda görebilirsiniz:_

![IMG_1899](https://github.com/user-attachments/assets/d10b2a54-b46a-4321-847e-ead8893a5069)

## En Küçük Kareler Yöntemi (Least Squares Method)

$A \cdot x = b$ lineer denklem sisteminde çözümü bulunmayan matrisler için en küçük kareler metodunu kullanılmaktadır. Mantığı eşitliğin her iki tarafını sol taraftan önce $A^T$ ile daha sonra $(A^T \cdot A)^{-1}$ ile çarpma sonucunda $x = (A^T \cdot A)^{-1} \cdot A^T \cdot b$ eşitliğinin elde edilmesine dayanmaktadır. Bu hesaplama, yaklaşık bir çözüm sunmaktadır.

_Örnek:_

<img width="1402" height="856" alt="image" src="https://github.com/user-attachments/assets/17b11d80-92c1-4ca3-aa4b-ba76011fd1fa" />

