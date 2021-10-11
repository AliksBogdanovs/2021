#.specifikācija

'''
Uzrakstīt funkciju:
*ievadīt linolēja cenu
*ievadīt telpas izmēru
*izvadīt cenu
'''

def lin_cena(cenu, izmers):
    kopa = cenu * izmers

    return kopa

print(lin_cena(5, 20))

# 2.specifikācija

'''
Uzrakstīt funkciju grīdas izmaksas(cena, telpas_garums, telpas_platumu)

*Cena EUR/m2
*Telpas platums un garums
*aprēķināt izmaksas, noapaļojot telpas garumu un platumu uz augšu
*izvadīt izmaksas
'''

def gridas_izmaksa(cena,telpas_garums,telpas_platumu):

    return telpas_garums * telpas_platumu * cena

    if telpas_platumu%linolēja_platums != 0:
        trukst = telpas_platums%linoleja_platums
        if trukst<linoleja_platums:
            papildus = round(linoleja_platums * telpas_garums)
            izmaksas = (round(telpas_garums*telpas_platumu) + papildus)*cena
        elif trukst > linoleja_platums:
            lin_gab = round(trukst/linoleja_platums)
            papildus = lin_gab * linoleja_platums * telpas_garums
            izmaksas = (round(telpas_platumu*telpas_garumu) + papildus)*cena
    else:
        izmaksas = round(telpas_platumu*telpas_garums)*cena

    return izmaksas
    