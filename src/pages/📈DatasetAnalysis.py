import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from matplotlib.font_manager import FontProperties

st.set_page_config(page_title="Datasets Analysis", page_icon="👋", layout="wide")


data100k = "datafiles/nep_spell_100k.csv"

# Preparing datafrmae
df = pd.read_csv(data100k)

# Count words
df["num_words"] = df["Correct"].apply(lambda x: len(x.split()))

# Count the number of sentences for each number of words
word_counts = df["num_words"].value_counts().sort_index()

# Create a Streamlit app
st.title("Dataset Analysis")

st.subheader("Word Count Analysis")
# Display the DataFrame (optional)
st.write(df)
st.write("---")
# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(word_counts.index, word_counts.values, color="skyblue")
plt.xlabel("Number of Words in Sentence")
plt.ylabel("Number of Sentences")
plt.title("Number of Words vs. Number of Sentences")
plt.grid(True)

# Set the range in the x-axis to 70
plt.xlim(0, 70)

# Save the plot as an image file (optional)
# plt.savefig("word_count_plot.png", dpi=300)

# Display the plot in Streamlit
st.pyplot(plt)

st.write("---")

#########################
# Concatenate all sentences into a single string
all_sentences = " ".join(df["Correct"])

# Tokenize the sentences and calculate word frequency
words = all_sentences.split()
word_freq = Counter(words)

# Consider the top 1000 most common words
top_words = word_freq.most_common(1000)
# Define the font file path
font1 = "fonts/TiroDevanagariHindi-Regular.ttf"
###################################
# Stop words
# Get the top 50 most frequent words
top_50_most_common = word_freq.most_common(25)

# Get the top 50 least frequent words
top_50_least_common = word_freq.most_common()[-25:]

# Extract words and their frequencies from the top 50 most frequent and least frequent lists
most_common_words, most_common_freqs = zip(*top_50_most_common)
least_common_words, least_common_freqs = zip(*top_50_least_common)


st.subheader("25 Most Frequent Words")
# Plot the histogram
plt.figure(figsize=(12, 6))
# Specify font properties
font_prop = FontProperties(fname=font1)
plt.barh(range(25), most_common_freqs, color="skyblue", label="Least Frequent")
plt.yticks(range(25), most_common_words, fontproperties=font_prop)
plt.gca().invert_yaxis()
plt.xlabel("Frequency")
plt.ylabel("Words")
plt.title("25 Most Frequent Words")
plt.legend()
plt.tight_layout()
st.pyplot(plt)

st.write("---")

st.subheader("25 Least Frequent Words")
# Plot the histogram
plt.figure(figsize=(12, 6))
# Specify font properties
font_prop = FontProperties(fname=font1)
plt.barh(range(25), least_common_freqs, color="salmon", label="Least Frequent")
plt.yticks(range(25), least_common_words, fontproperties=font_prop)
plt.gca().invert_yaxis()
plt.xlabel("Frequency")
plt.ylabel("Words")
plt.title("25 Least Frequent Words")
plt.legend()
plt.tight_layout()
st.pyplot(plt)
st.write("---")

# WORD CLOUD
# Generate the corpus for word cloud
corpus = {}
for word, frequency in top_words:
    corpus[word] = frequency


# Generate the word cloud
wordcloud_most_common = WordCloud(
    width=1000,
    height=500,
    background_color="white",
    min_font_size=10,
    regexp=r"[\u0900-\u097F]+",
    font_path=font1,
).generate_from_frequencies(corpus)


# Display the word cloud using Streamlit
st.subheader("Word Cloud of Most Frequent Words in Correct Sentences")
st.image(wordcloud_most_common.to_array(), use_column_width=True)
############################################
# WOrd cloud of least common
st.write("---")


# Concatenate all sentences into a single string

# Consider the least 1000 frequent words
least_common_words = word_freq.most_common()[: -1000 - 1 : -1]

# Generate the corpus for word cloud
corpus = {}
for word, frequency in least_common_words:
    corpus[word] = frequency

# Generate the word cloud for least frequent words
wordcloud_least_frequent = WordCloud(
    width=1000,
    height=500,
    background_color="white",
    min_font_size=10,
    regexp=r"[\u0900-\u097F]+",
    font_path=font1,
).generate_from_frequencies(corpus)

# Display the word cloud using Streamlit
st.header("Word Cloud of Least Frequent Words in Correct Sentences")
st.image(wordcloud_least_frequent.to_array(), use_column_width=True)


########################################
st.write("---")

# Data
char_seq_in = [
    "ि",
    "ी",
    "ु",
    "ू",
    "इ",
    "ई",
    "उ",
    "ऊ",
    "श",
    "श",
    "स",
    "स",
    "ष",
    "ष",
    "ब",
    "व",
    "त",
    "ट",
    "द",
    "ध",
    "ं",
    "ँ",
]
char_seq_out = [
    "ी",
    "ि",
    "ू",
    "ु",
    "ई",
    "इ",
    "ऊ",
    "उ",
    "स",
    "ष",
    "श",
    "ष",
    "श",
    "स",
    "व",
    "ब",
    "ट",
    "त",
    "ध",
    "द",
    "ँ",
    "ं",
]
datapoints_in_percentage = [
    5,
    5,
    5,
    5,
    2.5,
    2.5,
    2.5,
    2.5,
    1.5,
    0.5,
    1.5,
    0.5,
    0.5,
    0.5,
    1,
    1,
    1,
    0.6,
    0.5,
    0.5,
    1,
    1,
]

