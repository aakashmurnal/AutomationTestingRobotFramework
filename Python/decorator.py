# Change the behaviour of the existing function at the compile time itself without altering exist structure
### Example

def div(a,b):
    print(a/b)

def dec_div(function):
    def change_behaviour(a,b):
        if a<b:
            a,b=b,a
        return function(a,b)
    return change_behaviour

div = dec_div(div)
div(2,4)

