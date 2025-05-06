# anygraph
An interactive tool for tabular data exploration.

## Installation
These instructions assume that you have python and git already installed on your computer.
1. Clone the repo and move into the dir
```
git clone https://github.com/SamuelHLewis/anygraph
cd anygraph
```
2. Create a new python environment using `venv`
```
python -m venv venv
```
3. Activate the new python environment
```
source venv/bin/activate
```
4. Update pip
```
python -m pip install --upgrade pip
```
5. Install the modules for the app
```
python -m pip install -r requirements.txt
```

## Usage

To launch the app, make sure you have the python environment created above loaded, and then run the following in your terminal:
```
streamlit run app.py
```

This allows you to load any CSV file. If you would like to create an example CSV file for debugging or demonstration purposes, run the following:
```
python scripts/create_example_data.py
```
This will write the file `example_data.csv` to the `data` dir. This file is [the iris dataset](https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html) from sklearn.