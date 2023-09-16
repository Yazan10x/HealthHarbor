import cohere
from cohere.responses.classify import Example

import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler
co = cohere.Client('dW7n7345zsD7VRvluLFqZbRZLtMZfdm3Zf7CS0DA')

# we want to first oversample our dataframe model, then randomly sample 2500 rows to obtain our feature data.

df = pd.read_csv("Cohere\datasets\drugs_side_effects_drugs_com.csv", usecols=['medical_condition', 'medical_condition_description'], nrows=500)

# df.drop(df[df["drug_name"]=="Accutane"].index)

examples =[]
# print(df.head())

X = df[df.columns[:-1]].values
y = df[df.columns[-1]].values

over = RandomOverSampler()
X, y = over.fit_resample(X, y)
data = np.hstack((X, np.reshape(y, (-1, 1))))
transformed_df = pd.DataFrame(data, columns=df.columns)

len(transformed_df)

for index, row in transformed_df.iterrows():
    examples.append(Example(row["medical_condition_description"], row["medical_condition"]))

inputs=[
  "Big red spots on body", "Really stressed about exams. Want to Kill myself."#, "Hand is spazzing out"
]

# print(examples)

response = co.classify(
  inputs=inputs,
  examples=examples,
)
print(response)