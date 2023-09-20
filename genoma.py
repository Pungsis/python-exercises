secuencia = "ATGAGTGAAGAGGAGCAAGGCTCCGGCACTACCACGGGCTGCGGGCTGCCTAGTATAGAGCAAATGCTGGCCGCCAACCCAGGCAAGACCCCGATCAGCCTTCTGCAGGAGTATGGGACC"

current_word = ""
contador = 0

for i in secuencia:
    if contador % 3 == 0:
        current_word += " "
    if i == "T":
        current_word += "U"
    else:
        current_word += i
    contador += 1

print(current_word)
print(list(range(1, 10, 2)))
