from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True, as_frame=True)
df = X.join(y)
df['target'] = df['target'].replace(0, 'setosa')
df['target'] = df['target'].replace(1, 'versicolour')
df['target'] = df['target'].replace(2, 'virginica')
df.to_csv('example_data.csv', index=False)