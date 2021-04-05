
import barcode
from barcode.writer import ImageWriter

EAN = barcode.get_barcode_class('ean13')

start = 805383785270      # <- START NUMBER
num_code_to_generate = 3  # <- HOW MANY EAN BARCODE DO YOU WANT?

ean_barcode_directory = "EAN_barcode/"


stop = start + num_code_to_generate

for i in range(start,stop):
    code = str(i)
    ean = EAN(code, writer=ImageWriter())
    print(str(ean))
    fullname = ean.save(ean_barcode_directory+'ean13_barcode_'+code)
