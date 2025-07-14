#VARIABLE 
#EXAMPLE OF DECLARATION 
#integer

a=50
b=10
c=a/b 
d=5555564

print (c)

#string

x="john doe"
y="doe  is the younger in the family"

print(x[0])

#list

squares=[1, 9 , 4]
print(squares)
fruts=['pawpaw', 'plum', 'orange']

#operation on list 
#to add
fruts.append('kiwi')

print(fruts)

#del(): enlever a parti de lindex
#remove(): enlever un element d'une liste
# len() : obtenir la taille de la liste
# insert(index, élément) : insérer un élément à un index donné
# pop() : retirer et retourner le dernier élément (ou un élément à un index donné)

m, n= 0, 1
while m<10 :
    print(m)
    m, n = n, m+n


#Boucles
# if ..elif .. else

if a<b:
    print(str(a)+'est plus petit que'+str(b))
elif a==b :
    print(f"{a} est egal a {b}")
else :
    print('ras')

# for in

for p in fruts:
    print(p, len(p))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
    else :
        print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# range
for i in range(5):
     print(i)

#break



