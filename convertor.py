import pandas as pd
from scipy.io import arff

# Load the ARFF file
data, meta = arff.loadarff('dataset.arff')

# Convert to a DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('dataset.csv', index=False)
