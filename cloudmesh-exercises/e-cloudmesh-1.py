# sp20-516-240 E.Cloudmesh.Common.1

# Develop a program that demonstrates the use f banner, HEADING, and VERBOSE

from cloudmesh.common.util import banner, HEADING
from cloudmesh.common.debug import VERBOSE


class Common1:

    def banner(self):
        banner('This is my banner')

    def heading(self):
        HEADING()
        print('Hello, can you see my heading?')

    def verbose(self, m):
        VERBOSE(m)


if __name__ == "__main__":
    c = Common1()
    c.banner()
    c.heading()
    c.verbose({'key':'value'})
