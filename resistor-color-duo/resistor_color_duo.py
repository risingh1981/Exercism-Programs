def value(colors):
    color_dict = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    val_str = ""
    for color in colors[:2]:
        val_str += str(color_dict[color])
    return int(val_str)

