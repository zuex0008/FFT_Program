#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RooT
#
# Created:     26/10/2014
# Copyright:   (c) RooT 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import math
    k = []
    for j in range(0,128):
        k.append(10*math.sin(2*math.pi*10*j))
    print k


if __name__ == '__main__':
    main()
