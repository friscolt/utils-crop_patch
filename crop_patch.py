#crop_patch.py

import os 
import pandas as pd

from utils_make_patch_auto import make_patch_auto

# To set parameters: 
# **************************************************************************************************** 
window_size = 256
req_patch_total = 200
# **************************************************************************************************** 


# To read files from subtype folder: 
print('Reading files from subtype folder ...')
# **************************************************************************************************** 
# For section dataset
dir_root = '.../dataset/SEC/'
dir_subtypes = ["SEC-Subtype_Ia", "SEC-Subtype_IIa","SEC-Subtype_IIIa","SEC-Subtype_IVc","SEC-Subtype_IVd","SEC-Subtype_Va"]

"""
# For surface dataset
dir_root = '.../dataset/SUR/'
dir_subtypes = ["SUR-Subtype_Ia", "SUR-Subtype_IIa", "SUR-Subtype_IIIa", "SUR-Subtype_IVc", "SUR-Subtype_IVd", "SUR-Subtype_Va"]
"""

# For testing with one subtype only
#dir_subtypes = ["SEC-Subtype_Ia"]

for subtype in dir_subtypes:
    print("Processing subtype:", subtype)
    dir_folder = dir_root + subtype  # folder with images

    print('Current directory >> ', dir_folder, '\n', '*'*100)
    
    #To make patch auto: 
    print('Making patch auto ...')
    # ************************************************** 
    table_patch = make_patch_auto(dir_folder, window_size, req_patch_total) 
    
    print(table_patch)
    table_name = 'table_patch_' + subtype + '_' + str(window_size) + '.csv'
    table_patch.to_csv(table_name, index=False)






