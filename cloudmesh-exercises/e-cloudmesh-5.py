# sp20-516-240 E.Cloudmesh.Common.5

# Develop a program that demonstrates the use of cloudmesh.common.StopWatch.

from cloudmesh.common.StopWatch import StopWatch
from time import sleep

class Common5:

    def doit(self):
        StopWatch.start('test')
        sleep(1)
        StopWatch.stop('test')

        print(StopWatch.get('test'))
        StopWatch.benchmark()

if __name__ == "__main__":
    c = Common5()
    c.doit()