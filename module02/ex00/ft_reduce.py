import functools

def ft_reduce(function_to_apply, list_of_inputs):
    it = iter(list_of_inputs)
    accum_value = next(it)
    for e in it:
        accum_value = function_to_apply(accum_value, e)
    return accum_value
        



lis = [1, 8, 6]
l = iter(lis)
#print(next(l))
#print(next(l))
print(functools.reduce(lambda a,b : a + b, lis))
print(ft_reduce(lambda a,b : a + b, lis))