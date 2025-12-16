s  = "kodnest"
print(s[0])
print(s[1])
print(s[-2])
print(s[0:3])
print(len(s))
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.find("kod"))
print(s.replace("k","c"))

t = "apple,banana,orange"
f = t.split(",")
print(f)

joined_text= "-".join(f)
print(joined_text)
print(id(s))