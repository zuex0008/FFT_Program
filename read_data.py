#-------------------------------------------------------------------------------
# Name:        Read data from xls and create fft data
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
    file_name = ".\\freq_Sample.xls"
    workbook = xlrd.open_workbook(file_name)
    worksheet = workbook.sheet_by_name('Sheet 1')
    # location of saved data file
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    # initialize variables
    num_rows = worksheet.nrows - 1
    curr_row = -1
    # fft complex values
    fft_complex = []
    # fft amplitude values
    fft_amp = []
    # time stamp
    col1 = []
    # sampled values
    col2 = []
    float_col2 = []
    sample = input ('Enter number of samples to be taken from data space:- ')
    print "User selected sample space :- " , sample
    # filterd data based on user sample selected
    fil_col1 = []
    fil_col2 = []
    # maximum 2^N samples taken from filtered data
    sam_col1 = []
    sam_col2 = []
    # output frequency
    freq_out = []
    freq_out.insert(0, 0.0)
    # if sample is set to 0
    if sample == 0 :
        print "Sample point set to 0, setting it to 1"
        sample = 1
    #get row values from xls and feed it into list
    while curr_row < num_rows:
    	curr_row += 1
    	row = worksheet.row(curr_row)
    #Collect data in two columns
        col1.append(float((str(row[0]).split(':'))[1]))
        col2.append(float((str(row[1]).split(':'))[1]))

    #User message if length of data does not match
    if len(col1) <> len(col2) :
        print "User data file is corrupt, col1 row count : " + str(len(col1)) +" and col2 row count : " + str(len(col2))
    else :
        #calculate sampling frequency from the time
        sam_freq = len(col1) / (float(col1[len(col1)-1])- float(col1[0]))
        print "Sampling frequency is actual data set : " + str(sam_freq)

        #Filter sample data based on user selection
        for x in range (0,(len(col1))) :
            if (x%sample) == 0 :
                fil_col1.append(col1[x])
                fil_col2.append(col2[x])
        print fil_col1[0] ,fil_col1[len(fil_col1)-1]

        # finding maximum binary samples that can be taken from the filtered sample
        fft_sam_space = pow (2,len(str(bin(len(fil_col1))).split('b')[1]) - 1)
        print fft_sam_space , len(fil_col1), len(fil_col2)

        # creating sampled data from filtered data
        for j in range(0,fft_sam_space):
            sam_col1.append(fil_col1[j])
            sam_col2.append(fil_col2[j])
        print sam_col1[0] ,sam_col1[len(sam_col1)-1]

        #calculating fft for the sampled data
        fft_complex = numpy.fft.rfft(sam_col2)

        #calculate sampling frequency from the time
        sam_freq1 = float(("{0:.4f}").format(len(sam_col1) / (sam_col1[len(sam_col1)-1]- sam_col1[0])))
        print "Sampling frequency is from binary sampled data set : " + str(sam_freq1)

        # generate frequency data fro xls
        for k in range (1,((len(sam_col1)/2)+1)):
            freq_out.append(float(("{0:.4f}").format(freq_out[k-1]+ sam_freq1/len(sam_col1))))
        print freq_out[len(freq_out)-1] ,len(freq_out)

        # generate amplitude from fft complex data
        for j in range(0,len(fft_complex)) :
            fft_amp.append(float(("{0:.4f}").format(abs(fft_complex[j])/(fft_sam_space/2))))

        # save time data from master file to excel file
        sheet1.write(0,0,'Time')
        for j in range(0,len(col1)) :
            sheet1.write(j+1,0,col1[j])
        # save data from master file to excel file
        sheet1.write(0,1,'Data')
        for j in range(0,len(col2)) :
            sheet1.write(j+1,1,col2[j])

        # save filtered time to excel file
        sheet1.write(0,3,'Filtered_Time')
        for j in range(0,len(fil_col1)) :
            sheet1.write(j+1,3,fil_col1[j])
        # save filtered data to excel file
        sheet1.write(0,4,'Filtered_Data')
        for j in range(0,len(fil_col2)) :
            sheet1.write(j+1,4,fil_col2[j])

        # save sampled time to excel file
        sheet1.write(0,6,'Sampled_Time')
        for j in range(0,len(sam_col1)) :
            sheet1.write(j+1,6,sam_col1[j])
        # save sampled data to excel file
        sheet1.write(0,7,'Sampled_Data')
        for j in range(0,len(sam_col2)) :
            sheet1.write(j+1,7,sam_col2[j])

        # save freq of the sampled data
        sheet1.write(0,9,'FFT_Complex')
        for j in range(0,len(fft_complex)) :
            sheet1.write(j+1,9,str(fft_complex[j]))
        # save freq of the sampled data
        sheet1.write(0,11,'FFT_Amplitude')
        for j in range(0,len(fft_amp)) :
            sheet1.write(j+1,11,fft_amp[j])
        # save freq of the sampled data
        sheet1.write(0,10,'FFT_Frequency')
        for j in range(0,len(freq_out)) :
            sheet1.write(j+1,10,freq_out[j])

        # save the excel file
        book.save('FFT_Result.xls')

if __name__ == '__main__':
    main()