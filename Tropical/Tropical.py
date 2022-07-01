class Tropical:
    """
    Class that acts as an interface for converting conventional arithmetic to it's tropical counterpart.

    Object takes int as a value as labels it as Tropcial

    addition is min operation, e.g. a+b = min(a,b)

    multiplication is usual addition: a*b = a+b
    """

    def __init__(self,val):
        """
        init function.
        :param val: numerical value
        """
        self.val = val

    def __add__(self, other):
        """
        Operational overload on addition converting it to mean "min" in Tropical context

        :param other: Another tropical object like self
        :return: Tropical "sum"
        """
        return Tropical(min(self.val, other.val))

    def __mul__(self, other):
        """
        Overload * to mean conventional +

        :param other: Another tropical object
        :return: Tropical "product"
        """
        return Tropical(self.val + other.val)

    def __iadd__(self, other):
        """
        Operational overload for "+=" using correlating method for __add__
        :param other: Tropical Object
        :return: Updated sum (Tropical)
        """
        self = self+other
        return self

    def __imul__(self, other):
        """
        Operational overload for "*=" correlating to method for __mul__
        :param other: Tropical Object
        :return: Updated product (Tropical type)
        """
        self = self * other
        return self

    def __ge__(self, other):
        """
        Greater than equal to, same as normal numbers.
        :param other: Tropical object
        :return: a >= b ?
        """
        return self.val >= other.val

    def __le__(self, other):
        """
        Less than or equal to, same as normal numbers
        :param other: Tropical Object
        :return: a <= b ?
        """
        return self.val <= other.val

    def __gt__(self, other):
        """
        greater than
        :param other: Tropical Object
        :return: a > b
        """
        return self.val > other.val

    def __lt__(self, other):
        """
        Less than
        :param other: Tropical Object
        :return: a > b
        """
        return self.val < other.val

    def __eq__(self, other):
        """
        Equal to
        :param other: Tropical Object
        :return: a == b
        """
        return self.val == other.val

    def __ne__(self, other):
        """
        not equal to
        :param other: Tropical object
        :return: a != b
        """
        return self.val != other.val

    def __str__(self):
        """
        Convert to string
        :return: string converted numerical value
        """
        return str(self.val)

    def __repr__(self):
        """
        For print calls and debugging
        :return: see return statement
        """
        return f"Tropical : {self.val}"

    def __float__(self):
        """
        float conversion
        :return: float converted value
        """
        return float(self.val)

    def __int__(self):
        """
        int conversion
        :return: int converted value
        """
        return int(self.val)

if __name__ == '__main__':
    # Testing.
    lst = [Tropical(i) for i in [1,2,3,4,5.0]]
    print(list(lst))
    print(sum(lst,start=lst[0]))
    a, b, c = tuple(lst[:3])
    print(f"a+b = {a+b}\nb+c = {b+c}\na+c = {a+c}\na+b+c = {a+b+c}")
    print(f"\na*b = {a * b}\nb*c = {b * c}\na*c = {a * c}\na*b*c = {a * b * c}")
    a+=b
    b+=c
    print(f"\na+=b : {a}\nb+=c : {b}")
