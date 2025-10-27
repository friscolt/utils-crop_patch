#utils_functions.py

import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt


def estimate_num_images(dir_folder):
    list_images = os.listdir(dir_folder)
    #print(list_images)
    cont_images = 0

    for name_image in list_images:
        #print(name_image[-4:])
        if(name_image[-4:] == '.jpg'): #### <---- Change here if images have different format
            #print(name_image)
            cont_images = cont_images + 1
    #print(cont_images)
    return cont_images




def percentage(patch_mask):
    per_height, per_width = patch_mask.shape  
    #print('alto:', per_height)
    #print('ancho:', per_width)
    num_pixels = per_height*per_width
    #print('per_num_pixels: ', per_num_pixels)
    #print(' ')
    mask_normalize = patch_mask/255
    
    #print(mask_normalize)
    #print(' ')
    sum_pixels = np.sum(mask_normalize)
    ratio = (sum_pixels/num_pixels)*100

    """
    print('num_pixels: ', num_pixels)
    print('sum_pixels ', sum_pixels)
    print('ratio: ', round(ratio, 2))
    print(' ')
    """

    return ratio 




def estimate_num_images(dir_folder):
    est_list_images = os.listdir(dir_folder)
    #print(est_list_images)
    est_cont_images = 0

    for est_name_image in est_list_images:
        #print(est_name_image[-4:])
        if(est_name_image[-4:] == '.jpg'): #### <---- Change here if images have different format
            #print(est_name_image)
            est_cont_images = est_cont_images + 1
    #print(est_cont_images)
    return est_cont_images















