file = open("cog.txt", "r")
lines = file.readlines()
file.close()
st = ''
for line in lines:
    st+='"'
    for x in line:
        if x!='\n':
            st+=x
    st+='"'
    st+=','
print(st)

file2 = open("list.txt", "w")
file2.write(st)
file2.close()
