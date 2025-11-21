import time

dersbaslat = (input("Ders Başlaması için 'Başlat' Yaz (Durdur yazmak programı kapatır): "))

if dersbaslat == "Başlat":
    Derscalismasuresi = 0
    dersbitir = "Bitmedi"
    arazamani = 0
    loopend = 0
    
    
    while True:
        
        
        time.sleep(0.5)
        
        
        
        if dersbitir == "Bitmedi":
            for i in range(Derscalismasuresi, Derscalismasuresi + 6):
                Derscalismasuresi += 1
                time.sleep(0.5)
                print(Derscalismasuresi)
        if dersbitir == "Bitti":
            emin = (input("Eminmisin Eğer Eminim Yazarsan Araya giriceksin ('Devam' yazmak sayacı devam ettrir): "))       
            if emin == "Eminim":
                print("Ara Başladı")
                kacdk = int(input("Kaç dakika boyunca: "))
                
                for a in range(0, kacdk*6):
                    b = kacdk*6
                    derscalismaara = 0
                    
                    arazamani = arazamani + 1
                    time.sleep(0.5)
                    print(arazamani)
                    if b == arazamani:
                        derscalismaara = Derscalismasuresi / arazamani * 4
                        if derscalismaara > 100:
                            derscalismaara -= derscalismaara
                            derscalismaara += 100
                        
                        print(f"Ders Çalışma Verin ")
                        print(derscalismaara)
                        
                        if derscalismaara > 80:
                            print("Böyle Devam ET")
                            break
                        elif derscalismaara > 60:
                            print("eh ortalama")
                            break
                        else:
                            print("Biraz daha çalış")
                            loopend = 1
                            break
        # else:
        #     print("True yada False yazmalısın")
        #     break 

                    
        
        if loopend != 1:
            dersbitir = (input("Dersin bittiği Zaman 'Bitti' yaz (Bitmedi yazmak bu mesajı On dakika boyunca durdurur): "))
        else:
            print(":<)")
            break
elif dersbaslat == "Durdur":
    print(":<)")        

else:
    print("Başlat Yada Durdur Yazmalısın")         

        
