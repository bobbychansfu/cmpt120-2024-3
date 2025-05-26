a = 5
b = 10

print("5 == 10: ", a == b)
print("5 != 10: ", a != b)
print("5 > 10: ", a > b)
print("5 < 10: ", a < b)
print()

c = "hello"
d = "HELLO"
e = "HELLO"
f = "HELLo"

print("HELLO == HELLO: ", e==d)
print("HELLO <= HELLO: ", e<=d)
print("hello == HELLO: ", c==d)
print("hello < HELLO: ", c<d)
print("HELLo == HELLO: ", f==d)
print("HELLo < HELLO: ", f<d)
print()

s = "ell"

print("ell in hello: ", s in c)
print("ell in HELLO: ", s in d)
print("ell not in HELLO: ", s not in d)

print(isinstance("hello", int))
