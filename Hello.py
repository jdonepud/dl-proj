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

# Streamlit UI
st.title('Sentiment Analysis App')
st.write('Enter a comment to analyze its sentiment.')

user_input = st.text_area("Comment:", "Type your comment here...")
if st.button('Analyze'):
    if user_input:
        sentiment, confidence = analyze_sentiment([user_input])  # Ensure input is in a list
        st.write(f"Sentiment: {sentiment}, Confidence: {confidence:.2f}")
    else:
        st.write("Please enter a valid comment.")
