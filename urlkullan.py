import re
import urllib.request as url 

page = url.urlopen("https://www.tcmb.gov.tr/kurlar/today.xml")
text = page.readlines()

tarih = text[2]
tarihstring=tarih.decode("utf-8")
tarihstr=re.findall("\d+\.\d+", tarihstring)
tarihtam=tarihstring[19:29]

#Dolar çekme
dolar=text[8]
dolarstring=dolar.decode("utf-8")
dolarkuru=re.findall("\d+\.\d+", dolarstring)
dolarint = ' '.join(dolarkuru)

#Euro çekme

euro=text[44]
eurostring=euro.decode("utf-8")
eurokuru=re.findall("\d+\.\d+", eurostring)
euroint = ' '.join(eurokuru)

fiyat=float(input('Ürünün liste fiyatını giriniz (Para birimi hariç): '))
print('Lütfen işlem yapmak istediğiniz kuru seçiniz.')
birim=str(input('USD (U,u)  ,  Euro (E,e): '))

count=0 

while count == 0 :
    if birim in ["U" , "u"] :
        count = 1
        hesaplanan=float(fiyat)*float(dolarint)
    elif birim in ["E" , "e" ] :
        count=1
        hesaplanan=float(fiyat)*float(euroint)
    else :
        print("Girilen birim anlaşılmadı.")
        birim=input('USD (U,u)  ,  Euro (E,e) : ')

iskonto=float(input('İskonto tutarını giriniz: '))
hesaplanan = float(hesaplanan)*float(1-(iskonto/100))
print("\n")
print(str(tarihtam)+' - Günlük Kur Bilgisi')
print('USD/TRY : ' + '%.4f' %float(dolarint) + " - EUR/TRY : " + "%.4f" %float(euroint))
print("\n")
if birim in ["U" , "u"] :
    print("Ürün fiyatı: " + "%.2f" %fiyat + " USD")
elif birim in ["E" , "e" ] :
    print("Ürün fiyatı: " + "%.2f" %fiyat + " EUR")
print("Hesaplanan tutar: " + "%.3f" %hesaplanan + " TL" "  İskonto Tutarı = % " + "%.2f" %iskonto)