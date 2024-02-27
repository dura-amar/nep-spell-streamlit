import streamlit as st
import pandas as pd

st.set_page_config(page_title="Datasets Preparation", page_icon="👋", layout="wide")

##########################################

# Read lines from the text file
with open("../datafiles/sample_nep_corpus.txt") as file:
    items = file.readlines()

# Split each line into separate columns
datacorpus = pd.DataFrame(items, columns=["Content"])
# datacorpus.columns =["Content"]


# st.write(f"{datacorpus}")

datasentences = pd.read_csv("../datafiles/sample_nep_sentences.csv")

data100k = pd.read_csv(
    r"../datafiles/sample_nep_spell_100k.csv",
    nrows=50,
)


###########################################


st.title("Dataset Preparation")

st.write("---")
st.header(
    """
A Large Nepali Text Corpus 
"""
)

st.caption("**Table 1.** A Large Nepali Text Corpus")

st.dataframe(datacorpus, use_container_width=True)

st.write("---")
st.header(
    """
Sentence extrancted from A Large Nepali Text Corpus
"""
)
st.caption("**Table 2.** Extracted sentences")
st.dataframe(datasentences, use_container_width=True)

st.write("---")
st.header(
    """
Parallel dataset using extracted sentences
"""
)
st.caption("**Table 3.** 100k Dataset used for training")
st.dataframe(data100k, use_container_width=True)
