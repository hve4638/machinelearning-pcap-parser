from PIL import Image
import numpy as np

def checkarr(array):
    height = len(array)
    if height == 0:
        print("Empty array")
        return

    width = len(array[0])

    print("Height:", height)
    print("Widths:", end=" ")
    for inner_array in array:
        print(len(inner_array), end=" ")
    print()

def read_binary_file(filename):
    with open(filename, 'rb') as f:
        byte_list = list(f.read())
    return byte_list

def save_binary_as_image(filename, binary_data):
    array_data = np.array(binary_data)
    image = Image.fromarray(array_data.astype(np.uint8))
    image.save(filename)

def d2(arr, max_length):
    num_elements = len(arr)
    if num_elements < max_length:
        padding = [0] * (max_length - num_elements)
        arr.extend(padding)
    num_rows = (num_elements + max_length - 1) // max_length
    two_d_array = [arr[i * max_length: (i + 1) * max_length] for i in range(num_rows)]
    if num_elements % max_length != 0:
        padding = [0] * (max_length - num_elements % max_length)
        two_d_array[-1].extend(padding)

    return two_d_array

def arr_padding(arr, w, h):
    arr = arr[:]
    length = len(arr)
    for i in range(h - len(arr)):
        arr.append([0] * w)
    return arr

def arr_truncate(array, cut_rows, cut_cols):
    rows = len(array)
    cols = len(array[0])

    if cut_rows <= rows and cut_cols <= cols:
        cut_array = [row[:cut_cols] for row in array[:cut_rows]]
    else:
        cut_array = array

    return cut_array
