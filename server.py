import json
import os
from utils.db import DbConnection
from pages.course import Course
import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import streamlit as st
from dotenv import load_dotenv
from utils.llm import llm_utils
from components.header import Header 

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

load_dotenv()
db_connect = DbConnection()


os.environ["GROQ_API_KEY"] = "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"

# Initialize the LLM
llm = ChatGroq(temperature=0, model_name="llama-3.2-90b-text-preview")


PROMPT = """
Course is Python Programming
Create an interactive session to explain a topic when requested, and guide the user until they understand it, by providing explanations and responsive questioning.

Begin with an breaf detailed explanation of the topic with sub topics with fast learner in mind. and dont suggest any other topics here, Dont ask any user response or dont show practice, DOnt prompt for practice as well, Assess the user's understanding, provide clarification and examples based on their feedback, and continue engaging until mastery is demonstrated.
{input}

"""


PROMPT2 = """
Can you generate 3 MCQ questions with 4 options along with correct answer in JSON format.
    json format should be like this:
    {{
        "questions": [
            {{
                "question": "question 1",
                "options": ["a", "b", "c", "d"],
                "answer": "a"
            }},
            {{
                "question": "question 2",
                "options": ["a", "b", "c", "d"],
                "answer": "b"
            }},
            {{
                "question": "question 3",
                "options": ["a", "b", "c", "d"],
                "answer": "c"
            }}
        ]
    }}
    
INPUT:    
{input}

And dont print any other data except JSON
"""



st.set_page_config(layout="wide")

Header.header()

llm_call = llm_utils()
course = Course(db_connect,llm_call)


def handle_user_responses(questions):
    user_responses = []
    for i, q in enumerate(questions):
        selected_option = st.radio(
            f"Question {i+1}: {q['question']}", 
            q["options"], 
            index=None, 
            key=f"question_{i}",
            disabled=st.session_state.submitted
        )
        user_responses.append({"question": q["question"], "selected": selected_option})
    return user_responses

@st.fragment
@st.dialog("Assessments",width="large")
def display_questions(questions):
    user_responses = handle_user_responses(questions)
    if st.button("Submit"):
        process_submission(user_responses, questions)

def process_submission(user_responses, questions):
    st.session_state.submitted = True
    st.session_state.submitted = True
    st.write("Your answers:")
    for response in user_responses:
        question_text = response['question']
        selected = response['selected']
        correct = next(q['answer'] for q in questions if q['question'] == question_text)
        color = "green" if selected == correct else "red"
        st.markdown(f"<span style='color:{color}'>Question: {question_text}, Selected: {selected}</span>", unsafe_allow_html=True)


with st.container():
    if st.query_params.get("topic"):

        course.view_topic(st.query_params.get("topic"))
        print("restarted")
        # update(st.query_params["topic"])
        # inserted_id = db_connect.insert_data('topics', {"title":"test"})
        # print(inserted_id)



        # st.markdown(f"<a href='http://localhost:8501/' target='_self'>Home</a>", unsafe_allow_html=True)
        
        # st.write(st.query_params["topic"])
        # for entry in st.session_state.history:
        #     if entry.startswith("User:"):
        #         st.write(f"**Topic:** {entry.replace('User: ', '')}")
        #     else:
        #         st.write(f"{entry.replace('AI: ', '')}")

        # if st.session_state.history:
        #     st.write(f"{entry.replace('AI: ', '')}")


        # @st.fragment
        # @st.dialog("Assessments",width="large")
        # def assessments(questions):
        #     user_responses = []
        #     if 'submitted' not in st.session_state:
        #         st.session_state.submitted = False


        #     for i, q in enumerate(questions):
        #         selected_option = st.radio(
        #             f"Question {i+1}: {q['question']}", 
        #             q["options"], 
        #             index=None, 
        #             key=f"question_{i}",
        #             disabled=st.session_state.submitted
        #         )
        #         user_responses.append({"question": q["question"], "selected": selected_option})  
        
        #     if st.button("Submit"):
        #         st.session_state.submitted = True
        #         st.write("Your answers:")
        #         for response in user_responses:
        #             question_text = response['question']
        #             selected = response['selected']
        #             correct = next(q['answer'] for q in questions if q['question'] == question_text)
        #             color = "green" if selected == correct else "red"
        #             st.markdown(f"<span style='color:{color}'>Question: {question_text}, Selected: {selected}</span>", unsafe_allow_html=True)




        @st.fragment
        def open_assessments():
            if 'submitted' not in st.session_state:
                st.session_state.submitted = False
            if st.button("Assessments"):
                    questions_list = questions("python lists")
                    display_questions(questions_list.get("questions"))

        # open_assessments()



    else:
        course.list_topics()

        


    # else:
    #     st.write("Python course")
    #     topics = ['Lists',"Tuples","Dictionaries"]
    #     # st.markdown(generate_menu(topics), unsafe_allow_html=True)
    #     for topic in topics:
    #         st.markdown(f"<a href='http://localhost:8501/?topic={topic}' target='_self'>{topic}</a>", unsafe_allow_html=True)

