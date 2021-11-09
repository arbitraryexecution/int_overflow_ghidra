import binascii
import os
import sys

# Make sure there are 3 arguments
if len(sys.argv) != 3:
    sys.exit(f"Usage: ./{sys.argv[0]} <input file> <output_file>")

input_fpath = sys.argv[1]
if not os.path.isfile(input_fpath):
    sys.exit(f"ERROR: {input_fpath} is not a valid file!")

with open(input_fpath, 'r') as f:
    data = f.read()

data_bytes = binascii.a2b_hex(data.strip('\n'))

with open(sys.argv[2], 'wb') as f:
    f.write(data_bytes)

print(f'Finished creating file: {sys.argv[2]}')
