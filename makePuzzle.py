from helperFunctions import *
from definitions import *

save_path_puzzle        = "puzzles/"
physical_width_in_cm    = 98
physical_height_in_cm   = 75
border_top_in_cm        = 9
border_bottom_in_cm     = 1
border_special_in_cm    = 2 # if = 0, use buffer_Y
border_horizontal_in_cm = 0.5
cover_size              = 700 # 969
min_buffer_X            = 15
min_buffer_Y            = 0
covers_per_row          = 20

include_specials        = True

if include_specials:
    special_str    = "_sp"
else:
    special_str    = ""
    cover_names_sp = []



puzzle_name  = "puzzle"+special_str+"_"+str(physical_width_in_cm)+"x"+str(physical_height_in_cm)+"_cpr"+str(covers_per_row)
puzzle_name += "_bh"+str(border_horizontal_in_cm)+"_bt"+str(border_top_in_cm)+"_bb"+str(border_bottom_in_cm)+"_b2"+str(border_special_in_cm)
puzzle_name += "_cs"+str(cover_size)+"_bx"+str(min_buffer_X)+"_bY"+str(min_buffer_Y)+".jpg"

puzzle = makePuzzle(cover_names, cover_names_sp, save_path_cut, covers_per_row, physical_width_in_cm, physical_height_in_cm, border_horizontal_in_cm, border_top_in_cm, border_bottom_in_cm, border_special_in_cm, cover_size, min_buffer_X, min_buffer_Y)
cv2.imwrite(save_path_puzzle+puzzle_name, puzzle)








