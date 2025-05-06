# anygraph
An interactive tool for tabular data exploration.

# Installation
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
6. Run the app
```
streamlit run app.py
```