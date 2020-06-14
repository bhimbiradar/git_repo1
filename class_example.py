# class has:
#     1.class attribute
#     2.instance attribute: the attribute which are defined in constructor is instance attribute
#     e.g. self.l=mylist
#     3.private attribute
#     4.constructor: constructor is a method which initilise the object
#          constructor declaration
#          def__init__(self,mylist,f,l)
#              self.a=20
#              self.l=mylist
#      5.instances method: any method whose first parameter is self then it is called instance method.
#      6.class method: to use the class attributes (all class methods starts with @ classmethod decorator)
#      7.static method
#      8. properties -->getter:- get data from object
#      9. properties --> setter:- spilts data


class MyClass1:
    a = 10
    _b = 20
    firstname = None
    lastname = None

    # constructor
    def __init__(self, ml, f, L):
        super(MyClass1, self)
        # raise attributeError()
        print("MyClass1 object created:")
        print("a===", self.a)
        self.a = 20
        self.l = ml
        self.firstN = f
        self.lastN = L
        print("a===", self.a)
        self.l.append(10)
        print(self.l)

    # instance method
    def function1(self):
        print("self==", self)
        result = sum(self.l)
        return result;

    # private method
    def __myprivate(self):
        # any method that starts with double __ are called as private methods
        print("Calling private method")

    # classmethod
    @classmethod
    def myclassmethod(cls):
        print("this is classmethod a==",cls.a)

   #staticmethod
    @staticmethod
    def mystaticmethod():
        print("this is staticmethod")

    # factorial by instance method
    def instance_method(self):
        for item in self.l:
            print("factorial of %d==%d"%(item,MyClass1.myfactorial(item)))

    # staticmethod factorial
    @staticmethod
    def myfactorial(a):
        if a == 1 or a == 0:
            return 1
        return a * MyClass1.myfactorial(a - 1)
    # Getter property
    @property
    def classproperty(self):
        return self.l
    # setter property
    @classproperty.setter
    def classproperty(self,item):
        print("Executing setter property==")
        self.l.append(item)

    @property
    def name (self):
        return  self.firstN+" "+self.lastN

    @name.setter
    def name(self,str):
        name_list=str.split(' ')
        self.firstN=name_list[0]
        self.lastN=name_list[1]


if __name__ == "__main__":
    mylist = eval(input("Enter a list:"))
    firstname = input("Enter Firstname:")
    lastname = input("Enter lastname:")
    obj1 = MyClass1(mylist, firstname, lastname)
    print("a===", obj1.a)
    print("L===", obj1.l)
    print("firstname===", obj1.firstN)
    print("lastname===", obj1.lastN)
    print(dir(obj1))
    res = obj1.function1()
    print("sum of list=", res)

    # private methods can not call outside class
 #   obj1.__myprivate()

    # staticmethod factorial call
    fact=int(input("Enter factorial number:"))
    result=MyClass1.myfactorial(fact)
    print("factorial is: ",result)

    # classmethod and staticmethod calling by className
    MyClass1.myclassmethod()
    MyClass1.mystaticmethod()

    # classmethod and staticmethod calling by objectName
    obj1.myclassmethod()
    obj1.mystaticmethod()

    # instance method
    obj1.instance_method()

    # Myclass1.function1()
    print("name===",obj1.name)# this will call getter property name
    obj1.name="Abhay Biradar"# this will call setter
    print("name===",obj1.name)

    # class properties demo
    print("classproperty",obj1.classproperty)
    obj1.classproperty=38
    print("classproperty", obj1.l)
    obj1.classproperty = 1000
    print("classproperty", obj1.l)


