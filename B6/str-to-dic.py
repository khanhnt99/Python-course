import json
D = {'name': 'Khanh', 'age': 20, 'girlfriend': ['khong', 'co']}
s = json.dumps(D)
print(type(s), s)
