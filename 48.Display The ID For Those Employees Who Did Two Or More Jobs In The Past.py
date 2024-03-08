import pandas as pd
employees = pd.read_csv(r"EMPLOYEES.csv")
result = job_history.groupby(['employee_id']) 
print(result.filter(lambda x: len(x) > 1).groupby('employee_id').size().sort_values(ascending=False))
