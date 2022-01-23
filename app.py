from typing import Union, Any

import pandas as pd
import plotly.express as px
import streamlit as st
from plotly.graph_objs import Figure


@st.cache
def get_data():
    return pd.read_csv(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vRV48XxyP4ipyXu79PV_XpmshMSXPCBWAq9yX_hewG-BRb14Tesu4nylUCUEYLlyDeLOUsZpA228m6T/pub?gid=298041788&single=true&output=csv")


df = get_data()

st.title("🐶Dog Breed Explorer🐶")
st.markdown(
    "Welcome to Dog Breed Explorer! Scroll down to the charts to explore some characteristics of 122 dog breeds \n "
    "by their [Continental Kennel Club (CKC)](https://ckcusa.com/) group and subgroup. \n"
    "Please adopt a dog from your local shelter if possible. Find one [here]("
    "https://www.petfinder.com/animal-shelters-and-rescues/search/). If you must buy a puppy, please research the "
    "breeders "
    "you're interested \n "
    "in and avoid pet stores.")

st.markdown("> The better I get to know men, the more I find myself loving dogs. \n\n—Charles De Gaulle")
st.subheader(
    'For all you spreadsheet aficionados, here\'s a glance at the data I\'ve visualized in the interactive charts below.')
st.markdown('The first ten records of the dog breeds dataset. Click on a column name to sort. Click the two arrows to '
            'the outside and upper right of the table to view all columns.')
st.dataframe(df.head(10))


def convert_df(df):
    return df.to_csv().encode('utf-8')


csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='dog_breeds.csv',
    mime='text/csv',
)

st.subheader("Average Heights and Weights of Dogs by Breed")
st.markdown('In the scatterplot below, hover over any point for the breed name, average height, and average '
            'weight.')
fig_a: Union[Figure, Any] = px.scatter(df,x="avg_height",y="avg_weight", color="avg_weight",
                 template="plotly_dark", hover_name='breed',hover_data=['avg_height','avg_weight'])
fig_a.update_layout({'xaxis':{'title': {'text': 'average height (in)'}}, 'yaxis':{'title': {'text': 'average weight (lbs)'}}})
st.write(fig_a)

st.subheader("Average Lifespan of Each CKC Breed Group")
st.markdown("Hover over bars for more details. See interactivity options in the upper right side of the chart.")
span = df.groupby("breed_group_CKC").average_lifespan.median().sort_values(axis=0, ascending = True).reset_index()
fig_1 = px.bar(span, x="breed_group_CKC", y="average_lifespan", color="breed_group_CKC", template="plotly_dark")
fig_1.update_traces(hovertemplate='CKC Breed Group <br>Average Life Expectancy: %{y}')
fig_1.update_layout(showlegend = False)
fig_1.update_yaxes(title_text='average lifespan (years)')
fig_1.update_xaxes(title_text='CKC breed group')
st.write(fig_1)

st.subheader("Dog Breeds by Size, CKC Breed Group, and CKC Breed Subgroup")
st.markdown(
    'Click on the two arrows in the upper right corner of the chart to enlarge. Click the innermost circle to reset '
    'the sunburst chart.')
small = df[df["avg_weight"] < 25]
fig_2 = px.sunburst(small, path=['breed_group_CKC', 'breed_ckc_subgroup', 'breed'], values='avg_weight',
                    color='breed_group_CKC', title="Small Dog Breeds (under 25 lbs.)", template="plotly_dark")
st.write(fig_2)

medium = df.loc[(df["avg_weight"] >= 25) & (df["avg_weight"] < 50)]
fig_3 = px.sunburst(medium, path=['breed_group_CKC', 'breed_ckc_subgroup', 'breed'], values='avg_weight',
                    color='breed_group_CKC',
                    title="Medium Dog Breeds (25 to 50 lbs.)", template="plotly_dark")
st.write(fig_3)

large = df.loc[(df["avg_weight"] >= 50) & (df["avg_weight"] < 90)]
xl = df.loc[(df["avg_weight"] >= 90)]

fig_4 = px.sunburst(large, path=['breed_group_CKC', 'breed_ckc_subgroup', 'breed'], values='avg_weight',
                    color='breed_group_CKC',
                    title="Large Dog Breeds (51 to 89 lbs.)", template="plotly_dark")
st.write(fig_4)

fig_5 = px.sunburst(xl, path=['breed_group_CKC', 'breed_ckc_subgroup', 'breed'], values='avg_weight',
                    color='breed_group_CKC',
                    title="Extra Large Dog Breeds (90 lbs.+", template="plotly_dark")
st.write(fig_5)

st.markdown("### Yay! You explored some data today!")
st.write("You know you want to click that button 👇🏼")
btn = st.button("Celebrate!")
if btn:
    st.balloons()

