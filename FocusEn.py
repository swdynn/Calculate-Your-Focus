import time

dersbaslat = (input("To start the lesson type 'start' (Typing 'stop' will close this program): "))

if dersbaslat == "start":
    print("After 10 minutes you will get a message that will ask if you want to have break")
    Derscalismasuresi = 0
    dersbitir = "Not Finished"
    arazamani = 0
    loopend = 0
    devam = "Hayır"
    emin = "continue"
    
    while True:
        
        
        time.sleep(0.5)
        
        
        
        if dersbitir == "Not Finished":
            if emin == "continue":
                for i in range(Derscalismasuresi, Derscalismasuresi+600):
                    Derscalismasuresi += 1
                    time.sleep(0.5)
                    print(Derscalismasuresi)
        if dersbitir == "Finished":
            emin = (input("Are you sure if write 'im sure' then the break will begin(Writing 'continue' will start the counter): "))       
            if emin == "im sure":
                print("Break started")
                kacdk = int(input("How many Minutes: "))
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
                        
                        print(f"Your Focus Result ")
                        print(derscalismaara)
                        
                        if derscalismaara > 80:
                            print("Go like This")
                            break
                        elif derscalismaara > 60:
                            print("eh its average")
                            break
                        else:
                            print("u should study more")
                            loopend = 1
                            break
            elif emin == "continue":
                dersbitir = "Not Finished"
                
                

        # else:
        #     print("True yada False yazmalısın")
        #     break 

                    
        
        if loopend != 1:
            dersbitir = (input("When your lesson finishes write 'Finished'(writing 'Not finished' will make this message dissapear for 10 minutes): "))
        else:
            print(":<)")
            break
elif dersbaslat == "stop":
    print(":<)")        

else:
    print("You have to write 'start' or 'stop'")         

        
