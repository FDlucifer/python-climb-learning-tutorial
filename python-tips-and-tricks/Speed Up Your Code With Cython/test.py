import main
import time

start_vanilla = time.time()
print("prime_finder_vanilla: ", main.prime_finder_vanilla(4000))
end_vanilla = time.time()
print("prime_finder_vanilla used time:", end_vanilla - start_vanilla)

start_optimized = time.time()
print("prime_finder_optimized: ", main.prime_finder_optimized(6000))
end_optimized = time.time()
print("prime_finder_optimized used time:", end_optimized - start_optimized)