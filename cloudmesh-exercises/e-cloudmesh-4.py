# sp20-516-240 E.Cloudmesh.Common.4

# Develop a program that demonstrates the use of cloudmesh.common.Shell.

from cloudmesh.common.Shell import Shell

class Common4:

    def ls(self):
        result = Shell.run('dir')
        print(result)

if __name__ == "__main__":
    c = Common4()
    c.ls()