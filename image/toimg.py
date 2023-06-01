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

def padding(arr, w, h):
    arr = arr[:]
    length = len(arr)
    for i in range(h - len(arr)):
        arr.append([0] * w)
    return arr

ls = ["packet_0", "packet_1", "packet_2"]
for i in range(0, 10001):
    ls.append(f"packet_{i}")

for i, fname in enumerate(ls):
    print(f"{i}, ", len(read_binary_file(f"packets/{fname}")))

    continue
    binary_data = d2(read_binary_file(f"packets/{fname}"), 40)
    binary_data = padding(binary_data, 40, 40)

    #checkarr(binary_data)
    save_binary_as_image(f'results/{fname}.png', binary_data)
