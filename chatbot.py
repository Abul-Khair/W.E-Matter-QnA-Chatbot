import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the trained model and tokenizer
@st.cache_resource
def load_model_and_tokenizer():
    model_path = r"C:\Users\Khairul\Documents\W.E Matter Chatbot\interview_qnda_model"  # Use raw string or double backslashes
    model = AutoModelForCausalLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

model, tokenizer = load_model_and_tokenizer()

# Set up the Streamlit app
st.title("Interview Q&A Assistant")
st.write("Ask a question, and the model will generate a response based on its training.")

# Input for user's question
user_question = st.text_input("Enter your question:")

# Function to generate response
def generate_response(question, max_length=150):
    input_text = f"Question: {question}\nAnswer:"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    
    # Generate response
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response.split("Answer:")[-1].strip()

# Generate and display response when user submits a question
if user_question:
    with st.spinner("Generating response..."):
        response = generate_response(user_question)
    st.write("Model's response:")
    st.write(response)

# Add some information about the model
st.sidebar.header("About the Model")
st.sidebar.write("This model was fine-tuned on interview Q&A data using the GPT-Neo 125M model as a base.")
st.sidebar.write("It can generate responses to interview-related questions based on its training.")

# Add a note about potential limitations
st.sidebar.header("Note")
st.sidebar.write("The model's responses are generated based on patterns in its training data. Always verify important information and use critical thinking when considering the responses.")
