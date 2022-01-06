from string import maketrans

context = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

def rot13(text):
   return text.translate(context)
def main():
   txt = input("Metin Giriniz : ")
   print("Sifrelenmis Metin : "+rot13(txt)) 
   print("Sifrelenmis Metin : " +rot13(rot13(txt))) 
  
if __name__ == "__main__":
   while True: 
        main()