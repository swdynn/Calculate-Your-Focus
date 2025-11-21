import time

dersbaslat = (input("Ders Başlaması için 'Başlat' Yaz (Durdur yazmak programı kapatır): "))

if dersbaslat == "Başlat":
    print("10 dakika sonra sana ara vermek istermisin diye bir mesaj gelicek")
    Derscalismasuresi = 0
    dersbitir = "Bitmedi"
    arazamani = 0
    loopend = 0
    devam = "Hayır"
    emin = "Devam"
    
    while True:
        
        
        time.sleep(0.5)
        
        
        
        if dersbitir == "Bitmedi":
            if emin == "Devam":
                for i in range(Derscalismasuresi, Derscalismasuresi+600):
                    Derscalismasuresi += 1
                    time.sleep(0.5)
                    print(Derscalismasuresi)
        if dersbitir == "Bitti":
            emin = (input("Eminmisin Eğer Eminim Yazarsan Araya giriceksin ('Devam' yazmak sayacı devam ettrir): "))       
            if emin == "Eminim":
                print("Ara Başladı")
                kacdk = int(input("Kaç dakika boyunca: "))
                for a in range(0, kacdk*60):
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
            elif emin == "Devam":
                dersbitir = "bitmedi"
                
                

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

        
