def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

texto = "Luquinha"
print("Original:", texto)
print("Invertida:", inverter_string(texto))
