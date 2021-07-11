# web connection
import urllib.request as request
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    # data = response.read().decode("utf-8")  # 用utf-8解構中文網頁
    data = json.load(response)  # 用json模組解構JSON格式

clist = data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
