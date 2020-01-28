# sp20-516-240 E.Cloudmesh.Common.2

# Develop a program that demonstrates the use of dotdict.

from cloudmesh.common.dotdict import dotdict

class Common2:

    def doit(self):
        data = {'name': 'Falconi'}
        data = dotdict(data)
        print(f"My name is {data.name}")

        if data.name == 'Falconi':
            print('this is quite readable')

if __name__ == "__main__":
    c = Common2()
    c.doit()
