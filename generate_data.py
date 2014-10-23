#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RooT
#
# Created:     23/10/2014
# Copyright:   (c) RooT 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import math,xlwt
    t = 0   # sampling time
    val1 = 0

    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")


    for x in range(0,3000) :
        t = t + 1.5e-05
        val1 = 1*math.sin(2*math.pi*t*10) + 2*math.sin(2*math.pi*t*20)
        sheet1.write(x,0,t)
        sheet1.write(x,1, val1 )


    book.save("freq_Sample.xls")

if __name__ == '__main__':
    main()
