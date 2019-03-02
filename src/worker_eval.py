import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

csv_file = "../data/Batch_3548952_batch_results_pilot_b.csv"
#csv_file = "../data/test.csv"

cl_worker_id = "WorkerId"
cl_hit_id = "HITId"
cl_ans_nsim = "Answer.nosim"
cl_ans_sim = "Answer.other_feedback"

dt = pd.read_csv(csv_file)
numb_jobs = dt.shape[0]
workers = dt[cl_worker_id].drop_duplicates(keep="first")

df_eval = pd.DataFrame(columns=[cl_worker_id,'nosimR', 'simR'])
for w in workers:
    df = dt.loc[(dt[cl_worker_id] == w) & (dt[cl_ans_nsim] == "nosim")]
    sim = dt.loc[(dt[cl_worker_id] == w)].shape[0] - df.shape[0]
    print("Worker: {0}, No-Sim: {1}, Ratio: {2}".format(w, df.shape[0], df.shape[0]/numb_jobs))
    d_temp = {cl_worker_id: w, 'nosimR': df.shape[0]/numb_jobs, 'simR': sim/numb_jobs}
    df_eval = df_eval.append(d_temp, ignore_index=True)

df_eval = df_eval.sort_values(by=["nosimR"])
print(df_eval)

df_eval.to_csv("../data/output.csv")

df_eval = df_eval.cumsum()
plt.figure
df_eval.plot(x=cl_worker_id, y=["nosimR", "simR"], kind="bar")
plt.show()