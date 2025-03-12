import sys

input_list = sys.argv[2:]

res = float(sys.argv[1])

for i in range(len(input_list)):
    try:
        float(input_list[i])
        continue
    except:
        if input_list[i] == '+':
            res += float(input_list[i+1])
        elif input_list[i] == '-':
            res -= float(input_list[i+1])
        elif input_list[i] == '/':
            res = res/float(input_list[i+1])
        elif input_list[i] == '*':
            res = res*float(input_list[i+1])

print(res)
