import cv2
from helperFunctions import *
from definitions import *
from cutAllCovers_ranges import *
from cutAllCovers_categorization import *



##############################
# cut images
##############################
cutImages(cover_old_St,    sizes_old_St,    save_path, save_path_cut)
cutImages(cover_new_St,    sizes_new_St,    save_path, save_path_cut)
cutImages(cover_600_600,   sizes_600_600,   save_path, save_path_cut)
cutImages(cover_600_594,   sizes_600_594,   save_path, save_path_cut)
cutImages(cover_600_590,   sizes_600_590,   save_path, save_path_cut)
cutImages(cover_600_526,   sizes_600_526,   save_path, save_path_cut)
cutImages(cover_600_595,   sizes_600_595,   save_path, save_path_cut)
cutImages(cover_1491_1490, sizes_1491_1490, save_path, save_path_cut)
cutImages(cover_848_745,   sizes_848_745,   save_path, save_path_cut)

cutImages([cover_sp_04],   sizes_sp_04,     save_path, save_path_cut)
cutImages([cover_sp_05],   sizes_sp_05,     save_path, save_path_cut)
cutImages([cover_sp_06],   sizes_sp_06,     save_path, save_path_cut)
cutImages([cover_sp_07],   sizes_sp_07,     save_path, save_path_cut)
cutImages([cover_sp_08],   sizes_sp_08,     save_path, save_path_cut)
cutImages([cover_sp_09],   sizes_sp_09,     save_path, save_path_cut)
cutImages([cover_sp_10],   sizes_sp_10,     save_path, save_path_cut)
cutImages([cover_sp_11],   sizes_sp_11,     save_path, save_path_cut)
cutImages([cover_sp_12],   sizes_sp_12,     save_path, save_path_cut)
cutImages([cover_sp_13],   sizes_sp_13,     save_path, save_path_cut)
cutImages([cover_sp_14],   sizes_sp_14,     save_path, save_path_cut)
cutImages([cover_sp_15],   sizes_sp_15,     save_path, save_path_cut)
cutImages([cover_sp_16],   sizes_sp_16,     save_path, save_path_cut)
cutImages([cover_sp_18],   sizes_sp_18,     save_path, save_path_cut)
cutImages([cover_sp_19],   sizes_sp_19,     save_path, save_path_cut)
cutImages([cover_sp_21],   sizes_sp_21,     save_path, save_path_cut)
