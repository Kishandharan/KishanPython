words = ["hola", "tengo", "quiero", "por", "favor", "lo", "siento", "de", "nada", "mi", "hotel"] # Few spanish words
buffer = ""
str1 = "Holaporfavormihotel"
sentence = ""

for i in str1:
    buffer += i.lower()
    if buffer in words:
        sentence += buffer+" "
        buffer = ""

print(sentence)

# Spanish word seperator
