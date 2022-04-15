# EAN code generator     .txt or .png
![](https://github.com/erma0x/EAN-code-generator/blob/master/img/ean13_barcode_805383785270.png)

Generate EAN (European-Article-Number) code list in .txt or .png 
The International Article Number (also known as European Article Number or EAN)
is a standard describing a barcode symbology and numbering system used in global trade
to identify a specific retail product type, in a specific packaging configuration,
from a specific manufacturer. 

## Installation
``` python
pip install -r requirements.txt
```

## Usage

1. Change the variables inside the script ean13_barcode.py or ean13.py <br>
       **tot_ean_requested** = total ean requested <br>
       **ean_number** = starting ean number <br>

2. Generate numbers into the txt file
``` python
python3 ean13.py
```
2. Generate ean barcode images into /img/ folder
``` python    
python3 ean13_barcode.py
```
            
