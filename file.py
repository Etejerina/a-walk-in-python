num = 2500
string = "hola"
boolean = True

a_list = [1, 2, 3, 4]
a_set = set((1, 2, 3, 4, 5))
a_dict = {
    'name': 'Eze',
    'age': 47,
    'gender': 'male'
}

def check_params(num, string, boolean, a_list, a_set, a_dict):
    num += 1
    string += " mundo"
    boolean = False
    a_list.append(5)
    a_set.add(6)
    a_dict['age'] = 48


check_params(num, string, boolean, a_list, a_set, a_dict)

print(num)
print(string)
print(boolean)
print(a_list)
print(a_set)
print(a_dict)