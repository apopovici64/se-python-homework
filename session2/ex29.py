"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
x = input("Introduceti sirul de caractere:")
x_lowercase = x.lower()
total_vowel_count = 0
total_consonant_count = 0
for vowel in 'aeiou': #consideram vocalele din limba engleza
    count_v = x_lowercase.count(vowel)
    total_vowel_count += count_v
ctotal_consonant_count = len(x) - total_vowel_count

print(total_vowel_count)
print(total_consonant_count)