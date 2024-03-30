# Directions Reduction

def dirReduc(arr):
    changed = True
    arr = " ".join(arr)
    while changed:
        changed = False
        old = arr
        arr = arr.replace("EAST WEST", "")
        arr = arr.replace("WEST EAST", "")
        arr = arr.replace("SOUTH NORTH", "")
        arr = arr.replace("NORTH SOUTH", "")
        arr = arr.replace("  ", " ")
        if arr.startswith(" "):
            arr = arr[1:]
        if arr.endswith(" "):
            arr = arr[:-1]
        print(arr)
        if arr == old:
            return arr.split(" ") if arr.split(" ") != [''] else []
        else:
            changed = True