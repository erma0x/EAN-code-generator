import barcode



start = 805383785270
num_ean_codes = 20
ean_directory = 'EAN/'


def Save(ean_ ,ean_name, ean13_barcode):
    
    fullname = ean_.save(ean_directory + ean13_barcode)

def generate_ean_code(start_, num_ean_codes_):
    for i in range(start_, start_+num_ean_codes_):
        EAN = barcode.get_barcode_class('ean13')
        codebar = str(i)
        print(codebar)
        ean = EAN(codebar) # extract barcode
        Save(ean_ = EAN, ean_name= str(i)+'_EAN_CODE', ean13_barcode=ean )
        
generate_ean_code(start_=start, num_ean_codes_ = num_ean_codes)
 
