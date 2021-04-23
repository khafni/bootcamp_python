def ft_filter(function_to_apply, list_of_inputs):
    for e in list_of_inputs:
        b = function_to_apply(e)
        if not isinstance(b, (int, float)):
            yield e
            continue
        if not b:
            continue
        yield e

l = [1, -3, 2, 4, -1]

for e in ft_filter(lambda x : True if x > 0 else False, l):
    print(e)


print("------------------")

def f(e):
    return

for e in ft_filter(f, l):
    print(e)