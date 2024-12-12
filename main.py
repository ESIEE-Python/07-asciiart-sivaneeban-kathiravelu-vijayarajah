""" exercice code ascii """
import sys
sys.setrecursionlimit(5000)

def artcode_i(s):
    """retourne la liste de tuples 

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)"""

    if not s:
        return []

    chars = [s[0]]
    occurrences = [1]
    k = 1

    while k < len(s):
        if s[k] == s[k - 1]:
            occurrences[-1] += 1
        else:
            chars.append(s[k])
            occurrences.append(1)
        k += 1

    return list(zip(chars, occurrences))


def artcode_r(s):
    """Retourne la liste de tuples .

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: La liste des tuples (caractère, nombre d'occurrences).
    """

    if not s:
        return []

    firstchar = s[0]
    count = 1

    while count < len(s) and s[count] == firstchar:
        count += 1

    resultat = [(firstchar, count)]

    rest_of_string = s[count:]

    return resultat + artcode_r(rest_of_string)


    # recherche nombre de caractères identiques au premier
    # appel récursif



#### Fonction principale


def main():
    """ fonction main """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
