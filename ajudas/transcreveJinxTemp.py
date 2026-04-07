import json

def pegaId(data):
	return data["id"]
f = open("jinxes.json", "r", encoding="utf8")
jsonOriginal = json.load(f)
f.close()
g = open("all.json", "r", encoding="utf8")
ptbrJson = json.load(g)
g.close()

finalJson = []
for roles in ptbrJson:
	if "jinxes" in roles:
		finalJson.append({"id": roles["id"][:-3], "jinx": []})
		for j in roles["jinxes"]:
			finalJson[-1]["jinx"].append({"id": j["id"][:-3], "reason": j["reason"]})

finalJson.sort(key=pegaId)
h  = open("jinxes2.json", "w", encoding="utf8")
json.dump(finalJson, h, indent=2)


