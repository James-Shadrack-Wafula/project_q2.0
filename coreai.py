import google.generativeai as palm
palm.configure(api_key="AIzaSyBHINqTvLyNBmt3VCSBHYaqxsxfBjBlHDk")


from langchain_community.embeddings import GooglePalmEmbeddings
from langchain_community.llms import GooglePalm

# palm.configure(api_key=API_KEY)

models = [model for model in palm.list_models()]

for model in models:
  print(model.name)
def palm_(prompt='''write a cover letter for a data science job applicaton. 
    Summarize it to two paragraphs of 50 words each. '''):
    model_id="models/text-bison-001"
    # prompt='''write a cover letter for a data science job applicaton. 
    # Summarize it to two paragraphs of 50 words each. '''

    completion=palm.generate_text(
        model=model_id,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
    )

    print(completion.result)

def lang():
    llm=GooglePalm(google_api_key="AIzaSyBHINqTvLyNBmt3VCSBHYaqxsxfBjBlHDk")
    llm.temperature=0.2

    prompts=["How to Calculate the area of a triangle?","How many sides are there for a polygon?"]
    llm_result= llm._generate(prompts)

    res=llm_result.generations
    print(res[0][0].text)
    print(res[1][0].text)


while True:
    prompt = str(input("Enter prompt: "))
    palm_(prompt)