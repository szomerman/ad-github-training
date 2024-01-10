def likes(list_names):
    if len(list_names) == 0:
        true =  'no one likes this post'
    elif len(list_names) == 1:
        true = list_names[0] + ' likes this'
    else:
        true = list_names[0] + ' and ' + list_names[1] + ' like this post'
    return true


names = ['Niels', 'Yur']
print(likes(names))

