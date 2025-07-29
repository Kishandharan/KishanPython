f1 = open("sampledata1.txt", "r") # A file which contains items with prices and quantities
totalprice = 0
f1.readline() # Ignoring the first row as it contains column heading

for _ in range(0, 13, 1):
    line = f1.readline()
    item = line.split(",")[0].strip()
    rate = int(line.split(",")[1].strip())
    qunt = int(line.split(",")[2].strip())
    price = rate*qunt 
    totalprice+=price
    print(f"The price of {item} x {qunt} is {price}")

print(f"\nThe total price is {totalprice}")
