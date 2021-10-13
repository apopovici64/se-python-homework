"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""
x = input("Introduceti sirul de caractere:")
x_lowercase = x.lower()
total_vowel_count = 0
for vowel in 'aeiou':
    count = x_lowercase.count(vowel)
    total_vowel_count += count
print(total_vowel_count)


