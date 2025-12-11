import math
import sys

# Constantes de couleur pour l'affichage (optionnel, mais améliore la lisibilité)
VERT = "\033[92m"
JAUNE = "\033[93m"
CYAN = "\033[96m"
ROUGE = "\033[91m"
RESET = "\033[0m"

def rsa_crack():
    """
    Factorise le module RSA N et calcule les composants de la clé privée
    en utilisant la logique de recherche par force brute du code Java fourni.
    """

    # Module N en hexadécimal (à partir du Challenge )
    # n_hex est la représentation hexadécimale du modulus
    n_hex = "8da56919b526d45225aced4be64522cef04a63910b9f6ffea6b1125541013be45d48b6fb2671b7540e6a4e0b55e3a9e4c45a8d5f54a0699c6532d4a1287facb008b1c56e35d601dc2a9e2e665189eaa35d22d7bea252c1ecf27031ab657d5b35e82cde70f8259d2e14e986f362e3e86e7bd8e4812a52f2e8cc2f69b8b0c959778fdb240a8e17cb9572457012d83b6c727290e50b8e7da28febdfabf523da03b94b94322af421f9ca02ade604daab92cd9c28244436f115fdbed76d2c85007aca7fce49893af80e7955632ec7b89f56fab01876e0fe88299a37340d439cb2e01b3c07e60c8847421bfe049d5995406b26f4a08b20d149b3c61aaea3531d62f8f8d1e287"
    
    # Conversion de l'hexadécimal en grand entier BigInteger (nativement géré par Python)
    n = int(n_hex, 16)
    
    # Exposant public e (fixé par défaut [cite: 56])
    e = 65537
    
    # Démarrage de la recherche à 3 (comme dans le code Java, car N est impair)
    q = 3
    
    print(f"{CYAN}--- Démarrage de la factorisation (Recherche de q) ---{RESET}")
    print(f"{JAUNE}Module N (décimal) : {n}{RESET}")
    
    # Boucle pour trouver le petit facteur q.
    # On itère de 2 en 2 (q = q + 2) car N est le produit de deux nombres premiers impairs, 
    # donc N est impair, et son facteur q ne peut pas être pair.
    while n % q != 0:
        q += 2
        
    print(f"{VERT}✓ Petit facteur q trouvé : {q}{RESET}")
    
    # Calcul de p
    p = n // q
    
    # --- Calcul des composantes de la clé privée RSA ---
    
    p_minus_1 = p - 1
    q_minus_1 = q - 1
    
    # Indicatrice d'Euler (phi)
    phi = p_minus_1 * q_minus_1
    
    # Exposant privé d = e^-1 mod phi.
    # La fonction pow(base, exp, mod) de Python gère la modInverse avec exp=-1.
    # Ceci est l'équivalent de e.modInverse(phi) en Java.
    d = pow(e, -1, phi)
    
    # Composantes CRT (Chinese Remainder Theorem)
    # e1 = d mod (p-1) [cite: 50]
    e1 = d % p_minus_1
    
    # e2 = d mod (q-1) [cite: 51]
    e2 = d % q_minus_1
    
    # coef = (inverse of q) mod p [cite: 53]
    coef = pow(q, -1, p)
    
    # --- Affichage des résultats ---
    
    print(f"\n{CYAN}--- Composants de la clé privée RSA (pour Private.txt) ---{RESET}")
    print(f"{JAUNE}modulus (N) ={RESET} {VERT}{n}{RESET}")
    print(f"{JAUNE}pubExp (e) ={RESET} {VERT}{e}{RESET}")
    print(f"{JAUNE}privExp (d) ={RESET} {VERT}{d}{RESET}")
    print(f"{JAUNE}p ={RESET} {VERT}{p}{RESET}")
    print(f"{JAUNE}q ={RESET} {VERT}{q}{RESET}")
    print(f"{JAUNE}e1 (d mod p-1) ={RESET} {VERT}{e1}{RESET}")
    print(f"{JAUNE}e2 (d mod q-1) ={RESET} {VERT}{e2}{RESET}")
    print(f"{JAUNE}coeff (q^-1 mod p) ={RESET} {VERT}{coef}{RESET}")
    print(f"{CYAN}--------------------------------------------------------{RESET}")

if __name__ == "__main__":
    rsa_crack()