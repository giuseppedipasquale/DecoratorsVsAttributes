import time

""" CLASS TestA goes through decorators for ballistic
    is a reduced copy of Spacecraft class from poliastro
"""
class TestA:
    def __init__(self,A,m,C_D):
        self._A = A
        self._m = m
        self._C_D = C_D
    @property
    def A(self):
        return self._A
    @property
    def m(self):
        return self._m
    
    
    @property
    def ballistic(self):
        B = self._C_D*(self.A / self.m)
        return B

""" CLASS TestB uses attributes directly for ballistic"""
class TestB:
    def __init__(self,A,m,C_D):
        self._A = A
        self._m = m
        self._C_D = C_D

    @property
    def ballistic(self):
        B = self._C_D*(self._A/self._m)
        return B


n_iter = 10000

direct_wins = 0
total_runs = 1000

""" 
    Runs for total_runs and calculates delta-t [seconds] as end-start (calculated using time.time())
    In each run the ballistic function of the classes is called n_iter times.
    The order is inverted every iteration, so call TestA first, then TestB and so on.
"""
for j in range(0,total_runs):
    
    if (j%2)==0:
        print("______ TEST =",j)
        start = time.time()
        for i in range(0,n_iter):
            a = TestA(i,20,2.2).ballistic
        end = time.time()
        ta = end - start
        print("THROUGH DECORATORS:",ta,"seconds")

        start = time.time()
        for i in range(0,n_iter):
            a = TestB(i,20,2.2).ballistic
        end = time.time()
        tb = end - start
        print("DIRECT:            ", tb,"seconds")
        if (ta-tb)>0:
            print("-----> Direct is faster")
            direct_wins+=1
    else:
        print("______ TEST =",j)
        start = time.time()
        for i in range(0,n_iter):
            a = TestB(i,20,2.2).ballistic
        end = time.time()
        tb = end - start
        print("DIRECT:            ", tb,"seconds")
        
        start = time.time()
        for i in range(0,n_iter):
            a = TestA(i,20,2.2).ballistic
        end = time.time()
        ta = end - start
        print("THROUGH DECORATORS:",ta,"seconds")
        
        if (ta-tb)>0:
            print("-----> Direct is faster")
            direct_wins+=1
            
print("Direct is faster:",direct_wins/(total_runs)*100,"% of times")
