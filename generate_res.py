import pickle

with open('res.pkl', 'rb') as inp:
    d = pickle.load(inp)
print(f"Seach for keyword '{d['keyword']}'")
print("====================================")
for key in d:
    if isinstance(key, tuple):
        print(key)
        count = 1
        for text in d[key]:
            print(f"({count}) {text}")
            count += 1
        print("====================================")
