# Talk to PDF

This mini-project involves a combination of `OpenAI`, `LangChain` and `Facebook AI Similarity Search (FAISS)` to be able to talk to any PDF of your choice. 

`OpenAI` is mainly used for its embeddings model.

`LangChain` is the main library which helps in ease of question-answering the "PDF" as it is a wrapper which enables us to embed the PDF, store in a vector database, connects to `FAISS` to help with similarity search whenever a new query is sent to our custom chatbot. 

In order to use the code in `script.ipynb`, you will need to make a `.env` file with __OPEN_API_KEY__ key having the value of API key from your account on OpenAI. 

## Quickstart
Make sure to clone the repo on your machine before starting:
```bash
git clone https://github.com/tushar2407/talk_to_pdf.git
cd talk_to_pdf
```
Let's dive into the tutorial on talking to PDF of your choice.
First, create a virtual environment using the below command:
```bash
virtualenv venv
```
Next, activate your _venv_ virtual environment:
```bash
# for Linux/Mac
source venv/bin/activate

# for Windows
venv\Scripts\activate 
``` 
Now, install all the required packages:
```bash
pip install -r requirements.txt
```
Lastly, create a `.env` file with the following format:
```
OPENAI_API_KEY="..."
```
In the file, replace "..." with your OpenAI's API key.

With the above steps, you are all set to run `script.ipynb` without any error.

🚨 Caution: Make sure to select your Jupyter Notebook's kernel as your current virtual environment.