# Plot
plt.figure(figsize=(10, 6))
plt.bar(char_seq_in, datapoints_in_percentage, color="skyblue")
plt.xlabel("Character Sequence (Input)")
plt.ylabel("Percentage of Datapoints")
plt.title("Distribution of Character Substitution Errors")
# Specify font properties
font_prop = FontProperties(fname=font1)
plt.xticks(char_seq_in, char_seq_in, fontproperties=font_prop)

plt.grid(axis="y")

# Save the image
# plt.savefig("character_substitution.png", dpi=300, bbox_inches="tight")
# Show plot
plt.tight_layout()
# Display the plot in Streamlit
st.subheader("Character substitution error")
st.pyplot(plt)

##################################

st.write("---")

# Existing data
characters = [
    " ",
    "ा",
    "ि",
    "ी",
    "ु",
    "ू",
    "े",
    "ै",
    "ो",
    "ौ",
    "ृ",
    "्",
    "ः",
    "क",
    "ख",
    "ग",
    "घ",
    "ङ",
    "च",
    "छ",
    "ज",
    "झ",
    "ञ",
    "ट",
    "ठ",
    "ड",
    "ढ",
    "ण",
    "त",
    "थ",
    "द",
    "ध",
    "न",
    "प",
    "फ",
    "ब",
    "भ",
    "म",
    "य",
    "र",
    "ल",
    "व",
    "श",
    "स",
    "ष",
    "ह",
    "अ",
    "आ",
    "इ",
    "ई",
    "उ",
    "ऊ",
    "ऋ",
    "ए",
    "ऐ",
    "ओ",
    "औ",
]
datapoints_in_percentage = [
    1.5,
    1.5,
    1.5,
    1.5,
    1.5,
    1.5,
    1,
    1,
    1,
    1,
    1.2,
    1,
    0.5,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
]

# Additional data
additional_characters = ["क्ष", "त्र", "ज्ञ", "अं", "अः"]
additional_datapoints_in_percentage = [0.15, 0.15, 0.15, 0.15, 0.15]

# Combine the existing and additional data
characters += additional_characters
datapoints_in_percentage += additional_datapoints_in_percentage

# Plot
plt.figure(figsize=(12, 6))
plt.bar(characters, datapoints_in_percentage, color="skyblue")
plt.xlabel("Character")
plt.ylabel("Percentage of Datapoints")
plt.title("Distribution of Character Additions Errors")
plt.xticks(rotation=90)

# Specify font properties
font_prop = FontProperties(fname=font1)
plt.xticks(characters, characters, fontproperties=font_prop)

plt.grid(axis="y")

# Save the image
# plt.savefig("character_addition.png", dpi=300, bbox_inches="tight")

# Show plot
plt.tight_layout()
st.subheader("Character Addition Error")
st.pyplot(plt)
############################################################

st.write("---")

# Data
characters = [
    " ",
    "ा",
    "ि",
    "ी",
    "ु",
    "ू",
    "े",
    "ै",
    "ो",
    "ौ",
    "ृ",
    "्",
    "ः",
    "क",
    "ख",
    "ग",
    "घ",
    "ङ",
    "च",
    "छ",
    "ज",
    "झ",
    "ञ",
    "ट",
    "ठ",
    "ड",
    "ढ",
    "ण",
    "त",
    "थ",
    "द",
    "ध",
    "न",
    "प",
    "फ",
    "ब",
    "भ",
    "म",
    "य",
    "र",
    "ल",
    "व",
    "श",
    "स",
    "ष",
    "ह",
    "अ",
    "आ",
    "इ",
    "ई",
    "उ",
    "ऊ",
    "ऋ",
    "ए",
    "ऐ",
    "ओ",
    "औ",
    "क्ष",
    "त्र",
    "ज्ञ",
    "अं",
    "अः",
]
datapoints_in_percentage = [
    1.5,
    1.5,
    1.5,
    1.5,
    1.5,
    1.5,
    1,
    1,
    1,
    1,
    1,
    1.25,
    0.5,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.25,
    0.15,
    0.15,
    0.15,
    0.15,
    0.15,
]

# Plot
plt.figure(figsize=(10, 6))
plt.bar(characters, datapoints_in_percentage, color="skyblue")
plt.xlabel("Character")
plt.ylabel("Percentage of Datapoints")
plt.title("Distribution of Character Deletion Errors")
plt.xticks(rotation=90)

# Specify font properties
font_prop = FontProperties(fname=font1)
plt.xticks(characters, characters, fontproperties=font_prop)

plt.grid(axis="y")

# Save the image
# plt.savefig("character_deletion.png", dpi=300, bbox_inches="tight")

# Show plot
plt.tight_layout()

st.subheader("Character Deletion Error")
st.pyplot(plt)
############################################


st.write("---")

# Data
error_types = ["Deletion", "Addition", "Substitution", "Double Substitution"]
error_percentages = [28.5, 28.45, 40.1, 2.95]

# Create horizontal bar graph
plt.figure(figsize=(10, 6))
plt.barh(error_types, error_percentages, color="black")

# Add labels and title
plt.xlabel("Error Percentage")
plt.ylabel("Error Type")
plt.title("Error Types Distribution")

# Save the image
plt.savefig("error_type_distribution.png", dpi=300, bbox_inches="tight")

# Show plot
st.subheader("Distribution of Error Types")
st.pyplot(plt)
