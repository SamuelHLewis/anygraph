import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine, load_iris

# make sure to keep this as the first call, otherwise the plot will be tiny
st.set_page_config(layout='wide')

# this will be used to infer the correct chart type
continuous_types = ['int32', 'int64', 'float32', 'float64']

# define the available criteria as a session state
# this prevents new criteria from overwriting existing ones
if 'criteria_options' not in st.session_state:
    st.session_state.criteria_options = []

# define the total number of criteria as a session state
# this allows criteria levels to be labelled with unique and meaningful keys
if 'total_criteria_levels' not in st.session_state:
    st.session_state.total_criteria_levels = 1

# we want the plot (middle column) to be thrice as large as the menus
# we deliberately place the menus outside of the sidebar to separate tabs from page-specific elements
col1, col2 = st.columns([1,2])

# lefthand column holds the plotting options
with col1:
    dataset = st.selectbox(
        'Dataset',
        ['Wine', 'Iris']
    )
    if dataset=='Wine':
        X, y = load_wine(return_X_y=True, as_frame=True)
    elif dataset=='Iris':
        X, y = load_iris(return_X_y=True, as_frame=True)
    input_df = X.join(y)
    input_df['target'] = input_df['target'].astype(str)
    x_var = st.selectbox(
        "X Axis",
        input_df.columns,
        index=None,
        placeholder="Select a variable",
        key='x_selector'
    )
    y_var = st.selectbox(
        "Y Axis",
        input_df.columns,
        index=None,
        placeholder="Select a variable",
        key='y_selector'
    )
    # this section creates a third box to customise the plot in a plot-type-specific manner
    if x_var == None and y_var == None:
        pass
    # for scatterplots, offer a colour selector
    elif x_var and y_var and input_df[x_var].dtype in continuous_types and input_df[y_var].dtype in continuous_types:
        colour_var = st.selectbox(
            "Point Colour",
            input_df.columns.drop([x_var, y_var]),
            index=None,
            placeholder="Select a variable",
            key='colour_selector'
        )
    # for histograms, offer a granularity (i.e. total bins) slider
    elif x_var == None or y_var == None:
        total_bins = st.slider(
            "Granularity",
            min_value=2,
            max_value=int(len(input_df)),
            value=int(len(input_df)/5)
        )
    # for continuous vs categorical, offer a radio button to toggle between boxplot and violinplot
    elif x_var and y_var and (
        (input_df[x_var].dtype in continuous_types and input_df[y_var].dtype not in continuous_types) or
        (input_df[x_var].dtype not in continuous_types and input_df[y_var].dtype in continuous_types)):
        cont_vs_cat_plot_type = st.radio(
            "Plot type",
            ["Box-Whisker Graph", "Violin Graph"]
        )

# righthand column holds the graph itself
with col2:
    fig, ax = plt.subplots()
    if x_var == None and y_var == None:
        st.write("Select which variables you would like to visualise using the dropdowns on the left")
    elif y_var == None:
        ax = sns.histplot(data=input_df, x=x_var, bins=total_bins)
    elif x_var == None:
        ax = sns.histplot(data=input_df, y=y_var, bins=total_bins)
    else:
        x_type = input_df[x_var].dtype
        y_type = input_df[y_var].dtype
        if x_type in continuous_types and y_type in continuous_types:
            ax = sns.scatterplot(data=input_df, x=x_var, y=y_var, hue=colour_var)
        elif (x_type in continuous_types and y_type not in continuous_types) or (
            x_type not in continuous_types and y_type in continuous_types):
            if cont_vs_cat_plot_type == "Box-Whisker Graph":
                ax = sns.boxplot(data=input_df, x=x_var, y=y_var)
            elif cont_vs_cat_plot_type == "Violin Graph":
                ax = sns.violinplot(data=input_df, x=x_var, y=y_var)
        elif x_type not in continuous_types and y_type not in continuous_types:
            total_counts = input_df[[x_var, y_var]].value_counts().reset_index()
            total_counts_matrix = total_counts.pivot(index=x_var, columns=y_var, values="count")
            ax = sns.heatmap(total_counts_matrix)
    st.pyplot(fig)