
#################################
#    V.2.1                      #
#################################
# import google.generativeai as genai
# import PIL.Image
# import os
# import streamlit as st
# import os
# import google.generativeai as palm
# import replicate
# import requests
# from streamlit_extras.add_vertical_space import add_vertical_space
# import base64
# from PIL import Image
# from io import BytesIO
# # Configure Palm API key
# palm.configure(api_key="AIzaSyCGh4TndS8s5LMHzDYRTsS5kwYg4WxTwYo")

# # Configure Gemini API
# my_api = "AIzaSyAFq84DG1AVgjRdbsmWHZ2mCg4SYVdnXg4"
# api_key = os.environ.get("AIzaSyAFq84DG1AVgjRdbsmWHZ2mCg4SYVdnXg4")
# genai.configure(api_key=my_api)
# # genai.configure(api_key=os.environ["AIzaSyAFq84DG1AVgjRdbsmWHZ2mCg4SYVdnXg4"])
# # model = genai.GenerativeModel(model_name="gemini-pro-vision")
# model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# # App title
# st.set_page_config(
#     page_title="Q 2.0",
#     page_icon="🤖"
# )

# # Palm2 Credentials
# palm2_api_key = os.getenv('PALM2_API_KEY', '')

# def palm_(prompt='''write a cover letter for a data science job application. 
#     Summarize it to two paragraphs of 50 words each.'''):
#     model_id = "models/text-bison-001"
#     try:
#         completion = palm.generate_text(
#             model=model_id,
#             prompt=prompt,
#             temperature=0.99,
#             max_output_tokens=800,
#         )
#         return completion.result
#     except:
#         return "An error occurred"

# # Sidebar setup
# with st.sidebar:
#     st.title("Jimmy's AI Assistant\n🤖💬 Q 2.0")

#     st.sidebar.header("Upload an Image")
#     # uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
#     uploaded_file = st.sidebar.file_uploader("Choose a file...", type=None)
#     if uploaded_file is not None:
#         # Display the uploaded image
#         # st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
#         pass
#     st.markdown(
#     """
#     ## About
#     Hello meet Q, my AI Powered Personal Assistant \n 
#     Have a question? Ask Q. \n
#     Contact me on:
#     - [WhatsApp](https://wa.me/254746727592/)
#     - [email](mailto:jamesshadrack23@gmail.com) 
#     - [GitHub](https://github.com/James-Shadrack-Wafula/)
#     """
#     )
#     # st.write("Developed by [Jimmy](http://james-shadrack-wafula.rf.gd/)")

#     # Image upload functionality
    
#     st.write("Developed by [Jimmy](http://james-shadrack-wafula.rf.gd/)")
     

# # Store generated responses
# if "messages" not in st.session_state.keys():
#     st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# # Display or clear chat messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# def clear_chat_history():
#     st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
# st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# # Function to encode the image into base64 (assuming this is how the Gemini model accepts image input)
# # def encode_image(image):
# #     img = Image.open(image)
# #     buffered = BytesIO()
# #     img.save(buffered, format="PNG")  # Convert the image to PNG format (adjust if needed)
# #     img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
# #     return img_str
# def encode_file(file):
#     # Read file contents and encode it in base64
#     file_data = file.read()
#     encoded_file = base64.b64encode(file_data).decode('utf-8')
#     return encoded_file


# # Function to generate a response from Gemini with text and image inputs
# def generate_gemini_response(prompt_input, image=None):
#     # If there's an image, encode it
#     if image is not None:
#         encoded_image = encode_file(image)
#         # encoded_image = encode_image(image)
#         prompt_input += f"\nFile attached: {encoded_image}"  # Modify this part to suit how your model expects images
    
#     # Sending the prompt (and possibly image) to the model
#     response = model.generate_content(prompt_input)
    
#     # Extracting the AI's response text
#     if response and response.candidates and response.candidates[0].content.parts:
#         answer = response.candidates[0].content.parts[0].text
#         return answer.strip()  # Strip any leading or trailing whitespace/newlines
    
#     return None  # Return None if there's no valid response

# # Display the uploaded image if available
# if uploaded_file is not None:
#     # st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
#     if uploaded_file.type.startswith('image/'):
#         st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
#     else:
#         st.write(f"Uploaded file: {uploaded_file.name}")
#     encoded_file = encode_file(uploaded_file)
#     # st.write("File encoded in base64:")
#     # st.text(encoded_file)

