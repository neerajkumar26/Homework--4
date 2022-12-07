
# Name: - Neeraj Kumar
# ID: - 2047559
_input = '[]'
data=[]

_input  = input()

while _input!="-1":
    data.append(_input)
    _input  = input()
        

for record in data:
    val = record.split(" ")
    try:
        val[1] = int(val[1])
        print(f"{val[0]} {(val[1] + 1)}")
    except ValueError as ve:
        print(f"{val[0]} 0")
