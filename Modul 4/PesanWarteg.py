# ==================================
# Program memesan menu warteg
# Identitas Kelompok: 
# Yosua Evan Yudha (21120121120003)
# Valentinus Aryo Saputro (21120121140100)
# Putrandi Agung Prabowo (21120121130074)
# Rahmat Mukhalin (21120120130062)
# Kelompok: 21
# Shift: 2
# ==================================

def tidak_ada_uang():
    print("Maaf kamu tidak memiliki uang yang cukup")

print("----------- Warteg'21 -----------")

uang = int (input('Masukan jumlah uang anda : '))
makanan = ["Rendang",16000], ["Ayam Bakar",15000], ["Ayam Goreng", 15000], ["Nasi Goreng", 13000]
minuman = ["Teh Manis", 6000], ["Air Mineral", 3000], ["Teh Tawar", 5000], ["Jus Jeruk", 9000]
tambahan = ['pergedel', 2000], ['kerupuk', 1000]
bungkus = ['bawa pulang'], ['makan di tempat']
pesan_makanan = True
pesan_minuman = True
pesan_tambahan = True
pesan_bungkus = True

makananlen = len(makanan)
minumanlen = len(minuman)
tambahanlen = len(tambahan)
bungkuslen = len(bungkus)

#Print List Makanan
for i in range (makananlen):
    print(str(i+1) + ". " + makanan[i][0] + " (Rp." + str(makanan[i][1]) + ")")

while (pesan_makanan == True):
    choice1 = int(input("Pilih menu makanan yang diinginkan: "))
    if(choice1 > len(makanan)):
        print("Harap masukkan nomor orderan yang benar")
    else:
        totalchoice1 = int(input("Berapa banyak porsi yang ingin kamu beli? "))
        if(totalchoice1 >= 50):
            print("Maaf warteg kami tidak menyediakan porsi sebanyak itu")
        elif(uang >= (totalchoice1 * makanan[choice1-1][1])):
            uang = uang - (totalchoice1 * makanan[choice1-1][1])
            print("Kamu telah membeli menu " + makanan[choice1-1][0] + " sebanyak " + str(totalchoice1) + " porsi dan kamu memiliki sisa uang Rp." + str(uang))
            pesan_makanan = False
        else:
            tidak_ada_uang()

#Print List Minuman
for i in range (minumanlen):
    print(str(i+1) + ". " + minuman[i][0] + " (Rp." + str(minuman[i][1]) + ")")

while (pesan_minuman == True):
    choice2 = int(input("Pilih menu minuman yang diinginkan: "))
    if(choice2 > len(minuman)):
        print("Harap masukkan nomor orderan yang benar")
    else:
        totalchoice2 = int(input("Berapa banyak porsi yang ingin kamu beli? "))
        if(totalchoice2 >= 50):
            print("Mohon maaf warteg kami tidak mempunyai minuman sebanyak itu")
        elif(uang >= (totalchoice2 * minuman[choice2-1][1])):
            uang = uang - (totalchoice2 * minuman[choice2-1][1])
            print("Kamu telah membeli menu " + minuman[choice2-1][0] + " sebanyak " + str(totalchoice2) + " buah dan kamu memiliki sisa uang Rp." + str(uang))
            pesan_minuman = False
        else:
           tidak_ada_uang()



#print tambahan
for i in range (tambahanlen):
    print(str(i+1) + ". " + tambahan[i][0] + " (Rp." + str(tambahan[i][1]) + ")")

while (pesan_tambahan == True):
    choice3 = int(input("Pilih menu tambahan yang diinginkan: "))
    if(choice3 > len(tambahan)):
        print("Harap masukkan nomor orderan yang benar")
    else:
        totalchoice3 = int(input("Berapa banyak yang ingin kamu beli? "))
        if(totalchoice3 >= 50):
            print("Mohon maaf warteg kami tidak mempunyai minuman sebanyak itu")
        elif(uang >= (totalchoice3 * tambahan[choice3-1][1])):
            uang = uang - (totalchoice3 * tambahan[choice3-1][1])
            print("Kamu telah membeli menu " + tambahan[choice3-1][0] + " sebanyak " + str(totalchoice3) + " buah dan kamu memiliki sisa uang Rp." + str(uang))
            pesan_tambahan = False
        else:
           tidak_ada_uang()

#makan di temppat atau bawa pulang
for i in range (bungkuslen):
    print(str(i+1) + ". " + bungkus[i][0])


while (pesan_bungkus == True):
    choice4 = int(input("makan di tempat atau bungkus? : "))
    if(choice4 == 1):
        print("\nKamu telah memesan " + makanan[choice1-1][0] + " " + str(totalchoice1) + " porsi, " + minuman[choice2-1][0] + " " + str(totalchoice2) + " " +" " + tambahan[choice3-1][0] + ' '+ str(totalchoice3) +" " + "  buah dibungkus")
        print('mohon ditunggu ')
        pesan_bungkus = False
    else:
        print("\nKamu telah memesan " + makanan[choice1-1][0] + " " + str(totalchoice1) + " porsi, " + minuman[choice2-1][0] + " " + str(totalchoice2) + " " + tambahan[choice3-1][0] + ' '+ str(totalchoice3) +" " + "buah makan di tempat")
        pesan_bungkus = False

print ('selamat menikmati')
