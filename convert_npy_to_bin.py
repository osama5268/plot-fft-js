import os
import json
import numpy as np

# to convert npy formats to simple bin formats to load in browser js
path = "."
files = os.listdir(path)
files = [f for f in files if f.__contains__("samples.npy")]

for file in files:
    samples = np.load(file)
    samples_interleaved = np.empty(samples.size * 2, dtype=np.float32)
    samples_interleaved[0::2] = samples.real
    samples_interleaved[1::2] = samples.imag
    samples_interleaved.tofile("samples.bin")

    # Save metadata JSON
    meta = {
        "dtype": "float32",
        "length": len(samples),
        "is_complex": True,
    }
    with open("samples.json", "w") as f:
        import json

        json.dump(meta, f)
