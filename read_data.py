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
    import xlrd,xlwt,string,numpy
    # location of the data file
    file_name = "C:\\Users\\RooT\\Documents\\GitHub\\fft\\freq_Sample.xls"
    workbook = xlrd.open_workbook(file_name)
    worksheet = workbook.sheet_by_name('Sheet 1')
    # initialize variables
    num_rows = worksheet.nrows - 1
    curr_row = -1
    col1 = []
    col2 = []
    sample = 3
    sam_col1 = []
    sam_col2 = []
    # if sample is set to 0
    if sample == 0 :
        print "Sample point set to 0, setting it to 1"
        sample = 1
    #get row values from xls and feed it into list
    while curr_row < num_rows:
    	curr_row += 1
    	row = worksheet.row(curr_row)
    #Collect data in two columns
        col1.append((str(row[0]).split(':'))[1])
        col2.append((str(row[1]).split(':'))[1])
    #User message if length of data does not match
    if len(col1) <> len(col2) :
        print "User data file is corrupt, col1 row count : " + str(len(col1)) +" and col2 row count : " + str(len(col2))
    else :
        #Filter sample data based on user selection
        for x in range (0,(len(col1))) :
            if (x%sample) == 0 :
                sam_col1.append(str(col1[x]))
                sam_col2.append(str(col2[x]))
        # finding maximum binary samples that can be taken from the filtered sample
        fft_sam_space = pow (2,len(str(bin(len(sam_col1))).split('b')[1]) - 1)
        print fft_sam_space

if __name__ == '__main__':
    main()
