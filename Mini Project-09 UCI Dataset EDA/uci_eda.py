import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(csv_url):
    print('Loading dataset...')
    # df = pd.read_csv(csv_url)
    print('EDA steps: df.head(), df.describe(), df.info()')
    print('Visualizing distributions...')
    # sns.pairplot(df)
    # plt.show()

if __name__ == '__main__':
    # Use Iris dataset as an example
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    perform_eda(url)