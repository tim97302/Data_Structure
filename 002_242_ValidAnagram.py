c={"a":0,"b":2}
b={"a":1,"b":2}
a=(1,2,3,4,5)
for i in a:
    print(i)
# c["c"]=c.get("c",0)+1

print(c.get("c",5))
c.setdefault("d",1)
print(c)
print(3//2)