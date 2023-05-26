import hashlib

# Input data
data = "Khlid Arif"

# Create a SHA-256 hash object
sha256_hash = hashlib.sha256()

# Update the hash object with the input data
sha256_hash.update(data.encode('utf-8'))

# Get the hexadecimal representation of the hash
hex_digest = sha256_hash.hexdigest()

print("SHA-256 Hash:", hex_digest)
