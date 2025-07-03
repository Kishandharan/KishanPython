tf = open("in2.txt", "r")
tf_values1 = tf.readline().split(",")
tf_values2 = []

for x in tf_values1:
    tf_values2.append(int(x.replace("\n", "")))

for y in tf_values2:
   for x in range(1, 11, 1):
       print(f"{x}x{y}={x*y}")
   print()

