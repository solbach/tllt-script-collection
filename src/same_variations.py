import pandas as pd
import re

#load data
file_name = "clusters.pkl"
panda_belly = pd.read_pickle(file_name)

#output some stats
print("Number of Clusters: {0}".format(len(panda_belly)))

result = []
for col in panda_belly:
    regex = re.compile(".*(same).*|.*(similar).*|.*(identical).*|.*(equal).*")

    filtered = set([m.group(0) for l in panda_belly[col] for m in [regex.search(l)] if m])
    result.append(filtered)

    print("Length: {0}\tData: {1}".format(len(filtered), filtered))


df = pd.DataFrame(result)
df.to_csv('list.csv', index=True)