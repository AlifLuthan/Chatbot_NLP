import re
#Module re saya gunakan untuk membuat pola pencarian untuk pemanggilan Variable yang saya buat.
import random
#Module random digunakan agar dapat menggunakan Pemilihan secara asal , namun ketika saya menggunakannya
#untuk 1 pilihan itu tidak mengacak dan mengambil int dari variable yang saya tambahkan


interaksi1 = ["Hai,Aku Robod! Siapa Kamu ?"]
interaksi2 = ["Senang berkenalan dengan kamu :D ,Apa Jenis Kelamin Kamu ? "]
interaksi3 = ["Hebat, Sekarang Kamu Sibuk Apa Nih?"]
interaksi4 = ["Senang Mendengarnya,Semoga Kamu selalu Semangat Menjalankan Profesimu itu. Berapa Usiamu ?"]
interaksi5 = ["Sama-Sama"]
interaksi6 = ["Senang Mendengarnya,Semoga Kamu selalu Semangat dan Panjang Umur ^_^"]
interaksi7 = ["Program ini memang sedang di Kembangkan, Namun Anda dapat memulai dengan Sapaan yang Hangat"]
interaksi8 = ["Terimakasih telah menggunakan Bot ini, Masukan dan Saran Dapat disampaikan ke Telegram @okelip"]
#Interaksi diatas Merupakan Output dari Input yang kita masukan dalam Program

print("=====================================================================")
print("Selamat Datang, Terimakasih Telah menggunakan Chabot Robod ini")
print("Salam hangat dari Dev")
print("=====================================================================")
print("*********************************************************************")
print("Untuk Memulai Chat Robod bisa menggunakan Sapaan yang Ramah")
print("*********************************************************************")
while True: # Perulangan dibuat ketikan inputan sebelumnya Kondisinya adalah True , maka Program akan berjalan
    konsol = input("User\t:  ") #Input
    if re.findall(r'Halo|Hai|p|woy|hai|halo|Assalamualaikum|yo', konsol): # Jika ada kata yang ada dalam () maka
        print("Robod\t:" , random.choice(interaksi1)) # Jalankan atau mencetak Interaksi1
    elif re.findall(r'Ahmad|Rio|Alif|Luthan|ahmad|rio|alif|luthan' , konsol):# Jika ada kata yang ada dalam () maka
        print("Robod\t:" , random.choice(interaksi2)) # Jalankan atau mencetak Interaksi2
    elif re.findall(r'wanita|Laki|Wanita|laki|cowok|cewek', konsol):# Jika ada kata yang ada dalam () maka
        print("Robot\t:" , random.choice(interaksi3)) # Jalankan atau mencetak Interaksi3
    elif re.findall(r'Bekerja|bekerja|kuliah|Kuliah|Tidak bekerja|tidak bekerja|gawe|kerja|nguliah', konsol):# Jika ada kata yang ada dalam () maka
        print("Robot\t:" , random.choice(interaksi4)) # Jalankan atau mencetak Interaksi4
    elif re.findall(r'thanks|terima kasih|ty|Terima Kasih|terimakasih' , konsol):# Jika ada kata yang ada dalam () maka
        print("Robod\t:" , random.choice(interaksi5)) # Jalankan atau mencetak Interaksi5
    elif re.findall(r'17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40' , konsol):# Jika ada kata yang ada dalam () maka
        print("Robod\t:" , random.choice(interaksi6)) # Jalankan atau mencetak Interaksi6
    elif re.findall(r'test|Testing|testt|tesst|teest|ttest' , konsol):# Jika ada kata yang ada dalam () maka
        print("Robod\t:" , random.choice(interaksi7)) # Jalankan atau mencetak Interaksi7
    elif re.findall(r'end|selesai|quit|exit' , konsol):# Jika ada kata yang ada dalam () maka
        print("Robod\t:", random.choice(interaksi8)) # Jalankan atau mencetak Interaksi8
        quit() # Memberhentikan Program
    else: # Jika tidak ada kata yang ada dalam () maka 
        print("Bot\t: Maaf, Aku tidak mengerti :(") # Mencetak Interaksi berikut


#Noted
#masih banyak kekurangan dalam Program ini , Niatnya Kedepannya saya akan membuat GUI menggunakan
#module yang tersedia dan mencari cara dan sumber dalam internet.