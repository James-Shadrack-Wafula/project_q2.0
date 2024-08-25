# import streamlit as st
# from streamlit_extras.add_vertical_space import add_vertical_space
# import sqlite3
# from hashlib import sha256
# import os

# import google.generativeai as palm
# palm.configure(api_key="AIzaSyBHINqTvLyNBmt3VCSBHYaqxsxfBjBlHDk")

# # Initialize the SQLite database
# conn = sqlite3.connect('user_data.db')
# c = conn.cursor()

# # Create users table
# c.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         username TEXT PRIMARY KEY,
#         password TEXT
#     )
# ''')

# # Create queries table
# c.execute('''
#     CREATE TABLE IF NOT EXISTS queries (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT,
#         query TEXT,
#         response TEXT,
#         FOREIGN KEY (username) REFERENCES users (username)
#     )
# ''')

# conn.commit()

# def hash_password(password):
#     return sha256(password.encode()).hexdigest()

# # Palm2 API key
# palm2_api_key = os.getenv('PALM2_API_KEY', '')

# def palm_(prompt):
#     model_id = "models/text-bison-001"
#     try:
#         completion = palm.generate_text(
#             model=model_id,
#             prompt=prompt,
#             temperature=0.99,
#             max_output_tokens=800,
#         )
#         return completion.result
#     except Exception as e:
#         return f"An error occurred: {str(e)}"

# # Authentication function
# def login(username, password):
#     c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hash_password(password)))
#     return c.fetchone()

# def register(username, password):
#     try:
#         c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
#         conn.commit()
#         return True
#     except sqlite3.IntegrityError:
#         return False

# def save_query(username, query, response):
#     c.execute("INSERT INTO queries (username, query, response) VALUES (?, ?, ?)", (username, query, response))
#     conn.commit()

# # App title and sidebar
# st.set_page_config(page_title="Q 2.0", page_icon="🤖")

# with st.sidebar:
#     st.title("Jimmy's AI Assistant\n🤖💬 Q 2.0")
#     st.markdown("""
#     ## About
#     Hello meet Q, my AI Powered Personal Assistant. \n 
#     Have a question? Ask Q. \n
#     Contact me on:
#     - [WhatsApp](https://wa.me/254746727592/)
#     - [email](mailto:jamesshadrack23@gmail.com)
#     - [GitHub](https://github.com/James-Shadrack-Wafula/)
#     """)
#     st.write("Developed by [Jimmy](http://james-shadrack-wafula.rf.gd/)")

# # Login/Register
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# if not st.session_state.logged_in:
#     st.header("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     if st.button("Login"):
#         user = login(username, password)
#         if user:
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("Logged in successfully!")
#         else:
#             st.error("Invalid username or password")
#     if st.button("Register"):
#         if register(username, password):
#             st.success("Registered successfully! Please log in.")
#         else:
#             st.error("Username already exists.")
# else:
#     st.header(f"Welcome, {st.session_state.username}")

#     # Store generated responses
#     if "messages" not in st.session_state:
#         st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

#     # Display or clear chat messages
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.write(message["content"])

#     def clear_chat_history():
#         st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
#     st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

#     # Function for generating Palm2 response
#     def generate_palm2_response(prompt_input):
#         response = palm_(prompt_input)
#         save_query(st.session_state.username, prompt_input, response)
#         return response

#     # User-provided prompt
#     if prompt := st.chat_input():
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.write(prompt)

#     # Generate a new response if the last message is not from the assistant
#     if st.session_state.messages[-1]["role"] != "assistant":
#         with st.chat_message("assistant"):
#             with st.spinner("Thinking..."):
#                 response = generate_palm2_response(prompt)
#                 st.write(response)
#         message = {"role": "assistant", "content": response}
#         st.session_state.messages.append(message)


## Version 2.0
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import replicate
import os


import os
import streamlit as st
import requests

import google.generativeai as palm
palm.configure(api_key="AIzaSyBHINqTvLyNBmt3VCSBHYaqxsxfBjBlHDk")

# palm.configure(api_key=API_KEY)


    
# App title
st.set_page_config(
    page_title="Q 2.0",  # Change the title displayed on the browser tab
    page_icon="🤖")

# Palm2 Credentials
palm2_api_key = os.getenv('PALM2_API_KEY', '')

def palm_(prompt='''write a cover letter for a data science job applicaton. 
    Summarize it to two paragraphs of 50 words each. '''):
    model_id="models/text-bison-001"
    # prompt='''write a cover letter for a data science job applicaton. 
    # Summarize it to two paragraphs of 50 words each. '''
    try:  
        completion=palm.generate_text(
            model=model_id,
            prompt=prompt,
            temperature=0.99,
            max_output_tokens=800,
        )
        # print(completion.result)
        return completion.result
    except:
        return "An error occured"

    

with st.sidebar:
    # st.title('')
    st.title("Jimmy's AI Assistant\n🤖💬 Q 2.0")
    # st.title("Ai Powered Revision Assistant")
    st.markdown(
        """
    ## About
    Hello meet Q, my AI Powerd Personal Assistant \n 
    Have a question? Ask Q. \n
    Contact me on:
    - [WhatsApp](https://wa.me/254746727592/)
    - [email](mailto:jamesshadrack23@gmail.com) 
    - [GitHub](https://github.com/James-Shadrack-Wafula/)

 
    """
    )
    # add_vertical_space(5)
    st.write("Developed by [Jimmy](http://james-shadrack-wafula.rf.gd/)")
    # palm2_api_key = st.text_input('Enter Palm2 API key:', type='password', value=palm2_api_key)
    # os.environ['PALM2_API_KEY'] = palm2_api_key

    # st.subheader('Models and parameters')
    # selected_model = st.sidebar.selectbox('Choose a Palm2 model', ['davinci', 'davinci-codex'], key='selected_model')
    # if selected_model == 'davinci':
    #     model = 'text-davinci-002'
    # elif selected_model == 'davinci-codex':
    #     model = 'text-davinci-codex-002'
    # temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    # top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    # max_tokens = st.sidebar.slider('max_tokens', min_value=16, max_value=2048, value=120, step=8)
    # st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')

# Store generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating Palm2 response
def generate_palm2_response(prompt_input):
    conversation_history = ""
    # for dict_message in st.session_state.messages:
    #     if dict_message["role"] == "user":
    #         conversation_history += "User: " + dict_message["content"] + "\n"
    #     else:
    #         conversation_history += "Assistant: " + dict_message["content"] + "\n"
    # payload = {
    #     "model": model,
    #     "prompt": f"{conversation_history}User: {prompt_input}\nAssistant:",
    #     "temperature": temperature,
    #     "max_tokens": max_tokens,
    #     "top_p": top_p
    # }
    # headers = {
    #     "Content-Type": "application/json",
    #     "Authorization": f"Bearer {palm2_api_key}"
    # }
    response = palm_(prompt_input)
    return response
    # response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", json=payload, headers=headers)
    # return response.json()["choices"][0]["text"].strip()

# User-provided prompt

if prompt := st.chat_input( palm2_api_key):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if the last message is not from the assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_palm2_response(prompt)
            st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

