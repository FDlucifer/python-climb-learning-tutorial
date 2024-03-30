# Weight for weight

def order_weight(strng):
    weights = strng.split(" ")
    order_weights = {}
    for weight in weights:
        sum = 0
        for digit in weight:
            sum += int(digit)
        order_weights[weight] = sum
    weights.sort()
    weights.sort(key=lambda x: order_weights[x])
    return " ".join(weights)