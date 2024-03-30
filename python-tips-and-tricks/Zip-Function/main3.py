sales = [500, 800, 300, 1200, 600]
costs = [200, 600, 200, 100, 800]

for sale, cost in zip(sales, costs):
    print(sale-cost)