import pandas as pd

# part a
df = pd.read_csv("volunteer.csv")

# part b
df_new = df.rename(columns={"Phone 1": "Daytime Phone", "Phone 2": "Evening Phone"})

# part c 
df_new[['First Name', 'Last Name', 'Daytime Phone']].head(20)

# part d
zip_counts = df_new.groupby(["Zip5"])['Zip5'].count()

# part e
zip_counts.to_csv("zip5_counts.csv")
