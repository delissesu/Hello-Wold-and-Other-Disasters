# Menurutku, sederhananya parameter ini memperhatikan urutan
def posParam(num_one : int, num_two : int) -> int:
    return num_one + num_two
print(posParam(1, 2))

# Same, but use string
def strParam(str_one : str, str_two : str) -> str:
    return str_one.__add__(str_two)
print(strParam("Hello ", "World"))