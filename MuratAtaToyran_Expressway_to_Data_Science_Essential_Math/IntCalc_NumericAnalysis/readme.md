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

▶️ Önce bir başlangıç noktası seçeriz. $(x_0)$
▶️ Sonraki yeni x değeri $$(x_0) - \frac{f(x_0)}{f'(x_0)} olur.
▶️ Daha sonra bulduğumuz yeni x değerini formülde $(x_0)$ yerine koyup sonraki x değerini buluruz ve bu şekilde köke yaklaşırız.

Köke yaklaşmada en güçlü ve en hızlı metod budur ama dikkat etmemiz gereken bir şey var. Başlangıç noktasını çözüme olabildiğince yakın seçmeliyiz. Eğer başlangıç noktasını çözümden uzak seçersek kökten uzaklaşabilir ve çözümü bulamayabilir.

## Diyagonalizasyon

D matrisi, $D_ii$ değerleri dışında 0 ise diyagonal matristir. Yani aşağıdaki gibidir:

$$
\begin{matrix}
a & 0 & 0\\
0 & b & 0\\
0 & 0 & c
\end{matrix}
$$
