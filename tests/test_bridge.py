import sys
import os

# 1. Construct the absolute path to the folder containing simcore.pyd
# This goes up one level from 'tests', then into 'build/src/Release'
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "build", "src"))

# 2. Add that specific folder to sys.path
sys.path.append(module_path)

try:
    # 3. Import the module name directly (simcore), NOT build.src.simcore
    import simcore
    print("Success! simcore imported from:", module_path)
except ImportError as e:
    print(f"Error: Could not find simcore.pyd in {module_path}")
    print(f"Actual error: {e}")

import numpy as np
import time

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
result = simcore.batch_process(prices, quantities)
end = time.perf_counter()
print(f"C++ Zero-Copy Time: {end - start:.6f}s")