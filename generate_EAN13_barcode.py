import barcode
from barcode.writer import ImageWriter
EAN = barcode.get_barcode_class('ean13')

start = 805383785270
num_code_to_generate = 2000
stop = start + num_code_to_generate

f = open('ean.txt', 'a+')
for i in range(start,stop):
    code = str(i)
    ean = EAN(code, writer=ImageWriter())
    print(str(ean))
    f.write(str(ean)+'\n')
    #fullname = ean.save('EAN/ean13_barcode_'+code)
