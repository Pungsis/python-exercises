import random

count1 = 0
count2 = 0

vocales = "aeiou"
current_word = ""
frase = "un lunes lluvioso"
frase_transformada = ""
for i in frase:
    count1 += 1
    count2 += 1
    current_word += i
    if i == " " or count1 == len(frase):
        new_vocales = ""
        new_consonantes = ""
        count2_ref = count2
        count1_ref = count1
        while count1_ref > (count1 - count2):
            if current_word[count1_ref - 1] in vocales:
                new_vocales += current_word[count1_ref - 1]
            else:
                new_consonantes += current_word[count1_ref - 1]
            count1_ref -= 1

        frase_transformada += new_consonantes + \
            new_vocales + str(random.randint(1, 100)) + " "
        count2 = 0

super_frase = ""
for j in frase_transformada:
    if j in vocales:
        super_frase += j.upper()
    else:
        super_frase += j.lower()

print(super_frase)
