s = set()
print(type(s))
l = [1, 2, 3, 4]
s_list = set(l)
print(s_list)
print(type(s_list))
s.add(1)
# s.add(1)  # It can't add two 1 in one set. Set can only add different variables.
s.add(2)
s.remove(2)
s1 = {4, 6}
print(s)
print(s1)
print(s.isdisjoint(s1))

