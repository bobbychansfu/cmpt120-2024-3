NUM_COL = 4
more = True

scores = []

while (more):
    name = input("name: ")
    mt1 = float(input("input mt1: "))
    mt2 = float(input("input mt2: "))
    fin = float(input("input fin: "))
    student = [name,mt1,mt2,fin]
    scores.append(student)
    cont = input("more? ")
    if cont.lower() != "y":
        more = False

print(scores)
