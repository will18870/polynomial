# William Huang
# evaluate() acts kind of like a pseudo-recursive method, where each evaluate() call
# calls the evaluate() method of the class that makes up the variables of the current class
# until it inevitably reaches X or Int, in which it returns the raw value of those classes.

class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x):
        return x

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            return repr(self.p1) + " - ( " + repr(self.p2) + " )"
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            if isinstance(self.p2, (Add, Sub, Mul, Div)):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            if isinstance(self.p2, (Add, Sub, Mul, Div)):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) / self.p2.evaluate(x)

poly = Sub( Add( Int(4), Int(3)), Add( X(), Mul( Int(3), Add( Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(2))