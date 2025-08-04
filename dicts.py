x = {'key' : 3}
print(x)
print( 'key' in x)
print(x.values())
for key, value in x.items():
    print(key , value)
del x['key']
