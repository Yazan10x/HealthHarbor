import cohere
from cohere.responses.classify import Example
from cohere.responses.classify import LabelPrediction
# from cohere.responses.classify import Classification



import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import heapq
co = cohere.Client('dW7n7345zsD7VRvluLFqZbRZLtMZfdm3Zf7CS0DA')

# we want to first oversample our dataframe model, then randomly sample 2500 rows to obtain our feature data.

df = pd.read_csv("Cohere\datasets\drugs_side_effects_drugs_com.csv", usecols=['medical_condition', 'medical_condition_description'])

# df.drop(df[df["drug_name"]=="Accutane"].index)

examples =[]
# print(df.head())

X = df[df.columns[:-1]].values
y = df[df.columns[-1]].values

over = RandomUnderSampler()
X, y = over.fit_resample(X, y)
data = np.hstack((X, np.reshape(y, (-1, 1))))
transformed_df = pd.DataFrame(data, columns=df.columns)

len(transformed_df)

for index, row in transformed_df.iterrows():
    examples.append(Example(row["medical_condition_description"], row["medical_condition"]))

inputs=[
  "Big red spots on body"#, "Really stressed about exams. Want to Kill myself.", "pain in left arm"
]

# print(examples)

response = co.classify(
  inputs=inputs,
  examples=examples,
)
print(response, "\n\n")

lol = response[0].labels.items

for i in response:
    print(1)

LabelPrediction

LabelsDict = {}

for i in range(len(response)):
    for j in response[i].labels:
      x = response[i].labels[j]
      LabelsDict[j] = x.confidence

top = heapq.nlargest(3, LabelsDict.values())
topnames = []
for i in LabelsDict.keys():
    if LabelsDict[i] in top:
        topnames.append((i, LabelsDict[i]))

print(topnames)
print(top)

#print(responseww)
#print(response)