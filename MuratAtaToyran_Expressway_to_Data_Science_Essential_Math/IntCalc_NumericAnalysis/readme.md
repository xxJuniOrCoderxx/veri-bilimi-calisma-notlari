# İntegral

Bir fonksiyonun altında kalan alanı hesaplamak için fonksiyonun altındaki alanı geometrik bir şekilmiş gibi düşünüp formüllerle hesaplama yapabiliriz. Formülün altında kalan alan dikdörtgen, üçgen gibi basit şekillerse bunu yapabiliriz. Peki $x^2$ gibi karmaşık bir fonksiyonun altında kalan alanı nasıl hesaplarız? Bunu da integral sayesinde yaparız. 

Fonksiyonun altında kalan alanı N tane eşit aralıklı dikdörtgen parçaya bölüp bu dikdörtgenlerin alanlarını toplayalım. N sayısı arttıkça eğri altında kalan alanı daha doğru hesaplarız. N sonsuza gittikçe tam çözüme ulaşmış oluruz ve bu da integralin tanımıdır.

![image](https://github.com/user-attachments/assets/73437c55-f7c5-49ee-a46a-1c2b9326d12c)

İntegral hesaplarken temel kuralları bilmemiz gerekir:

1. F(x) fonksiyonunun türevi f(x) olsun (dolayısıyla F(x) fonksiyonu, f(x) fonksiyonunun anti-türevi olmuş olur). $\int f(x) \ dx$ = F(x) + c olur (c sabit sayı).
2. $$\int_{a}^{b} f(x) \ dx$$ = F(b) - F(a) olur.

-----------------------
**Aşağıdaki örnekte a'dan b'ye integral alırsanız ($$\int_{a}^{b} f(x) \ dx$$) bulacağınız sonuç $A_1 - A_2$ olur.**

![image](https://github.com/user-attachments/assets/c939fb35-25e9-4625-b572-abfe31123709)

**Not:** Karmaşık integralleri hesaplamak için parçalı integral metodunu kullanırız. Parçalı integral ispatı türevden gelir:

$$(u \cdot v)' = u \cdot v' + v \cdot u' $$
$$\int (u \cdot v)' \  = u \cdot v = \int u \cdot v' \ + \int v \cdot u' \ $$
$$\int u \cdot v' \  = u \cdot v - \int v \cdot u' \ $$

# Nümerik Analiz

### İkiye Bölme Metodu
$$f(a) \cdot f(b) < 0$$ olmak üzere a ve b noktaları seçeriz. Bu iki noktanın ortasını alırız (c). f(c) değeri bu ikisinden hangisi ile çarpıldığında negatif olursa ona göre aralığı belirleriz. Örneğin f(a) ile çarpıldığında negatif değer verirse a ile c aralığı için ayısını yaparız ve bu şekilde sonsuza kadar giderek köke yaklaşırız. Bu metod en yavaş metoddur. Ayrıca fonksiyon sürekli pozitif veya sürekli negatif değerler aldığında bu metod işe yaramaz.

### Newton-Raphson Metodu

Seçilen bir başlangıç noktasından teğet çekerek o teğetin x eksenini kestiği noktayı bulup o x değerine de başlangıç noktasına yaptıklarımızı tekrarlı şekilde yaptığımız bir köke yaklaşma metodudur.

➡ Önce bir başlangıç noktası $(x_0)$ seçeriz. Sonraki yeni x değeri $$x_0 - \frac{f(x_0)}{f'(x_0)}$$ olur. Daha sonra bulduğumuz yeni x değerini formülde $(x_0)$ yerine koyup sonraki x değerini buluruz ve bu şekilde köke yaklaşırız.

Köke yaklaşmada en güçlü ve en hızlı metod budur ama dikkat etmemiz gereken bir şey var. Başlangıç noktasını çözüme olabildiğince yakın seçmeliyiz. Eğer başlangıç noktasını çözümden uzak seçersek kökten uzaklaşabilir ve çözümü bulamayabilir. [Bu videoya](https://www.youtube.com/watch?v=d4TtDbC0zEo) da göz atabilirsiniz.

## Diyagonalizasyon

D matrisi içindeki değerler, $D_{ii}$ değerleri dışında 0 ise D matrisi diyagonal matristir. Yani aşağıdaki gibidir:

$$
\begin{bmatrix}
a & 0 & 0\\
0 & b & 0\\
0 & 0 & c
\end{bmatrix}
$$

Bu matrisin kuvvetini $(D^k)$ aldığımızda aşağıdaki gibi olur:

$$
\begin{bmatrix}
a^k & 0 & 0\\
0 & b^k & 0\\
0 & 0 & c^k
\end{bmatrix}
$$

***Diyagonalizasyon nedir, nasıl yapılır peki?*** Bir A matrisimiz olsun. Bu A matrisi için öyle bir P matrisi ve öyle bir diyagonal D matrisi vardır ki $A = P \cdot D \cdot P^{-1}$ eşitliğini sağlar ve A matrisini bu formatta yazabiliriz. Bunun bize sağladığı asıl kolaylık, A matrisinin kuvvetini $(A^k)$ almak istediğimizde eşitliği $A^k = P \cdot D^k \cdot P^{-1}$ formatında düzenleyip A'nın kuvvetini kolayca alabilmemizdir.

***Peki P ve D matrislerini nasıl buluruz?*** Bunun için özdeğer ve özvektörlerden yararlanırız. Her $\lambda_i$ özdeğeri için belli bir $v_i$ özvektörü vardır. P ve D matrisleri de aşağıdaki şekilde oluşur:

$$
\begin{align*}
P=
\begin{bmatrix}
v_1 &
v_2 &
v_3
\end{bmatrix}
&&&&&&
D=
\begin{bmatrix}
\lambda_1 & 0 & 0\\
0 & \lambda_2 & 0\\
0 & 0 & \lambda_3
\end{bmatrix}
\end{align*}
$$

***Aşağıdaki örneğe göz atın:***

![image](https://github.com/user-attachments/assets/e36dbb73-40fd-42b4-8710-baa6e42cec11)

🥇 _Not:_ Şunu bilmemiz gerekir ki A matrisinin kare matris olmaması veya diyagonalize edilemeyecek kadar az özvektöre sahip olması gibi durumlar, diyagonalizasyonun çalışmadığı durumlardır.

***Simetrik matrisler***, transpozu kendisine eşit olan matrislerdir $(A^T=A)$, yani tanım gereği kare matris olmaları gerekir. Simetrik matrislere diyagonalizasyon uyguladığımızda P matrisi ile ilgili ilginç bir şey gözlemleriz, P matrisinin bütün sütunları birbirine dik, yani P matrisi ortagonal bir matris, yani A matrisinin özvektörleri birbirine dik. Daha da ilginç ve işlerimizi kolaylaştıran bir şey daha var, A matrisinin tüm özvektörlerini birim vektör haline getirirsek *(ki buna ortanormal hale getirmek denir)*, yani vektörleri normlarına bölersek ve bu vektörlerle P matrisini  oluşturursak P matrisinin tersi transpozuna eşit olmuş olur $(P^T=P^{-1})$.

![image](https://github.com/user-attachments/assets/f2374716-0393-452f-8715-60168dc06a97)

## Tekil Değer Ayrışımı(SVD)

Her A matrisine diyagonalizasyon yapamadığımız için tekli değer ayrışımı gibi ek ayrışımlara ihtiyaç duyarız.

***Peki  nasıl çalışır?*** Bir $A_{n \times p}$ matrisimiz olsun. Bu $A_{n \times p}$ matrisi için öyle bir $U_{n \times n}$ matrisi, öyle bir $V_{p \times p}$ matrisi ve öyle bir diyagonal(?) $\Sigma_{n \times p}$ matrisi vardır ki $A = U \cdot \Sigma \cdot V^T$ eşitliğini sağlar ve A matrisini bu formatta yazabiliriz.

***Peki U, V ve Σ matrislerini nasıl buluruz?*** Önce $A \cdot A^T$ matrisini bulalım (dikkat ederseniz bu matrisin simetrik olduğunu görebilirsiniz). Bulduğumuz matrisin özdeğer ve özvektörlerini bulalım. Matrisimiz simetrik olduğundan özvektörler ortagonal olacaktır, bunları ortanormal hale getirelim. Her $\lambda_i$ özdeğeri için belli bir $v_i$ özvektörü olduğuna da dikkat ederek sütunlar halinde V matrisini oluşturalım. Sonrasında özdeğerlerin köklerini $(\sigma_i = \sqrt{\lambda_i})$ hesaplayıp özvektörlerin sırasına dikkat ederek $\Sigma$ matrisinde yerine koyalım. En son $u$ vektörlerini bulmak için $u_i = A \cdot \frac{v_i}{\sigma_i}$ formülünü uygulayıp U matrisinde yerine koyalım. $A_{2 \times 3}$ matrisinin tekil değer ayrıştırması için oluşturulacak matrisler aşağıdaki gibi olur:

$$
\begin{align*}
V=
\begin{bmatrix}
v_1 &
v_2 &
v_3
\end{bmatrix}
&&&&&&
\Sigma=
\begin{bmatrix}
\sigma_1 & 0 & 0\\
0 & \sigma_2 & 0
\end{bmatrix}
&&&&&&
U=
\begin{bmatrix}
u_1\\
u_2
\end{bmatrix}
\end{align*}
$$


| Durum                                       | Diyagonalizasyon | SVD   |
| ------------------------------------------- | ---------------- | ----- |
| Kare olmayan matrisler                      | ❌                | ✅     |
| Defektif matrisler                          | ❌                | ✅     |
| Sayısal kararlılık (nümerik analiz)         | Zayıf            | Güçlü |
| Gürültülü verilerle çalışmak (PCA, LSA vb.) | ❌                | ✅     |
| Her matris için çalışır mı?                 | ❌                | ✅     |
