tf = open("in2.txt", "r")
tf_lines = []

for x in tf:
    tf_lines.append(int(x.replace("\n", "")))

for y in tf_lines:
    for x in range(1, 11, 1):
        print(f"{x}x{y}={x*y}")
    print()
    
