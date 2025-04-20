import openai
import streamlit as st
import pandas as pd

#this is a simple streamlit app that allows user to chat with a data analysis bot.
# The bot uses OpenAI's GPT-3.5-turbo model to answer questions about the data.
# The app uses streamlit to create a web interface for the bot.
# The app allows user to upload a CSV file and then ask questions about the data.
# The app uses pandas to read the CSV file and convert it to a dataframe.
# The app uses openai to send the user's question to the GPT-3.5-turbo model and get the answer.
# The app uses streamlit to display the answer to the user.
# The app uses streamlit to display the dataframe and the answer to the user.

#openai.api_key = st.secrets["openai_api_key"]
openai.api_key = "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" #replace with your own API key

global df,question
def get_answer(question, df):
    # Convert the dataframe to a string
    df_str = df.to_csv(index=False)
    
    # Create the prompt for the model
    prompt = f"Answer the following question about the data:\n\n{question}\n\nData:\n{df_str}"
    
    # Call the OpenAI API to get the answer
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Extract the answer from the response
    answer = response['choices'][0]['message']['content']
    
    return answer

def chatwithgpt():
    st.write("# Chat with Data Analysis Bot")
    st.markdown("## Upload your CSV file")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("## Data Preview")
        st.dataframe(df.head())

        # Display the columns of the dataframe
        st.write("## Data Columns")
        st.write(df.columns.tolist())

        # Ask user for a question about the data
        question = st.text_input("Ask a question about the data:")
        
        if st.button("Get Answer"):
            if question:
                with st.spinner("Getting answer..."):
                    answer = get_answer(question, df)
                    st.write("## Answer")
                    st.write(answer)
            else:
                st.warning("Please enter a question.")
    

if __name__ == "__main__":
    st.set_page_config(page_title="Data Analysis App", layout="wide")
    st.title("Data Analysis App")
    st.sidebar.title("Data Analysis App")
    chatwithgpt()








# This is a simple streamlit app that allows user to chat with a data analysis bot.