# # Function for generating Palm2 response
# def generate_palm2_response(prompt_input):
#     response = palm_(prompt_input)
#     return response

# # def generate_gemini_response(prompt_input):
# #     response = model.generate_content(prompt_input)
    
#     # Extracting the AI's response text
#     if response and response.candidates and response.candidates[0].content.parts:
#         answer = response.candidates[0].content.parts[0].text
#         return answer.strip()  # Strip any leading or trailing whitespace/newlines
    
#     return None  # Return None if there's no valid response

# # def generate_gemini_response(prompt_input):
# #     response = model.generate_content(prompt)
# #     return response

# # Image upload functionality
# # st.sidebar.header("Upload an Image")
# # uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# # if uploaded_file is not None:
# #     # Display the uploaded image
# #     st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
#     # Optionally, process the image with Gemini or another service
#     # Example with a hypothetical function `process_image_with_gemini`
#     # response = process_image_with_gemini(uploaded_file)
#     # st.write(response)

# #User-provided prompt
# if prompt := st.chat_input("Enter your prompt:"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)

# # Generate a new response if the last message is not from the assistant
# if st.session_state.messages[-1]["role"] != "assistant":
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             # response = generate_palm2_response(prompt)
#             response = generate_gemini_response(prompt, uploaded_file)
#             st.write(response)
#     message = {"role": "assistant", "content": response}
#     st.session_state.messages.append(message)
#################################
#    V.2.0                      #
#################################



##################################
#      v.3.0                     #
##################################

import google.generativeai as genai
import os
import streamlit as st
import base64
from io import BytesIO
from PIL import Image

# Configure Gemini API
my_api = "AIzaSyAFq84DG1AVgjRdbsmWHZ2mCg4SYVdnXg4"
genai.configure(api_key=my_api)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# App title
st.set_page_config(
    page_title="Q 3.0",
    page_icon="🤖"
)

# Sidebar setup
with st.sidebar:
    st.title("Jimmy's AI Assistant\n🤖💬 Q 3.0")
    uploaded_file = st.sidebar.file_uploader("Choose a file...", type=None)
    st.markdown(
        """
        Contact me on:
        - [WhatsApp](https://wa.me/254746727592/)
        - [email](mailto:jamesshadrack23@gmail.com)
        - [GitHub](https://github.com/James-Shadrack-Wafula/)
        """
    )
    st.write("Developed by [Jimmy](http://james-shadrack-wafula.rf.gd/)")

# Store generated responses
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function to encode the file into base64
def encode_file(file):
    file_data = file.read()
    encoded_file = base64.b64encode(file_data).decode('utf-8')
    return encoded_file

# Function to generate a response from Gemini with the conversation history as context
def generate_gemini_response(conversation_history, prompt_input, image=None):
    if image is not None:
        encoded_image = encode_file(image)
        prompt_input += f"\nFile attached: {encoded_image}"
    
    # Combine all messages to maintain context
    full_prompt = "\n".join([msg["content"] for msg in conversation_history]) + "\n" + prompt_input
    
    response = model.generate_content(full_prompt)
    
    if response and response.candidates and response.candidates[0].content.parts:
        answer = response.candidates[0].content.parts[0].text
        return answer.strip()
    
    return "I'm sorry, I couldn't process that."

# Display the uploaded image if available
if uploaded_file is not None:
    if uploaded_file.type.startswith('image/'):
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    else:
        st.write(f"Uploaded file: {uploaded_file.name}")

# User-provided prompt
if prompt := st.chat_input("Enter your prompt:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if the last message is not from the assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_gemini_response(st.session_state.messages, prompt, uploaded_file)
            st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

####### v.3.0 .///##########


# Set up the chat input and image upload layout
# col1, col2 = st.columns([4, 1])  # Adjust column width ratio as needed

# # Left column: Text input for the prompt
# with col1:
#     prompt = st.chat_input("Enter your prompt:")

# # Right column: Image upload button
# with col2:
#     uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# # Process the prompt and image input
# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)

#     # If an image is uploaded, handle it
#     if uploaded_image is not None:
#         st.session_state.messages.append({"role": "user", "content": "Image uploaded"})
#         with st.chat_message("user"):
#             st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

# # Example AI response (modify with your actual AI response function)
# if prompt or uploaded_image:
#     response = generate_gemini_response(prompt)  # Adjust this to include image processing if needed
#     with st.chat_message("ai"):
#         st.write(response)