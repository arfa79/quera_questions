# یک دیکشنری از نام سنگ‌ها و رنگ‌هایشان
stone_colors = {
    "space": "blue",
    "mind": "yellow",
    "reality": "red",
    "power": "purple",
    "time": "green",
    "soul": "orange"
}

# ورودی را گرفته و رنگ مربوطه را چاپ می‌کند
def print_stone_color(stone_name):
    if stone_name in stone_colors:
        print(stone_colors[stone_name])
    else:
        print("Invalid stone name!")

# تست‌های مختلف
print_stone_color("time")  # این باید "green" چاپ کنه
print_stone_color("power")  # این باید "purple" چاپ کنه
print_stone_color("space")  # این باید "blue" چاپ کنه
print_stone_color("soul")  # این باید "orange" چاپ کنه
print_stone_color("mind")  # این باید "yellow" چاپ کنه
print_stone_color("reality")  # این باید "red" چاپ کنه
print_stone_color("unknown")  # این باید "Invalid stone name!" چاپ کنه
