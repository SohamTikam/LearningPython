def func (x,y,z=None):
    print('run',x ,y,z)
    return x+y*z, x-y+z
r1, r2 = func(5,6,7)
print(r1, r2)
