import yaml

# with open("./value.yml", "r", encoding="utf-8") as f:
#     data = yaml.safe_load(f)
#     print("data:{}".format(data))
#     print("类型{}".format(type(data)))
data = {'t1':{'t2': {'t3': [123]}}}
with open("./ww.yml","a",encoding="utf-8") as f:
    yaml.safe_dump(data,f,encoding="utf-8",allow_unicode=True)
