tf = open("in2.txt", "r")
tf_values1 = tf.readline().split(",")
tf_values2 = []

of = open("out1.txt", "w")
of_cont = ""


for x in tf_values1:
    tf_values2.append(int(x.replace("\n", "")))

for y in tf_values2:
   f1 = open(f"table{y}.txt", "w") 
   for x in range(1, 11, 1):
       of_cont += f"{x}x{y}={x*y}\n"
   of_cont += "\n"
   f1.write(of_cont)
   f1.close()
   of_cont = ""
tf.close()

