# membuat kalkulator sederhana

def pengurangan(a,x):
  return a - x

def penambahan(a,x):
  return a + x

def perkalian(a,x):
  return a * x

def pembagian(a,x):
  return a / x

try:
  cal = int(input("ini adalah operasi kalkulator sederhana tekan 1 untuk melanjutkan "))


  while cal == 1:
    try:
      y = int(input("memilih operasi yang digunakan \n1. pengurangan \n2. penambahan \n3. perkalian \n4. pembagian \n5. keluar dari program\nmasukan angka "))
      if y > 5:
        print("tidak ada dalam operasi")
        continue
      if y == 5:
        break
      a = int(input("masukan angka pertama "))
      b = int(input("masukan angka kedua "))



      if y == 1:
        print(f"hasil pengurangan {a} - {b} = {pengurangan(a,b)}")
      elif y == 2:
        print(f"hasil penambahan {a} + {b} = {penambahan(a,b)}")
      elif y == 3:
        print(f"hasil perkalian {a} X {b} = {perkalian(a,b)}")
      elif y == 4:
        print(f"hasil pembagian {a} / {b} = {pembagian(a,b)}")
    except Exception:
      print("masukan anda salah")

    print("ingin melanjutkan tekan 1")
    lanjut = int(input())
    if lanjut != 1:
      break

except Exception:
  print("masukan anda salah")

print("\npemorgraman selesai terima kasih")