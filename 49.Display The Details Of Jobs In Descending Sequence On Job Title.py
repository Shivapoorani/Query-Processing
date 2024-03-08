import pandas as pd
employees = pd.read_csv(r"EMPLOYEES.csv")
print("job_id      Job ID                                min_salary  max_salary")
result = jobs.sort_values('job_title')
for index, row in result.iterrows():
    print(row['job_id'].ljust(15),row['job_title'].ljust(35),str(row['min_salary']).ljust(9),row['max_salary'])
