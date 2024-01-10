def likes(list_names):
    if len(list_names) == 0:
        true =  'no one likes this post'
    elif len(list_names) == 1:
        true = list_names[0] + ' likes this'
    elif len(list_names) == 2:
        true = list_names[0] + ' and ' + list_names[1] + ' like this post'
    else:
        true = list_names[0] + ' and ' + list_names[1] + ' and ' + list_names[2] + ' like this post'
    return true


names = ['Niels', 'Yur', 'Sofie']
print(likes(names))

