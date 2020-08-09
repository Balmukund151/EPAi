import random
import decimal
import math

class Qualean:
    def __init__(self,real_val):
        decimal.getcontext().prec=10
        self.computed_val = decimal.Decimal(real_val * random.uniform(-1, 1))/decimal.Decimal(1)

    def  __and__(self, value):
        return bool(float(self.computed_val)) & bool(float(value))

    def __or__(self, value):
        return bool(float(self.computed_val)) | bool(float(value))

    def __repr__(self):
        return 'Qualean({0})'.format(self.computed_val)

    def __str__(self):
        return 'Qualean({0})'.format(self.computed_val)

    def __add__(self,value):
        return self.computed_val + value.computed_val

    def __eq__(self,value):
        return self.computed_val == value.computed_val

    def __float__(self):
        return float(self.computed_val)

    def __ge__(self,value):
        return self.computed_val >= value.computed_val

    def __gt__(self,value):
        return self.computed_val > value.computed_val

    def __invertsign__(self):
        return self.computed_val * -1

    def __le__(self,value):
        return self.computed_val <= value.computed_val

    def __lt__(self,value):
        return self.computed_val < value.computed_val

    def __mul__(self,value):
        return self.computed_val * value.computed_val

    def __sqrt__(self):
        if self.computed_val<0:
            return decimal.Decimal.sqrt(decimal.Decimal(-1)* self.computed_val)
        else:
            return decimal.Decimal.sqrt(self.computed_val)

    def __bool__(self):
        return self.computed_val!=0

    def __round__(self):
        return round(self.computed_val,10)

    def check_for_100_sums(self):
        decimal.getcontext().prec=15
        added_val=decimal.Decimal(0)
        for i in range(100):
            added_val+= self.computed_val
        decimal.getcontext().prec=10
        return added_val == self.computed_val * 100

    def sum_1_milliontimes(self,count):
        sum = decimal.Decimal(0)
        for i in range(count):
            sum += decimal.Decimal(round(random.choice([-1,0,1]) * random.uniform(-1, 1),10))
        return math.isclose(round(float(sum)),0)