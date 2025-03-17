from helperFunctions import *
from definitions import *

cover_names_leftover = cover_names

'''1429x1417 - old covers'''
cover_new = cover_names[125:]
cover_new_St = getCoversBySize(cover_new, save_path, 1429, 1417)
cover_names_leftover = removeCoversFromList(cover_names_leftover, cover_new_St)

'''1429x1417 - new covers'''
cover_old = cover_names[0:125]
cover_old_St = getCoversBySize(cover_old, save_path, 1429, 1417)
cover_names_leftover = removeCoversFromList(cover_names_leftover, cover_old_St)

'''600x600'''
cover_600_600 = getCoversBySize(cover_names_leftover, save_path, 600, 600)
cover_names_leftover = removeCoversFromList(cover_names_leftover, cover_600_600)

'''600x594'''
cover_600_594 = getCoversBySize(cover_names_leftover, save_path, 600, 594)
cover_names_leftover = removeCoversFromList(cover_names_leftover, cover_600_594)

'''600x590 - Nr.174'''
cover_600_590 = getCoversBySize(cover_names_leftover, save_path, 600, 590)
cover_names_leftover = removeCoversFromList(cover_names_leftover, cover_600_590)

'''600x526 - Nr.175'''
cover_600_526 = getCoversBySize(cover_names_leftover, save_path, 600, 526)
cover_names_leftover = removeCoversFromList(cover_names_leftover, cover_600_526)

'''600x595 - Nr.191'''
cover_600_595 = getCoversBySize(cover_names_leftover, save_path, 600, 595)
cover_names_leftover = removeCoversFromList(cover_names_leftover, cover_600_595)

'''1491x1490 - Nr.150'''
cover_1491_1490 = getCoversBySize(cover_names_leftover, save_path, 1491, 1490)
cover_names_leftover = removeCoversFromList(cover_names_leftover, cover_1491_1490)

'''848x745 - Nr.125'''
cover_848_745 = getCoversBySize(cover_names_leftover, save_path, 848, 745)
cover_names_leftover = removeCoversFromList(cover_names_leftover, cover_848_745)

'''special 04''' 
cover_sp_04 = "sp_04.jpg"  # 1695.0x1488.0

'''special 05''' 
cover_sp_05 = "sp_05.jpg"  # 1519.0x1417.0

'''special 06''' 
cover_sp_06 = "sp_06.jpg"  # 1429.0x1417.0

'''special 07''' 
cover_sp_07 = "sp_07.jpg"  # 1429.0x1417.0

'''special 08''' 
cover_sp_08 = "sp_08.jpg"  # 1429.0x1417.0

'''special 09''' 
cover_sp_09 = "sp_09.jpg"  # 1429.0x1417.0

'''special 10''' 
cover_sp_10 = "sp_10.jpeg" #  500.0x495.0

'''special 11''' 
cover_sp_11 = "sp_11.jpeg" #  600.0x594.0

'''special 12''' 
cover_sp_12 = "sp_12.jpg"  # 1500.0x1500.0

'''special 13''' 
cover_sp_13 = "sp_13.jpeg" #  600.0x594.0

'''special 14''' 
cover_sp_14 = "sp_14.jpg"  # 1429.0x1417.0

'''special 15''' 
cover_sp_15 = "sp_15.jpeg" #  600.0x594.0

'''special 16''' 
cover_sp_16 = "sp_16.jpg"  # 1429.0x1417.0

'''special 18''' 
cover_sp_18 = "sp_18.jpg"  # 1644.0x1475.0

'''special 19''' 
cover_sp_19 = "sp_19.jpg"  # 260.0x260.0

'''special 21''' 
cover_sp_21 = "sp_21.jpg"  # 1429.0x1417.0
