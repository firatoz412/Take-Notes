import os

File_Name = "notes.txt"

def load_notes():
    if not os.path.exists(File_Name):#File_Name adlı dosya yok ise
        return []#boş liste döndürsün 
    with open(File_Name,"r",encoding="utf-8") as file:
        return [satir.strip() for satir in file.readlines()]
        
   
def not_ekle():
    note_write = input("Eklemek istediğiniz notu yazınız: ")
    with open(File_Name,"a",encoding="utf-8") as file:
            file.write(f"{note_write}\n")
    print("Notunuz eklendi ")

def not_listele():
    if not os.path.exists(File_Name):
        return
    with open(File_Name,"r",encoding="utf-8") as file:
        notes = file.readlines()
        if not notes:
            print("henüz not eklemediniz \n")
            return
        print("\n -----Notlarınız-----")
        for i, notlar in enumerate(notes,start=1):
            print(f"{i}. {notlar.strip()}")
        print("---------------------\n")

        
        
def not_sil():
    not_listele()#silmek istediğimiz notu seçmek için önce notları görmemiz lazım.
    if not os.path.exists(File_Name):
        print("silinecek not bulunamadı.")
        return
    with open(File_Name,"r",encoding="utf-8") as file:
        notes = file.readlines()
        try:
            secim = int(input("silmek istediğiniz not numarasını giriniz"))
            if 1 <= secim <= len(notes):#kullanıcının gireceği not numarası,not listesindeki numaralarda biri olmalı onu sınırlandırıyoruz.3 notumuz olsun kullanıcı...
                silinen = notes.pop(secim-1)
                with open(File_Name,"w",encoding="utf-8") as file:
                    file.writelines(notes)
                print(f"'{silinen.strip()}' notunu sildiniz")
            else:
                print("geçersiz numara girdiniz.lütfen menüdeki not numaranızı kontrol edin.")#4 nolu notu girerse bu else bloğu çalışır.
        except ValueError:
                print("lütfen sadece rakam ya da say giriniz.metin karakterleri kullanmayınız.")
                

def delete_all_notes():
    if not os.path.exists(File_Name):
        print("silinecek not bulunamadı... \n")
        return
    
    silme_onayi = input("bütün notlar geri dönüşüm kutusuna taşınacak emin misiniz?evet ise e ye,iptal etmek istiyorsanız h ye basın(e/h)")
    
    if silme_onayi.lower() != "e":
        print("silme işlemi iptal edildi.\n")
        return
    
    with open(File_Name,"w",encoding="utf-8"):
        pass
    
    print("bütün dosyalar geri dönüşüm kutusuna taşındı.\n")
    

def edit_note():
    not_listele()
    if not os.path.exists(File_Name): 
        print("düzenlenecek not bulunamadı!")   
        return   

    with open(File_Name,"r",encoding="utf-8") as file:
        notes = file.readlines()
        
        if not notes:
            print("Henüz not eklemediniz.\n")
            return
    try:
        secim = int(input("Düzenlemek istediğiniz not numarasını giriniz: "))
        if 1 <= secim <= len(notes):
            eski_not = notes[secim - 1].strip()
            print(f"\nŞu anki not: {eski_not}")
            yeni_not = input("Yeni notu yazın: ")
                
            if yeni_not.strip():#Boş not kontrolü
                notes[secim - 1] = yeni_not + "\n"
                with open(File_Name, "w", encoding="utf-8") as file:
                    file.writelines(notes)
                print(f"Not düzenlendi!\n")
            else:
                print("Boş not eklenemez!\n")
        else:
            print("Geçersiz numara girdiniz.\n")
    except ValueError:
            print("geçersiz işlem.\n")
    
        

def main():
    print("-----Not alma uygulamasına hoşgeldiniz-----")
    print("Yapmak istediğiniz işlemi seçiniz: ")
    while True:
        print("not eklemek için ==> 1")
        print("notları listelemek için == > 2")
        print("not silmek için ==> 3")
        print("bütün notları silmek için ==> 4")
        print("Herhangi bir notunuzu düzenlemek için ==> 5")
        print("çıkış için ==> 0")
        secim = input("Yapmak istediğiniz işlemi seçin: ")
        
        if secim == "1":
            not_ekle()
        elif secim == "2":
            not_listele()
        elif secim == "3":
            not_sil()
        elif secim == "4":
            delete_all_notes()
        elif secim == "5":
            edit_note()
        elif secim == "0":
            print("çıkış yapıldı.")
            break
        else:
            print("geçersiz seçim, tekrar deneyin")
            
    
if __name__ == "__main__":
    load_notes()
    main()
            
        
        