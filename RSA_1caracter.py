def pgcd(a,b):
    if b==0:
        # la précédente itération a renvoyé un reste de a%b = 0 ; donc on retourne le précédent b, qui est le pgcd
        return a

    else: 
        # la précédente itération a renvoyé un reste != 0, donc on réitère sur b et le reste de a%b 
        return pgcd(b, a % b)

Choix_Generation_Cle = input("[1] Générer une paire de clé\n[2] Définir les clés\n")
if(Choix_Generation_Cle == "1"):
    # Nombres premiers
    p = int(input("p: "))
    q = int(input("q: "))

    n = p*q
    print ("n = ", n)

    phi = (p-1)*(q-1) 
    print ("phi = ", phi)


    # Calcul de e , 1 < e < phi , et e premier avec Phi
    for e in range(2,phi): 
        if pgcd(e,phi)== 1:
            break

    print("e = ",e)

    #calcul de d
    for d in range(2,phi):
        if((e*d) % phi != 1 ):
            d += 1
        else:
            break
    
    print("d = ",d)
 
else:
    n = int(input("n: "))
    e = int(input("e: "))
    d = int(input("d: "))


print("Clé publique : {",n,",",e,"}")
print("Clé privée : {",n,",",d,"}")


Choix_Chiffrement_Dechiffrement = input("[1] Chiffrer avec clé publique\n[2] Déchiffrer avec clé privée\n")

if(Choix_Chiffrement_Dechiffrement == "1"):
    # Chiffrement

    #input caractères à chiffrer
    Car_Clair = input("Caractère à chiffrer : ")
    ASCII_Clair = ord(Car_Clair)
    print("Entier en Clair : ", ASCII_Clair)

    # Chiffrement
    ASCII_Chiffre = pow(ASCII_Clair,e) % n
    print("Entier chiffré : ", ASCII_Chiffre)

    Car_Chiffre = chr(ASCII_Chiffre)
    print("Caractère chiffré : ", Car_Chiffre)

else:
    # Déchiffrement
    
    #input code à déchiffrer
    ASCII_Chiffre = int(input("Code à déchiffrer : "))
 
    # Chiffrement
    ASCII_Dechiffre = pow(ASCII_Chiffre,d) % n
    print("Entier déchiffré : ", ASCII_Dechiffre)

    Car_Dechiffre = chr(ASCII_Dechiffre)
    print("Caractère Déchiffré : ", Car_Dechiffre)
