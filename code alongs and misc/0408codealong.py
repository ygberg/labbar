def new_decorator(func):

    def warp_funk():
        print('code here, berfore execute func')

        func()
        print('print code here excute after func')

    return warp_funk

def func_needs_decorator():
    print('this functions is in need of decorator')


func_needs_decorator()

#reasign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

