# sorted mette in ordine, reverse=True per il decrescente,
# lambda prende ogni voce del dizionario
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
	return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
	return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
	return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
	if not mages:
		return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
	powers = list(map(lambda x: x['power'], mages))
	max_p = max(powers)
	min_p = min(powers)
	avg_p = round(sum(powers) / len(powers), 2)
	return {'max_power': max_p, 'min_power': min_p, 'avg_power': avg_p}


def main():
	artifacts = [
		{'Name': "FireStaff", 'power': 90, 'type': "Fire"},
		{'Name': "WaterStaff", 'power': 75, 'type': "Water"},
		{'Name': "CaosWand", 'power': 170, 'type': "Caos"},
		{'Name': "EarthWand", 'power': 120, 'type': "Earth"}
	]
	print("Trying artifact sorter...")
	print("=" * 40)
	for art in artifacts:
		print(art)
	artifacts = artifact_sorter(artifacts)
	print("------")
	for art in artifacts:
		print(art)
	print("=" * 40)
	mages = [
		{'Name': "Franko", 'power': 90, 'element': "Fire"},
		{'Name': "Lino", 'power': 178, 'element':"Water"},
		{'Name': "Bob", 'power': 145, 'element': "Caos"},
		{'Name': "Fred", 'power': 45, 'element': "Earth"}
	]
	print("\nTrying power filter...")
	print("=" * 40)
	for m in mages:
		print(m)
	mages = power_filter(mages, 100)
	print("------")
	for m in mages:
		print(m)
	print("=" * 40)
	print("\nTrying spell transformer...")
	print("=" * 40)
	spells = ["Fireball", "Excalibur", "Lighting Bolt"]
	for s in spells:
		print(s)
	spells = spell_transformer(spells)
	print("------")
	for s in spells:
		print(s)
	print("=" * 40)
	print("\nTrying mage stats...")
	print("=" * 40)
	stats = mage_stats(mages)
	for st in stats.items():
		print(st)
	print("=" * 40)



if __name__ == "__main__":
	main()