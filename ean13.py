# Ermano Buikis

import barcodenumber

ean_number = '9788478290222' # start from this number
tot_ean_requested = 200     # produce tot ean codes in txt format
name_file_output = 'ean13_numbers.txt'
ean_produced = 0

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
