
import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt

from utils_functions import percentage  


def make_patch_on_images(dir_folder, name_img, window_size, step_size, percent, write_patch, req_patch):
    """
    Genera parches (patches) de una imagen con base en una máscara, 
    según un umbral de porcentaje y parámetros de ventana y paso.

    Parameters:
        dir_folder (str): Carpeta que contiene las imágenes y subcarpeta 'mask/'.
        name_img (str): Nombre de la imagen a procesar.
        window_size (int): Tamaño de la ventana cuadrada del patch.
        step_size (int): Paso entre parches consecutivos.
        percent (float): Porcentaje mínimo de área activa en la máscara.
        write_patch (int): Si es 1, guarda los patches en disco.
        req_patch (int): Número máximo de patches a generar por imagen.

    Returns:
        counter_num_patch (int): Número total de patches generados.
    """

    # ---------------------------------------------------------------
    # Rutas
    dir_image = os.path.join(dir_folder, name_img)
    dir_mask = os.path.join(dir_folder, 'mask', name_img)

    # Asegurar que la máscara tenga extensión .png
    if dir_mask.lower().endswith('.jpg'):
        dir_mask = dir_mask[:-4] + '.png'

    # ---------------------------------------------------------------
    # Cargar imagen y máscara
    image_color = cv2.imread(dir_image)
    image_gray = cv2.imread(dir_mask, cv2.IMREAD_GRAYSCALE)

    if image_color is None:
        print(f"⚠️  No se pudo leer la imagen: {dir_image}")
        return 0
    if image_gray is None:
        print(f"⚠️  No se pudo leer la máscara: {dir_mask}")
        return 0

    # ---------------------------------------------------------------
    height_img, width_img, _ = image_color.shape
    d = (window_size - 1) // 2  # Distancia del centro

    counter_num_patch = 0

    # ---------------------------------------------------------------
    # Iterar sobre posiciones de la imagen
    for x in range(d, height_img - d, step_size):
        for y in range(d, width_img - d, step_size):

            patch_img = image_color[x - d:x + d + 1, y - d:y + d + 1, :]
            patch_mask = image_gray[x - d:x + d + 1, y - d:y + d + 1]

            ratio = percentage(patch_mask)  # <- función externa

            if ratio > percent:
                counter_num_patch += 1

                # Solo guardar si se indicó y no se superó el número requerido
                if write_patch == 1:
                    if counter_num_patch <= req_patch:
                        my_name = os.path.splitext(name_img)[0]
                        my_ext = os.path.splitext(name_img)[1]
                        name_image_no_patch = f"{my_name} - patch {counter_num_patch}{my_ext}"

                        dir_folder_save = os.path.join(dir_folder, 'patch')
                        os.makedirs(dir_folder_save, exist_ok=True)
                        path_patch_save = os.path.join(dir_folder_save, name_image_no_patch)

                        # Guardar imagen
                        #cv2.imwrite(path_patch_save, patch_img)
                        print(f"💾 Guardado patch: {path_patch_save}")

                    else:
                        print(f"✅ Se alcanzaron {req_patch} patches. Rompiendo el ciclo...\n")
                        return counter_num_patch  # <-- salir inmediatamente

    # ---------------------------------------------------------------
    print(f"🔹 Total patches generados: {counter_num_patch} | Window={window_size}, Step={step_size}, Percent={percent}")
    return counter_num_patch





















