#!/usr/bin/python3
import barcodenumber

###################################
# START NUMBER

ean_number = '8053831640150'  # <<<---- HERE
# modify your starting number here

tot_ean_requested = 300     # produce tot ean codes in txt format

name_file_output = 'ean13_numbers.txt' # name of the output file .txt for the numbers

###################################

ean_produced = 0

if len(ean_number) != 13:
   print ('error : your ean number has not 13 digits' )

else:
    while ean_produced < tot_ean_requested :
    	valid = barcodenumber.check_code('ean13',ean_number)
    	if valid:
    	    with open(name_file_output, '+a') as f: 
    	    # every restart of this program delete the file .txt
    	        f.write( ean_number+'\n')
            
    	        ean_number = str(1+int(ean_number))
    	        ean_produced += 1

    	else:
    	    ean_number = str(1+int(ean_number))
