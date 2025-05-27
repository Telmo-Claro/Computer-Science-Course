dict_key_value = {}
key = r"a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"
data = "yourmomlovescock"


for index in range(0, len(key), 2):
    dict_key_value[key[index]] = key[index + 1]


def encode_string(data, key):
    hashed_string = ""
    for key, value in dict_key_value.items():
        for index in range(len(data)):
            # a:_
            # 0
            if key == data[index]:
                # if input = a
                hashed_string += value
                index += 1
                break
                # if input != a, hashed string + input(letter in index)
            index += 1
            hashed_string += data[index]
            break
    return hashed_string


print(encode_string(data, dict_key_value))
