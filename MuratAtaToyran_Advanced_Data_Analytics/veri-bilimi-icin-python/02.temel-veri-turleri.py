# =======================================================
# PYTHON DERS 2: TEMEL VERİ TÜRLERİ
# =======================================================

# Bir önceki derste matematiksel işlemleri öğrendik.
# Bu derste Python'da hangi türde veriler saklayabileceğimizi öğreneceğiz.

# Öğreneceğiniz veri türleri:
#   1. int (Tam sayılar)
#   2. float (Ondalıklı sayılar) 
#   3. str (Metinler)
#   4. bool (Mantıksal değerler)

# type() fonksiyonu bir verinin hangi türde olduğunu gösterir.

print("Python Veri Türleri Dersine Hoş Geldiniz!")


# =======================================================
# 1. TAM SAYILAR (int)
# =======================================================
print("1. TAM SAYILAR (int)")
print("---------------------")

# Tam sayılar pozitif, negatif veya sıfır olabilir
sayi1 = 42        # Pozitif tam sayı
sayi2 = -15       # Negatif tam sayı  
sayi3 = 0         # Sıfır

print("Pozitif tam sayı:", sayi1)
print("Negatif tam sayı:", sayi2)
print("Sıfır:", sayi3)

# type() fonksiyonu ile veri türünü kontrol edebiliriz
print("sayi1'in türü:", type(sayi1))
print("sayi2'in türü:", type(sayi2))

print("Tam sayılar konusu tamamlandı!")


# =======================================================
# 2. ONDALIKLI SAYILAR (float)
# =======================================================
print("2. ONDALIKLI SAYILAR (float)")
print("------------------------------")

# Ondalıklı sayılar nokta ile yazılır
pi = 3.14159      # Pi sayısı
sicaklik = -5.2   # Negatif ondalıklı sayı
yukseklik = 175.5 # Pozitif ondalıklı sayı

print("Pi sayısı:", pi)
print("Sıcaklık:", sicaklik)
print("Yükseklik:", yukseklik)

# type() ile kontrol edelim
print("pi'nin türü:", type(pi))
print("sicaklik'in türü:", type(sicaklik))

print("Ondalıklı sayılar konusu tamamlandı!")


# =======================================================
# 3. METİNLER (str)
# =======================================================
print("3. METİNLER (str)")
print("-----------------")

# Metinler tek veya çift tırnak içinde yazılır
isim = "Ahmet"           # Çift tırnak
soyisim = 'Yılmaz'       # Tek tırnak
mesaj = "Merhaba Dünya!" # Uzun metin
bos_metin = ""           # Boş metin

print("İsim:", isim)
print("Soyisim:", soyisim)
print("Mesaj:", mesaj)
print("Boş metin:", bos_metin)

greet1 = "Hello"
greet2 = "world"
print(greet1 + " " + greet1)

# type() ile kontrol edelim
print("isim'in türü:", type(isim))
print("mesaj'ın türü:", type(mesaj))

# string slice
new_string = 'pining for the fjords'
print(new_string[5:20])
print(new_string[6:])
print(new_string[:15])
print(len(new_string))

# String format

x = 'values'
y = 100
print('''String formatting lets you insert {} into strings.
They can even be numbers, like {}.'''.format(x, y))

var_a = 'A'
var_b = 'B'
print('{a}, {b}'.format(b=var_b, a=var_a))
print('{1}, {0}'.format(var_a, var_b))
print('{0}, {1}'.format(var_a, var_b))

print('{0}{1}{0}'.format('abra', 'cad'))

var_a = 1
var_b = 2
print(f'{var_a} + {var_b}')
print(f'{var_a + var_b}')
print(f'var_a = {var_a} \nvar_b = {var_b}')

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, (x-32) * 5 / 9))

num = 1000.987123
print(f'{num:.2f}')
print(f'{num:.3e}')
print(f'{num:.4%}')

my_string = 'Happy birthday'
print(my_string.count('y'))
print(my_string.count('y', 2, 7))
my_string.find('birth')

separator_string = ' '
iterable_of_strings = ['Happy', 'birthday', 'to', 'you']
separator_string.join(iterable_of_strings)

# Daha fazla string metodu için dokümantasyona bakın.
print("Metinler konusu tamamlandı!")

# =======================================================
# 4. MANTIKSAL DEĞERLER (bool)
# =======================================================
print("4. MANTIKSAL DEĞERLER (bool)")
print("------------------------------")

# Mantıksal değerler sadece True (Doğru) veya False (Yanlış) olabilir
# DİKKAT: True ve False büyük harfle yazılır!
dogru = True      # Doğru değer
yanlis = False    # Yanlış değer

print("Doğru değer:", dogru)
print("Yanlış değer:", yanlis)

# type() ile kontrol edelim
print("dogru'nun türü:", type(dogru))
print("yanlis'ın türü:", type(yanlis))

# Mantıksal değerler genellikle karşılaştırmalarda kullanılır
# Örnek: Bir sayının büyük olup olmadığını kontrol etmek
sayi = 15
buyuk_mu = sayi > 10  # 15 > 10 True'dur
print("15 sayısı 10'dan büyük mü?", buyuk_mu)
print("Sonucun türü:", type(buyuk_mu))

print("Mantıksal değerler konusu tamamlandı!")


# =======================================================
# 5. VERİ TÜRLERİNİ KARŞILAŞTIRMA
# =======================================================
print("5. VERİ TÜRLERİNİ KARŞILAŞTIRMA")
print("--------------------------------")

# Aynı değerde farklı türlerde veriler oluşturalım
tam_sayi = 5        # int türünde 5
ondalik_sayi = 5.0  # float türünde 5.0
sayi_metni = "5"    # str türünde "5"

print("Tam sayı:", tam_sayi, "- Türü:", type(tam_sayi))
print("Ondalıklı sayı:", ondalik_sayi, "- Türü:", type(ondalik_sayi))
print("Sayı metni:", sayi_metni, "- Türü:", type(sayi_metni))

# Bu değerler farklı türlerde olsa da bazıları birbirine eşit olabilir
print("5 == 5.0 mi?", tam_sayi == ondalik_sayi)     # True
print("5 == '5' mi?", tam_sayi == sayi_metni)       # False

print("Veri türlerini karşılaştırma tamamlandı!")


# =======================================================
# DEĞİŞKEN İSİMLENDİRİRKEN NELERE DİKKAT ETMELİYİZ?
# =======================================================
print("sadece harf, sayı ya da alt çizgi içerebilir\n")
print("sadece harf ya da alt çizgi ile başlayabilir\n")
print("parantez içeremez\n")
print("büyük harf ve küçük harf farklı kabul edilir\n")
print("for, if, else gibi önceden alınmış fonksiyonları değişken ismi içinde kullanamazsın\n")

print("ayrıca değişkenin kolay okunabilmesine dikkat edin\n")


# =======================================================
# DERS ÖZET
# =======================================================
print("DERS ÖZETİ")
print("-----------")
print("Bu derste öğrendiğiniz veri türleri:")
print("1. int (Tam sayılar): 42, -15, 0")
print("2. float (Ondalıklı sayılar): 3.14, -5.2, 175.5")
print("3. str (Metinler): 'Merhaba', \"Python\"")
print("4. bool (Mantıksal değerler): True, False")
print("5. type() fonksiyonu: Veri türünü kontrol eder")

print("VERİ TÜRLERİ DERSİ TAMAMLANDI!")
print("Sonraki ders: Tip dönüşümlerini öğreneceğiz.")
