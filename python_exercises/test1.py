import pandas as pd

data = {"maths":100, "science":90, "social":80, "english":90}

res = pd.DataFrame(list(data.items()), columns = ["subject","marks"])
new_res = res.drop_duplicates("marks")
print(new_res)