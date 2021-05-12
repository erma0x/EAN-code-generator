#!/usr/bin/python
import barcode
from barcode.writer import ImageWriter
import sys

directory = sys.path[0]

EAN = barcode.get_barcode_class('ean13')

start = 805383785270      # <- START NUMBER
num_code_to_generate = 3  # <- HOW MANY EAN BARCODE DO YOU WANT?

ean_barcode_directory = "/img/"

stop = start + num_code_to_generate

for i in range(start,stop):
    code = str(i)
    path_new_image = directory+ean_barcode_directory+'ean13_barcode_'+code
    
    #print(path_new_image)
    
    ean = EAN(code, writer=ImageWriter())
    fullname = ean.save(path_new_image)
    print(fullname)
