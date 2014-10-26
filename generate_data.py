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
    pi_val = math.pi

    for x in range(0,2050) :
        val1 = 20*math.sin(2*pi_val*t*50) #+ 0* math.sin(2*pi_val*t*100)
        sheet1.write(x,0,t)
        sheet1.write(x,1, float("{0:.4f}".format(val1)) )
        t = t + 0.00003

    book.save("freq_Sample.xls")

if __name__ == '__main__':
    main()
