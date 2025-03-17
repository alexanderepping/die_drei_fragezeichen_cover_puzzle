import requests
import cv2
import math
import numpy as np

def getCoverNames(cover_pair_array):
    cover_names = []
    for pair in cover_pair_array:
        cover_names += [pair[0]]
    return cover_names

def downloadCovers(url_pre, save_path, cover_pair_array):
    print("\n\nSTART DOWNLOADING COVERS...")
    for cover_pair in cover_pair_array:
        print("Downloading "+cover_pair[0])
        file_name = save_path + cover_pair[0]
        url       = url_pre   + cover_pair[1]

        data = requests.get(url).content
        f=open(file_name, 'wb')
        f.write(data)
        f.close()
    return 1

def getCoversBySize(cover_names, save_path, size_0, size_1):
    correct_covers = []
    for name in cover_names:
        img = cv2.imread(save_path+name)
        sz_0 = img[0,:].size/3
        sz_1 = img[:,0].size/3
        if ((size_0 == sz_0) and (size_1 == sz_1)):
            correct_covers += [name]
    print("\nCovers with size "+str(size_0)+"x"+str(size_1)+":")
    print(correct_covers)
    return correct_covers

def getSize(name):
    img = cv2.imread(name)
    size_0 = img[0,:].size/3
    size_1 = img[:,0].size/3
    print(name+": "+str(size_0)+"x"+str(size_1))
    return [size_1, size_0]

def cutImages(cover_names, sizes, save_path, save_path_cut):
    for name in cover_names:
        img = cv2.imread(save_path+name)
        img2 = img[sizes[0]:sizes[1],sizes[2]:sizes[3]]
        #img2 = img[414:1383,225:1194]
        cv2.imwrite(save_path_cut+name, img2)
        print("Successful cut: "+name)
        #print(str(img2[0,:].size/3)+"x"+str(img2[:,0].size/3))
    return 1

def removeCoversFromList(cover_names_leftover, cover_names):
    cover_names_left = cover_names_leftover
    for name in cover_names:
        cover_names_left.remove(name)
    return cover_names_left

# buffers are only added between covers
def makePuzzle(cover_names, cover_names_sp, path_to_files, covers_per_row, physical_width_in_cm, physical_height_in_cm, border_horizontal_in_cm, border_top_in_cm, border_bottom_in_cm, border_special_in_cm, cover_size, min_buffer_X, min_buffer_Y):
    width  = physical_width_in_cm  - 2 * border_horizontal_in_cm
    height = physical_height_in_cm - (border_top_in_cm + border_bottom_in_cm + border_special_in_cm)

    number_of_covers    = len(cover_names)
    number_of_covers_sp = len(cover_names_sp)
    number_of_rows_standard = math.ceil(number_of_covers/covers_per_row) # round up
    number_of_rows_special  = math.ceil(number_of_covers_sp/covers_per_row) # round up
    number_of_rows          = number_of_rows_standard + number_of_rows_special

    if border_special_in_cm == 0:
        min_height_overall = number_of_rows * cover_size + (number_of_rows - 1) * min_buffer_Y
        min_width_overall  = covers_per_row * cover_size + (covers_per_row - 1) * min_buffer_X
    else:
        min_height_overall = number_of_rows * cover_size + (number_of_rows - 2) * min_buffer_Y
        min_width_overall  = covers_per_row * cover_size + (covers_per_row - 1) * min_buffer_X

    if width/min_width_overall > height/min_height_overall:
        buffer_Y = min_buffer_Y

        if border_special_in_cm == 0:
            overall_height = number_of_rows * cover_size  + (number_of_rows - 1) * buffer_Y
        else:
            overall_height = number_of_rows * cover_size  + (number_of_rows - 2) * buffer_Y

        overall_width  = overall_height / height * width # could be a non-integer

        buffer_X = math.ceil((overall_width - covers_per_row * cover_size) / (covers_per_row - 1))
        overall_width  = covers_per_row * cover_size  + (covers_per_row - 1) * buffer_X
        pixels_per_cm  = overall_height  / height

    else:
        buffer_X = min_buffer_X

        overall_width  = covers_per_row * cover_size  + (covers_per_row - 1) * buffer_X
        overall_height = overall_width / width * height # could be a non-integer

        if border_special_in_cm == 0:
            buffer_Y = math.ceil((overall_height - number_of_rows * cover_size) / (number_of_rows - 1))
            overall_height = number_of_rows * cover_size  + (number_of_rows - 1) * buffer_Y
        else:
            buffer_Y = math.ceil((overall_height - number_of_rows * cover_size) / (number_of_rows - 2))
            overall_height = number_of_rows * cover_size  + (number_of_rows - 2) * buffer_Y
        pixels_per_cm  = overall_width  / width


    physical_overall_width  = math.ceil(pixels_per_cm * physical_width_in_cm)
    physical_overall_height = math.ceil(pixels_per_cm * physical_height_in_cm)
    height_border_top       = math.ceil(pixels_per_cm * border_top_in_cm)
    height_border_special   = math.ceil(pixels_per_cm * border_special_in_cm)
    width_border_horizontal = math.ceil(pixels_per_cm * border_horizontal_in_cm)
    overall_buffer_X_in_cm  = (covers_per_row - 1) * buffer_X / pixels_per_cm
    if border_special_in_cm == 0:
        overall_buffer_Y_in_cm  = (number_of_rows - 1) * buffer_Y / pixels_per_cm
    else:
        overall_buffer_Y_in_cm  = (number_of_rows - 2) * buffer_Y / pixels_per_cm


    puzzle = np.zeros((physical_overall_height, physical_overall_width, 3), np.uint8)
    for i_y in range(number_of_rows_standard):
        for i_x in range(covers_per_row):
            cover_number = (i_y)*covers_per_row + i_x
            if cover_number < number_of_covers:
                name = cover_names[cover_number]

                img        = cv2.imread(path_to_files+name)
                img_resize = cv2.resize(img, (cover_size, cover_size))

                y_pos = i_y * (cover_size + buffer_Y) + height_border_top
                x_pos = i_x * (cover_size + buffer_X) + width_border_horizontal
                puzzle[y_pos:y_pos+cover_size,x_pos:x_pos+cover_size] = img_resize
                print("Successful addition: "+name)

    for i_y in range(number_of_rows_special):
        for i_x in range(covers_per_row):
            cover_number = (i_y)*covers_per_row + i_x
            if cover_number < number_of_covers_sp:
                name = cover_names_sp[cover_number]

                img        = cv2.imread(path_to_files+name)
                img_resize = cv2.resize(img, (cover_size, cover_size))

                y_pos = (i_y + number_of_rows_standard) * (cover_size + buffer_Y) + height_border_top + height_border_special
                x_pos = i_x * (cover_size + buffer_X) + width_border_horizontal
                puzzle[y_pos:y_pos+cover_size,x_pos:x_pos+cover_size] = img_resize
                print("Successful addition: "+name)


    print("height_border_special = "+str(height_border_special))
    print("buffer_X = "+str(buffer_X))
    print("buffer_Y = "+str(buffer_Y))
    print("overall_buffer_X_in_cm = "+str(overall_buffer_X_in_cm))
    print("overall_buffer_Y_in_cm = "+str(overall_buffer_Y_in_cm))
    return puzzle
