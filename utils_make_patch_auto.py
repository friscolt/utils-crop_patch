#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:36:00 2025

@author: franciscolt
"""

import os
import numpy as np
import pandas as pd
from utils_functions import estimate_num_images
from utils_make_patch_on_images import make_patch_on_images


def make_patch_auto(dir_folder, window_size, req_patch): 
    print('📂 dir_folder:', dir_folder)
    
    # Crear carpeta de salida
    dir_folder_save = os.path.join(dir_folder, 'patch')
    if not os.path.isdir(dir_folder_save):
        os.mkdir(dir_folder_save)
    print('✅ Carpeta para crop-patch:', dir_folder_save)
    
    # -------------------------------------------------------------
    # Calcular número de patches requeridos por imagen
    list_images = [
        f for f in os.listdir(dir_folder)
        if os.path.isfile(os.path.join(dir_folder, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.bmp'))
    ]
    cont_num_images_folder = estimate_num_images(dir_folder)
    patch_per_images = int(req_patch / cont_num_images_folder)
    
    print(f'📸 Total imágenes: {cont_num_images_folder}')
    print(f'🎯 Patches por imagen: {patch_per_images}\n')

    # -------------------------------------------------------------
    results = []  # Lista para almacenar los resultados

    for name_image in list_images:
        print(f'🖼 Procesando imagen: {name_image}')
        best_step_patch = None
        best_num_patch = None
        best_percent = None

        for auto_percent in range(100, 80, -5):  # rango descendente de 100 a 85
            print(f'   🔹 auto_percent = {auto_percent}')
            
            list_num_patch = []
            list_num_step = []

            for auto_step_size in range(1, 200, 1):  # step size de 1 a 45
                pre_cont_num_patch_auto = make_patch_on_images(
                    dir_folder, name_image, window_size, auto_step_size, auto_percent, 0, 0)
                
                list_num_patch.append(pre_cont_num_patch_auto)
                list_num_step.append(auto_step_size)
            
            list_num_patch = np.array(list_num_patch)
            list_num_step = np.array(list_num_step)

            # Si no se generaron patches, pasar al siguiente auto_percent
            if list_num_patch.size == 0 or list_num_patch[0] == 0:
                print("   ⚠️  No se generaron patches. Pasando al siguiente auto_percent...\n")
                continue
            
            # Seleccionar el step que produce un número de patches más cercano al deseado
            idx_best = np.argmin(np.abs(list_num_patch - patch_per_images))
            best_num_patch = list_num_patch[idx_best]
            best_step_patch = list_num_step[idx_best]
            best_percent = auto_percent

            print(f'   ✅ Best number of patch: {best_num_patch} of {patch_per_images} required')
            print(f'   ✅ Best step patch: {best_step_patch}\n')
            
            break  # ya encontró un buen valor, salir del loop de percent
        
        if best_step_patch is None:
            print(f'⚠️ No se encontró configuración válida para {name_image}, se omite.\n')
            continue
        
        print(f'✅ Imagen {name_image} procesada con best_step = {best_step_patch}\n')
        
        auto_num_patch = make_patch_on_images(
            dir_folder, name_image, window_size, best_step_patch, best_percent, 1, patch_per_images)
        
        # Agregar fila de resultados
        results.append({
            'name_image': name_image,
            'num_patch_auto': auto_num_patch,
            'window_size': window_size,
            'auto_step_size': best_step_patch,
            'percent': best_percent
        })

    # -------------------------------------------------------------
    # Crear DataFrame final
    df_features = pd.DataFrame(results)
    print('\n📊 Tabla final de resultados:')
    print(df_features)
    
    # Guardar opcionalmente como CSV
    save_path = os.path.join(dir_folder_save, 'summary_patch_info.csv')
    df_features.to_csv(save_path, index=False)
    print(f'\n💾 Tabla guardada en: {save_path}')
    
    return df_features


































"""
import os 
import numpy as np
import pandas as pd
from utils_functions import estimate_num_images
from utils_make_patch_on_images import make_patch_on_images


def make_patch_auto(dir_folder, window_size, req_patch): 
    print('📂 dir_folder:', dir_folder)
    
    # Crear carpeta de salida
    dir_folder_save = os.path.join(dir_folder, 'patch')
    if not os.path.isdir(dir_folder_save):
        os.mkdir(dir_folder_save)
    print('✅ Carpeta para crop-patch:', dir_folder_save)
    
    # -------------------------------------------------------------
    # Calcular número de patches requeridos por imagen
    list_images = [
        f for f in os.listdir(dir_folder)
        if os.path.isfile(os.path.join(dir_folder, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.bmp'))
    ]
    cont_num_images_folder = estimate_num_images(dir_folder)
    patch_per_images = int(req_patch / cont_num_images_folder)
    
    print(f'📸 Total imágenes: {cont_num_images_folder}')
    print(f'🎯 Patches por imagen: {patch_per_images}\n')

    # -------------------------------------------------------------
    for name_image in list_images:
        print(f'🖼 Procesando imagen: {name_image}')
        #cont_patch_auto = 0
        
        for auto_percent in range(100, 80, -5):  # rango descendente de 100 a 85
            print(f'   🔹 auto_percent = {auto_percent}')
            
            list_num_patch = []
            list_num_step = []

            for auto_step_size in range(1, 50, 5):  # step size de 1 a 45
                pre_cont_num_patch_auto = make_patch_on_images(
                    dir_folder, name_image, window_size, auto_step_size, auto_percent, 0, 0)
                
                # almacenar resultados
                list_num_patch.append(pre_cont_num_patch_auto)
                list_num_step.append(auto_step_size)
            
            list_num_patch = np.array(list_num_patch)
            list_num_step = np.array(list_num_step)

            # Si no se generaron patches, pasar al siguiente auto_percent
            if list_num_patch.size == 0 or list_num_patch[0] == 0:
                print("   ⚠️  No se generaron patches. Pasando al siguiente auto_percent...\n")
                continue
            
            # -------------------------------------------------------------
            # Seleccionar el step que produce un número de patches más cercano al deseado
            idx_best = np.argmin(np.abs(list_num_patch - patch_per_images))
            best_num_patch = list_num_patch[idx_best]
            best_step_patch = list_num_step[idx_best]

            print(f'   ✅ Best number of patch: {best_num_patch} of {patch_per_images} required')
            print(f'   ✅ Best step patch: {best_step_patch}\n')
            
            # Ya se encontró un buen valor, no es necesario seguir con otros auto_percent
            break
        
        print(f'✅ Imagen {name_image} procesada con best_step = {best_step_patch}\n')
        
        auto_num_patch = make_patch_on_images(
            dir_folder, name_image, window_size, best_step_patch, auto_percent, 1, patch_per_images)
        #print('Number ',auto_num_patch)
        
        
        
        info_patch_img = np.hstack((name_image, auto_num_patch, window_size, best_step_patch, auto_percent))
        #print(info_patch_img)

        if (cont_num_images == 0):
            table_num_patch_image = info_patch_img
            cont_num_images = cont_num_images + 1
        else:
            table_num_patch_image = np.vstack((table_num_patch_image,info_patch_img))
        
    df_features = pd.DataFrame(table_num_patch_image, columns = ['name_image', 'num_patch_auto', 'window_size', 'auto_step_size', 'percent'])
    #print('\n', df_features)
    return df_features    
        
"""
        

 