# sp20-516-240 E.Cloudmesh.Common.3

# Develop a program that demonstrates the use of FlatDict.

from cloudmesh.common.FlatDict import FlatDict

class Common3:

    def doit(self):
        data = {
            'name': 'Falconi',
            'address': {
                'city': 'Portland',
                'state': 'OR'
            }
        }

        flat = FlatDict(data)
        print(f"My name is {flat.name}")
        print(f"The City I live in is {flat.address__city}")
        print(f"The State I live in is {flat.address__state}")


if __name__ == "__main__":
    c = Common3()
    c.doit()
