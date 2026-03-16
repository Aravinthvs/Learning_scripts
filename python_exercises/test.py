data = [

  {"id": 1, "status": "SUCCESS", "duration": 12},

  {"id": 2, "status": "FAILURE", "duration": 4},

  {"id": 3, "status": "SUCCESS", "duration": 6}

]

data1 = '[{"id":1,"status":"SUCCESS"},{"id":2,"status":"FAILURE"}]'
print(type(data1))
import pandas as pd

df = pd.DataFrame(data)

res = df["duration"].sort_values()

print(res)

