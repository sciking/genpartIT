import random
def genpart():
 a = ["Alleanza", "Scelta", "Alternativa", "Avanti", "Lega", "Federazione"]
 b = ["Nord", "Nazionale", "Civica", "Popolare", "Padana", "della Famiglia", "Cristiana"]
 c = ["Monti", "Berlusconi", "Alfano", "Berlusconi", "Bossi","Renzi","Vendola","Casini","Maroni"]
 d = ["l'Italia", "l'indipendenza della Padania", "la famiglia tradizionale", "l'Italia fedrale", "l'Europa unita"]
 l = random.randint(1,4)
 g = len(a)-1
 k = len(b)-1
 j = len(c)-1
 h = len(d)-1
 za = a[random.randint(0,g)]
 zb = b[random.randint(0,k)]
 zc = c[random.randint(0,j)]
 zd = d[random.randint(0,h)]
 if l == 1:
  print za, zb
 elif l == 2:
  print za, zb, "per",zd
 elif l == 3:
  print za, zb, "con",zc
 elif l == 4:
  print za, zb, "con",zc, "per",zd
genpart()
