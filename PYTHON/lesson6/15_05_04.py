d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

a = int(input("enter phone number\n"))
if a in d:
    print({d[a][0][0]}," ",{d[a][0][1]}," from ",{d[a][1][0]},", ",{d[a][1][1]})
else: 
    print("not faund")