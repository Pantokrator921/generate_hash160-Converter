import hashlib

def hash160(data):
    sha256 = hashlib.sha256(data.encode('utf-8')).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    return ripemd160.hex()

# Datei mit Wortliste laden
input_file = "wordlist.txt"  # Ihre Wortliste
output_file = "hash160_sorted.txt"

# Hash160-Werte berechnen
with open(input_file, 'r') as f:
    words = f.readlines()

hashes = [(word.strip(), hash160(word.strip())) for word in words]

# Nach Hash160 sortieren
hashes.sort(key=lambda x: x[1])

# Ergebnisse speichern
with open(output_file, 'w') as f:
    for word, h160 in hashes:
        f.write(f"{word},{h160}\n")

print(f"Hash160-Werte sortiert und in {output_file} gespeichert.")
