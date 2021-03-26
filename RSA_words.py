def pgcd(a,b):
    if b==0:
        return a
    else: 
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
    Texte_Clair = input("Caractère(s) à chiffrer : ")
    
    Texte_Tab_Clair = list(Texte_Clair)
    ASCII_Tab_Clair = ""
    ASCII_Tab_Chiffre = ""
    Car_Tab_Chiffre = ""
    
    for Car_Clair in Texte_Tab_Clair:
    
        ASCII_Clair = ord(Car_Clair)
        ASCII_Tab_Clair = ASCII_Tab_Clair + " " + str(ASCII_Clair)
        # print("Entier en Clair : ", ASCII_Clair)

        # Chiffrement
        ASCII_Chiffre = pow(ASCII_Clair,e) % n
        ASCII_Tab_Chiffre = ASCII_Tab_Chiffre + " " + str(ASCII_Chiffre)
        #print("Entier chiffré : ", ASCII_Chiffre)

        Car_Chiffre = chr(ASCII_Chiffre)
        Car_Tab_Chiffre = Car_Tab_Chiffre + " " + Car_Chiffre
        #print("Caractère chiffré : ", Car_Chiffre)
        
    print("Entiers en Clair : ", ASCII_Tab_Clair)
    print("Entiers chiffrés : ", ASCII_Tab_Chiffre)
    print("Texte chiffré : ", Car_Tab_Chiffre)

else:
    # Déchiffrement
    
    #input code à déchiffrer
    ASCII_Multiple_Chiffre = input("Code(s) à déchiffrer : ")

    ASCII_Tab_Dechiffre = ""
    Car_Tab_Dechiffre = ""
    
    ASCII_Tab_Chiffre = ASCII_Multiple_Chiffre.split(" ")
    
    for ASCII_Chiffre in ASCII_Tab_Chiffre:
 
        ASCII_Dechiffre = pow(int(ASCII_Chiffre),d) % n
        ASCII_Tab_Dechiffre = ASCII_Tab_Dechiffre + " " + str(ASCII_Dechiffre)
        #print("Entier déchiffré : ", ASCII_Dechiffre)

        Car_Dechiffre = chr(ASCII_Dechiffre)
        Car_Tab_Dechiffre = Car_Tab_Dechiffre + " " + str(Car_Dechiffre)
        #print("Caractère Déchiffré : ", Car_Dechiffre)
        
    print("Entiers déchiffrés : ", ASCII_Tab_Dechiffre)
    print("Caractères Déchiffrés : ", Car_Tab_Dechiffre)
