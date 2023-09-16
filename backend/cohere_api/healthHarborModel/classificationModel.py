import cohere
from cohere.responses.classify import Example
from cohere.responses.classify import LabelPrediction
from cohere.responses.classify import Classification
import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import heapq


# print(topnames)
# print(top)

# lista =[]

# for j in response[0].labels:
#   lista.append(j)

# print(lista)

def _get_disease_with_medicine(description: str) -> list[dict[str, str]]:
  co = cohere.Client('dW7n7345zsD7VRvluLFqZbRZLtMZfdm3Zf7CS0DA')
  df = pd.read_csv("backend\cohere_api\healthHarborModel\datasets\drugs_side_effects_drugs_com.csv", usecols=['medical_condition', 'medical_condition_description', 'drug_name'])

  dfDrugs = df['drug_name']
  df.drop('drug_name', axis=1)
  dfCondCopy = df['medical_condition']
  DictDesToDrug = {}
  l = 0
  for inx, row in dfCondCopy.items():
    if row not in DictDesToDrug.keys():
      DictDesToDrug[row] = dfDrugs[l]
    l+=1

  # print(DictDesToDrug)

  examples =[]
  X = df[df.columns[:-1]].values
  y = df[df.columns[-1]].values

  over = RandomUnderSampler()
  X, y = over.fit_resample(X, y)
  data = np.hstack((X, np.reshape(y, (-1, 1))))
  transformed_df = pd.DataFrame(data, columns=df.columns)

  len(transformed_df)
  for index, row in transformed_df.iterrows():
      examples.append(Example(row["medical_condition_description"], row["medical_condition"]))

  inputs=[description]

  response = co.classify(
    inputs=inputs,
    examples=examples,
  )

  LabelsDict = {}
  numOfSuggestions = 3

  for i in range(len(response)):
      for j in response[i].labels:
        x = response[i].labels[j]
        LabelsDict[j] = x.confidence

  top = heapq.nlargest(numOfSuggestions, LabelsDict.values())
  topnames = []
  for j in range(numOfSuggestions):
    for i in LabelsDict.keys():
        if LabelsDict[i]==top[j]:
            Dctionr = {'rank': j, 'medicine': DictDesToDrug[i], 'disease': i, 'confindence': LabelsDict[i]}
            topnames.append(Dctionr)

  return topnames




if __name__ == '__main__':
   print(_get_disease_with_medicine("Big red spots on body"))
   print(_get_disease_with_medicine("Really stressed about exams. Want to Kill myself."))
   # "Big red spots on body", "Really stressed about exams. Want to Kill myself.", "pain in left arm"
