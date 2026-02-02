
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import sys

cert_filename = "ds_cert.pem"
#Julkinen sertifikaatti
print(f"Ladataan sertifikaattia: {cert_filename}")
try:
	with open(cert_filename, "rb") as f:
		cert_data = f.read()
		cert = x509.load_pem_x509_certificate(cert_data, default_backend())
		public_key = cert.public_key()
except FileNotFoundError:
	print("Virhe: Sertifikaattia ei löydy")
	sys.exit(1)

#Ladataan passi ja allekirjoitus
try:
	with open("dtc_data.json", "rb") as f:
		data = f.read()
	with open("dtc_signature.bin", "rb") as f:
		signature = f.read()
except FileNotFoundError:
	print("Virhe: Passia tai allekirjoitusta ei löydy!")
	sys.exit(1)

print("Tarkistetaan allekirjoitus")
try:
	public_key.verify(
		signature,
		data,
		ec.ECDSA(hashes.SHA256())
	)
	print("\n----------")
	print("SUCCESS")
	print("---------")
	print("Matkustaja: (lisaa)")
	print("Tila hyväksytty")

except Exception as e:
	print("\n---------")
	print("Failed")
