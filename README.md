# generate_hash160-Converter
import hashlib

def hash160(data):
    """Calculate the HASH160 of the input data."""
    sha256 = hashlib.sha256(data.encode('utf-8')).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    return ripemd160.hex()

# Specify the input and output files
input_file = "wordlist.txt"  # Your word list
output_file = "hash160_sorted.txt"

# Read the word list from the file
with open(input_file, 'r') as f:
    words = f.readlines()

# Calculate HASH160 values for each word
hashes = [(word.strip(), hash160(word.strip())) for word in words]

# Sort by HASH160 values
hashes.sort(key=lambda x: x[1])

# Save the results to the output file
with open(output_file, 'w') as f:
    for word, h160 in hashes:
        f.write(f"{word},{h160}\n")

print(f"HASH160 values sorted and saved in {output_file}.")
