a = input()
s = a.split(";")
for i in range(len(s)):
    if s[i].isdigit():
        if int(s[i]) % 2 == 0:
            print(f'{s[i]},', end="")
for i in range(len(s)):      
        if s[i].isdigit() == True:
            if int(s[i]) % 3 == 0:
                print(f'{s[i]},', end="")
for i in range(len(s)):       
        if not s[i].isdigit():
            if len(s[i]) > 4:
                print(f'{s[i]},', end="")           