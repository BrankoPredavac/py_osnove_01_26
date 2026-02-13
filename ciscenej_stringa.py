primjer = "       Ante    \n   "

print(primjer, end="|")
print()
# "Ante" nakon strip
print(primjer.strip(), end="|")
print()
# lstrip  "Ante    \n   "
print(primjer.lstrip(), end="|")

# lstrip  "       Ante"
print(primjer.rstrip(), end="|")
