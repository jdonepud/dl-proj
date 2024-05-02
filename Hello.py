# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    # Process the input text through the sentiment analysis pipeline
    result = sentiment_pipeline(text)
    return result[0]['label'], result[0]['score']  # Return both label and confidence score

st.markdown("""
<style>
.main {
    background-color: #f1f2f6;
}
.stTextInput>label {
    color: #4b4b4b;
}
.stButton>button {
    color: #ffffff;
    background-color: #ff6347;
    border-radius: 10px;
    border: none;
    padding: 10px 24px;
    font-size: 16px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Set up the title and intro text
st.title('Sentiment Analysis App')
st.markdown("""
This app analyzes the sentiment of the text you provide. 
            Type a comment and hit the 'Analyze' button to see the sentiment and confidence level of the analysis.
""")

# Text input for user
user_input = st.text_area("Enter your comment:", value="", placeholder="Type your comment here...", height=150)

if st.button('Analyze'):
    if user_input:
        sentiment, confidence = analyze_sentiment([user_input])
        st.success(f"Sentiment: **{sentiment}**")
        st.info(f"Confidence: **{confidence:.2f}**")

        st.bar_chart([confidence, 1-confidence])

        html_str = f"""
        <div style="font-size:24px; font-weight:bold; color:{'green' if sentiment == 'POSITIVE' else 'red'};">
            {sentiment}
        </div>
        """
        st.markdown(html_str, unsafe_allow_html=True)
    else:
        st.error("Please enter a valid comment.")
else:
    st.write("Results will appear here after you submit your comment.")
