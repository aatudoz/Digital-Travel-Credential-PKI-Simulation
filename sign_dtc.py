import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

with open("ds_private.pem", "rb") as key_file:
	private_key = serialization.load_pem_private_key(
		key_file.read(),
		password=None
	)

with open("dtc_data.json", "rb") as f:
	data = f.read()

signature = private_key.sign(
	data,
	ec.ECDSA(hashes.SHA256())
	)

with open("dtc_signature.bin", "wb") as f:
	f.write(signature)

print("Allekirjoitus valmis! Tiedostoon: dtc_signature.bin")
