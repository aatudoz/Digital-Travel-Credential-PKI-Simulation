import json

with open("face_b64.txt", "r") as file:
	kuva_tekstina = file.read().strip()

dtc_passi = {
	"etunimi": "Testi",
	"sukunimi": "asd",
	"passinumero": "FI1111111",
	"syntymaaika": "1990-01-01",
	"kansalaisuus": "FI",
	"kasvokuva": kuva_tekstina,
}

#Tallennus
with open("dtc_data.json", "w") as f:
	json.dump(dtc_passi, f, indent=4)

print("onnistui!")
