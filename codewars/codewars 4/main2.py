def page_digits(pages):
    length = len(str(pages))
    if length == 1 or pages == 0:
        return pages
    digits = 0
    next_lowest = int("9" * (length - 1))
    digits += (pages - next_lowest) * length
    return digits + page_digits(next_lowest)