import json
c = []
for i in range (0,10000):
    c.append(i)
data = {'presion':c,
        'valor':c,
        'flujo':c
        }
print(len(data['presion']))
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)