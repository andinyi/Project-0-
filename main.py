import convertJson

out = convertJson.jsonreturnDataframe("posts.json")
print(f"\033[92m {out}\033[00m")