import json
f = open("roles.json", "r", encoding="utf8")
jsonOriginal = json.load(f)
f.close()
g = open("all.json", "r", encoding="utf8")
ptbrJson = json.load(g)
g.close()

rolesPtbr = {}
for roles in ptbrJson:
	rolesPtbr[roles["id"]] = roles
for roles in jsonOriginal:
	roles["name"] = rolesPtbr[roles["id"]+"_br"]["name"]
	roles["ability"] = rolesPtbr[roles["id"]+"_br"]["ability"]
	roles["reminders"] = rolesPtbr[roles["id"]+"_br"]["reminders"]
	if "firstNightReminder" in roles:
		roles["firstNightReminder"] = rolesPtbr[roles["id"]+"_br"]["firstNightReminder"]
	if "otherNightReminder" in roles:
		roles["otherNightReminder"] = rolesPtbr[roles["id"]+"_br"]["otherNightReminder"]
	if "flavor" in rolesPtbr[roles["id"]+"_br"]:
		roles["flavor"] = rolesPtbr[roles["id"]+"_br"]["flavor"]

h  = open("roles2.json", "w", encoding="utf8")
json.dump(jsonOriginal, h, indent=4)

