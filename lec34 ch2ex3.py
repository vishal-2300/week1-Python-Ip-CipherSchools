name=input("enter your name")
chra=input("enter chr").strip()
print(len(name))
#print(name.count(chra.upper() or chra.lower())) mistake
print(f"count {name.lower().count(chra.lower())}")