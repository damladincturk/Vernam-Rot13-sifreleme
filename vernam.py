def sifrele( text, key ):
    """ Returns the Vernam Cypher for given string and key """
    cevap = "" # the Cypher text
    p = 0 # pointer for the key
    for char in text:
        cevap += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p==len(key):
            p = 0
    return cevap

                      
MY_KEY = "cvwopslweinedvq9fnasdlkfn2"
while True:
    print("\n\n---Vernam Cypher---")
    PlainText = input("Dönüstürülecek metni giriniz : ")
    # Encrypt
    Cypher = sifrele(PlainText, MY_KEY)
    print("Sifrelenmis metin: "+Cypher)
    # Decrypt
    decrypt = sifrele(Cypher, MY_KEY)
    print("Cozümlenmis metin: "+decrypt)