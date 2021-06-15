import json
dict={'9':10,'11':12,'4':5,'6':7}
print("original dict")
print(dict)
print("json data")
print(json.dumps(dict,sort_keys=True,indent=4))
