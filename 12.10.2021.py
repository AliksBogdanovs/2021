"""
Uzraksti funkciju, kura atgriež mazāko skaitli, ja abi skaitļi ir pāra skaitļi
Atgriež lielāko skaitli, ja abi skaitļi ir nepāra vsi viens no skaitļiem ir nepāra skaitlis

atgriez_skaitli(2,4) ----- > 2
print(atgriez_skaitli(2,5)) ----- > 5
"""

'''
4%2=0
min()
max()

return
'''


print(min(1,4,6,8))
print(max(1,4,9,7))
def atgriez_skaitli(a,b):

    #Pirmā parbaude - vai a un b ir pāra skaitļi

    if a%2 == 0 and b%2 == 0:
    
        return min(a,b)

    else:
        return max(a,b)

print(atgriez_skaitli(2,4))
print(atgriez_skaitli(5,6))
