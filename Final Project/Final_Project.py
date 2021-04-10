import random as rn

#Bilgi yarışması programı

#Sorular rastgele sırayla sorulur
#Cevap büyük-küçük harfe duyarlıdır.
#Her soru için 3 cevap hakkı vardır.
#Her sorunun sadece 1 cevabı vardır.
#Her soru 10 puan değerindedir.

#Sorular bu sitelerden alınmıştır:
#https://www.iyigunler.net/nedir/bilgi-yarismasi-soru-ve-cevaplari-kolay-sorular-kolay-cevaplar-h341280.html

def sor(sorudic):
    soru, cevap = sorudic["q"],sorudic["a"]
    print(soru)
    for i in range(1,4):
        ans = input("["+str(4-i)+" hakkınız kaldı] Cevabınızı yazın:")
        if ans==cevap:
            print("Bildiniz! «+10 Puan»")
            return True
        else:
            print("Cevabınız doğru değil.")
        

questions = [{"q":"Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu tepesi nerededir?","a":"Yeni Zelanda"},
             {"q":"Dünyanın en büyük deniz kazalarından biri olarak tarihe geçen, 1912 yılında 1.550 kişiye mezar olan ünlü transatlantiğin adı nedir?","a":"Titanik"},
             {"q":"\"Lakin\" ve \"fakat\" kelimelerinin eş anlamlısı nedir?","a":"Ama"},
             {"q":"Belli bir süre eğitimi tamamladıktan sonra alınan, sir okul ya da eğitim kurumu tarafından verilen belgenin adı?","a":"Diploma"},
             {"q":"TC kimlik numaramız kaç harften oluşur?","a":"11"},
             {"q":"Savaşlarda düşmandan elde edilen eşya araç ve başka mallara ne ad verilir?","a":"Ganimet"},
             {"q":"Mustafa Kemal Atatürk, 19 Mayıs 1919 tarihinde hangi vapurla Samsun'a gitmiştir?","a":"Bandırma"},
             {"q":"Yerel Seçimler kaç yılda bir yapılır?","a":"5"},
             {"q":"Ölenden geriye kalan mal veya para","a":"Miras"},
             {"q":"Kurutulmuş yaprakları demlendirilerek içilen bitkiye ne ad verilir?","a":"Çay"}]


#Açılış ekranı
print("Bilgi yarışmasına hoş geldiniz.")
uname = input("Başlamadan önce kullanıcı isminizi giriniz: ")
print("İlk soruyla başlayalım. Bol şans!")



puan = 0



sorulmayan = questions.copy()
while (len(sorulmayan)>1): #Tüm sorular sorulana kadar tekrarlıyoruz
    
    i = rn.randint(0,len(sorulmayan)-1) #Soru seçme işlemi
    ans = sor(sorulmayan[i]) #Soruyu sorma

    #Sorunun cevabına göre işlem yapmak
    if ans:
        puan += 10

    #Aynı soruyu tekrar sormamak için soruyu listeden kaldırıyoruz.
    sorulmayan.pop(i)

#Puanına göre kullanıcıyı değerlendirmek.

if puan>5:
    print("Tebrikler",uname+"! Oyunu başarıyla bitirdiniz. Puanınız:",puan)
else:
    print("Oyunu başarıyla tamamlayamadınız, ama tekrar deneyebilirsiniz!")
    print("Bu arada puanınız:",puan)
