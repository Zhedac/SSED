import json


 f = open("eso_names.txt", "w")
    f1 = open("esoJson.txt", 'r')
    data = json.loads(f1)
    f.write(json.dumps(data, indent=1))
    f.close()
