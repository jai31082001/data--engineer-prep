# Generate a list of squares of numbers 1–10.
a=[x*x for x in range(1,12)]
print(a)

b=[x for x in range(1,21) if x%2==0]
print(b)
list_even_nums = [x for x in range(1,21) if x%2==0]
string="aapple"
vowels = [x for x in string if x.lower() in ['a', 'e', 'i', 'o', 'u']]
print(vowels)
