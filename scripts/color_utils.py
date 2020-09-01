def rgb_to_hex(r, g, b, octothorpe=True):
    hex_code = '#' * octothorpe
    for x in (r, g, b):
        hex_code += format(x, 'x').zfill(2)

    return hex_code
