import numpy as np
import time
import build.simcore as sm 

# Generate 1 million rows of SME data [cite: 456]
prices = np.random.uniform(10.0, 100.0, 1000000)
quantities = np.random.randint(1, 10, 1000000)

# 1. Test Pure Python Speed
start = time.perf_counter()
py_revenue = sum(p * q for p, q in zip(prices, quantities))
end = time.perf_counter()
print(f"Python Time: {end - start:.6f}s")

# 2. Test C++ Zero-Copy Speed [cite: 322]
start = time.perf_counter()
result = sm.batch_process(prices, quantities)
end = time.perf_counter()
print(f"C++ Zero-Copy Time: {end - start:.6f}s")