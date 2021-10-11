def pasuti_tkreklus(skaits,apdruka,piegadi):


    #Definē cenas
  Cena = {'TEKSTS' :5, 'ZIME' :7, 'FOTO' :20}
    #Aprēķina apdrukas izmaksas
  apdrukas_vert = cena[apdruka] * skaits
    #Definē nosacījumus piegādei un atlaidēm

  if apdrukas_vert < 50:
      return apdrukas_vert + 15
  elif apdrukas_vert >= 50:
      return apdrukas_vert
  elif apdrukas_vert > 100:
      return apdrukas_vert * 0.05

else:
    #Ja piegade = False
    if apdrukas_vert > 100
    return apdrukas_vert * 0.05
else:
    return apdrukas_vert
pasuti_tkreklus(5,'TEKSTS', True)

