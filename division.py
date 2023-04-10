num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

bin_num1 = bin(num1)[2:]
bin_num2 = bin(num2)[2:]

if len(bin_num1) > len(bin_num2):
    bin_num2 = bin_num2.zfill(len(bin_num1))
else:
    bin_num1 = bin_num1.zfill(len(bin_num2))

cociente = ""
residuo = ""
temp = ""

for i in range(len(bin_num1)):
    temp += bin_num1[i]
    if int(temp, 2) < int(bin_num2, 2):
        cociente += "0"
    else:
        cociente += "1"
        temp = bin(int(temp, 2) - int(bin_num2, 2))[2:]
    residuo = temp

print("El cociente en bits es:", cociente)
print("El residuo en bits es:", residuo)