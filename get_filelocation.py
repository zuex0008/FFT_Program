#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      RooT
#
# Created:     28/10/2014
# Copyright:   (c) RooT 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    from Tkinter import Tk
    from tkFileDialog import askopenfilename
    import xlrd
    curr_row = -1

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    file_name = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(file_name)

    # open xls sheet
    workbook = xlrd.open_workbook(file_name)
    worksheet = workbook.sheet_by_index(0)

    num_rows = worksheet.nrows - 1
    while curr_row < num_rows:
    	curr_row += 1
    	print worksheet.row(curr_row)

if __name__ == '__main__':
    main()
