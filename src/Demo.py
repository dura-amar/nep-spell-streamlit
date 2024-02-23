import streamlit as st
import pandas as pd

from ModelMethods import generate


st.set_page_config(page_title="DEMO", page_icon="👋", layout="wide")


# Make basic configuration for the app
appTitle = "Nepali Spell Correction"


# Some test examples here
example = (
    "अबको स्थायी कमिटी ओली सरकारलाई दीएको समर्थन फिर्ताको तयारि रहेको साहले जानकारी दिए।"
)
examples = {
    "Examples": "",
    "अखिलेस झा धेरै दिनदेखि अनुपस्थीत थिए ।": "अखिलेस झा धेरै दिनदेखि अनुपस्थीत थिए ।",
    "आठौँ तह उपनिर्देषक पदमा दुई जना उत्तीर्ण भएका छन्।": "आठौँ तह उपनिर्देषक पदमा दुई जना उत्तीर्ण भएका छन्।",
    "उनीहरूमा रोगसँग लड्ने क्षमता मज्जाले बिकसित भइसकेको हुँदैन।": "उनीहरूमा रोगसँग लड्ने क्षमता मज्जाले बिकसित भइसकेको हुँदैन।",
}


def main():

    st.header(appTitle)
    left_column, right_column = st.columns(2)
    correctedText= None

    with left_column:
        model_options = {"mT5", "mBART", "VartaT5"}

        # Display the radio options in a single line
        selected_model = st.radio("Select the model", model_options, index=0)

        # Create a dropdown menu
        selected_example_key = st.selectbox("Select an example", list(examples.keys()))
        # Display the selected example text in a text area
        selected_example_text = examples[selected_example_key]

        # Get user input
        user_input = st.text_area(
            "Enter a Nepali Sentence: ",
            selected_example_text,
            max_chars=512,  # Set the maximum input length to 512 characters
        )
        if st.button("Check Spelling"):
            if user_input:
                correctedText = generate(selected_model, user_input)
                # # Perfrom grammer correction
                # st.subheader("Corrected Text:")
                # st.write([f"{line['score']:.2f}: {line['sequence']}"for line in correctedText])
            else:
                st.warning("Please enter some text to check.")
    with right_column:
        if correctedText is not None:
            st.write("Corrected Text:")
            # st.write([f"{line['score']:.2f}: {line['sequence']}" for line in correctedText])
            df = pd.DataFrame(correctedText, columns=["score","sequence"])
            st.table(df)


if __name__ == "__main__":
    main()
