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

uang = input('Masukan jumlah uang anda : ')
makanan = ["Rendang",16000], ["Ayam Bakar",15000], ["Ayam Goreng", 15000], ["Nasi Goreng", 13000]
minuman = ["Teh Manis", 6000], ["Air Mineral", 3000], ["Teh Tawar", 5000], ["Jus Jeruk", 9000]
pesan_makanan = True
pesan_minuman = True

makananlen = len(makanan)
minumanlen = len(minuman)

#Print List Makanan
for i in range (makananlen):
    print(str(i+1) + ". " + makanan[i-1][0] + " (Rp." + str(makanan[i-1][1]) + ")")

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
    print(str(i+1) + ". " + minuman[i-1][0] + " (Rp." + str(minuman[i-1][1]) + ")")

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

print("\nKamu telah memesan " + makanan[choice1-1][0] + " " + str(totalchoice1) + " porsi dan " + minuman[choice2-1][0] + " " + str(totalchoice2) + " buah")
print("Selamat menikmati!")
