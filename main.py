nom = 'alice'
age = 19

if age >= 18:
    print('majeure')
else:
    print('mineur')
#huh

def addition(a,b,c=0):
    """

    :param c:
    :param a:
    :param b:
    :return:
    """
    return a+b+c

resultat = addition(12,12)
print(resultat)

message = input("entrez une message : ")
print(message)

#t uples (???????)
def operation(a,b):
    return a+b, a-b, a*b, a/b
resultat = operation(12,12)
print(resultat)
#prints (24, 0, 144, 1.0) (this is a t-uple?