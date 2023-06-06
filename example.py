class Test:
    x=10
    def __init__(self):
        self.y=20
        self.z=30
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y,t1.z)
print('t2:',t2.x,t2.y,t2.z)
t1.x=888
del Test.x
t1.y=999
print('t1:',t1.x,t1.y,t1.z)
print('t2:',t2.x,t2.y)

