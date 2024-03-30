# Paginating a huge book

def page_digits(pages):
    if len(str(pages)) == 1:
        return pages
    digits = 0
    next_lowest = int("9" * (len(str(pages)) - 1))
    digits += (pages - next_lowest) * len(str(pages))
    return digits + page_digits(next_lowest)