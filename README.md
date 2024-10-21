# **W.E Matter Q&A Chatbot**

### **Overview**
This repository contains the source code for the **W.E Matter Q&A Chatbot**, a conversational assistant designed to answer interview-related questions. The chatbot is fine-tuned using advanced language models and can generate responses based on the data it has been trained on.

### **Features**
- Handles interview-related questions.
- Built using **Streamlit** for an easy-to-use web interface.
- Powered by a **GPT-Neo 125M model** fine-tuned on interview Q&A data.

### **Setup Instructions**

1. **Clone the Repository**
   Start by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/Abul-Khair/W.E-Matter-QnA-Chatbot.git
   cd W.E-Matter-QnA-Chatbot
   ```

2. **Create `interview_qnda_model` Directory**
   You need to create a directory where the model files will be stored. Inside the project directory, create a folder named `interview_qnda_model`:

   ```bash
   mkdir interview_qnda_model
   ```

3. **Download Model Files**
   Download all the necessary model files from the provided **Google Drive link** below, and place them inside the `interview_qnda_model` folder.

   **[[Google Drive Link](https://drive.google.com/drive/folders/1LErbJFh3SG3XvyPwRTByRaFIClOhA9kx?usp=sharing)]**  

4. **Install Dependencies**
   Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   To launch the chatbot, run the following command:

   ```bash
   streamlit run chatbot.py
   ```

   This will start the chatbot interface in your browser.

### **Repository Structure**
- `chatbot.py`: The main file that runs the Streamlit-based chatbot interface.
- `requirements.txt`: A list of dependencies required to run the chatbot.
- `interview_qnda_model/`: Directory where the model files should be stored (created by you).

### **Usage**
Once the Streamlit app is running, you can enter interview-related questions, and the chatbot will generate responses based on the trained model.

### **Notes**
- The model files are required to run the chatbot. Make sure you download them from the provided Google Drive link and place them in the `interview_qnda_model` directory.
- The chatbot’s responses are generated based on patterns learned from the training data. Always verify the generated responses, especially in professional settings.

---

### **Contact**
For any issues or queries, please open an issue in this repository.
Abul Khair
mail: meet.abulkhair2002@gmail.com
