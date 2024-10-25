from datetime import datetime
import os
import streamlit as st

from utils.db import DbConnection
from utils.llm import llm_utils

content_prompt = "Please provide the content for the topic: {input}"

questions_prompt = """
You are an invigilator AI. Your task is to generate questions based on content that you have been provided below:
 
{input}
 
The input contains subtopics that are outlined using markdown heading sytnax.
Make one question per subtopic in the input unless the subtopic is really vast and it requires more than one input.
 
General guidelines for creating questions are given below:
Common Guidelines
1. Focus on Learning Objectives: Align each question with clear goals for what learners should achieve.
2. Keep Language Simple and Direct: Avoid unnecessary jargon to ensure questions are accessible.
3. Maintain a Consistent Difficulty Level: Match the question's difficulty to the learners’ skill level.
4. Test One Concept per Question: Prevent overlap to assess specific knowledge accurately.
5. Review and Test: Double-check for clarity, errors, and effectiveness in assessing knowledge.
6. This string should be markdown.
 
Format the output as given below:
 
{{
    "questions": [
        {{
            "question": "text of question 1",
            "answer": "answer of question 1"
        }},
        {{
            "question": "text of question 2",
            "answer": "answer of question 2"
        }},
        {{
            "question": "text of question 3",
            "answer": "answer of question 3"
        }}
    ]
}}
 
 
Don't give anything in the output besides the JSON. Strictly adhere to the format given above."""

validation_prompt  = ""

class Course:
    def __init__(self,db: DbConnection,llm_utils: llm_utils):
        self.db = db
        self.collection_name = "topics"
        self.content_from = "db"
        self.topic_history = []
        self.questions = []

    def list_topics(self):
        topics = self.db.find(self.collection_name,{})
        

        st.subheader("Python course")

        for topic in topics:
            title = topic.get("title")
            st.markdown(f"<div ><a href='http://localhost:8501/?topic={title}' style='border: 1px solid rgb(237, 235, 231);padding:15px;display:block;margin-bottom:20px;background:#fff;color:#000' target='_self'>{title.title()}</a></div>", unsafe_allow_html=True)

    def view_topic(self, topic):
        topic = self.db.find_one(self.collection_name, {"title": topic})
        description = topic.get("description")
        st.markdown(f"<a href='http://localhost:8501/' class='breadcrumb1' target='_self'>Home</a>", unsafe_allow_html=True)
        self.update_content_from_llm(topic, st.query_params["topic"])

    def update_content_from_llm(self, topic, content):
        updated_topic = llm_utils.get_llm_response(content_prompt, topic, [content])
        st.markdown(f"<div class='parent-div'></div>", unsafe_allow_html=True)
        st.write(f"{updated_topic}", unsafe_allow_html=True)
        self.topic_history.append(updated_topic)
        self.open_assessments()
    
    @st.fragment
    @st.dialog("Assessments",width="large")
    def assessments(self,questions):
        user_responses = []
        if 'submitted' not in st.session_state:
            st.session_state.submitted = False


        for i, q in enumerate(questions):
            answer = st.text_input(f"Question {i+1}: {q['question']}")
            user_responses.append({"question": q["question"], "user_response": answer, "answer": q["answer"]})  
    
        if st.button("Submit"):
            st.session_state.submitted = True
            print(user_responses) 

    @st.fragment
    def open_assessments(self):
        if 'submitted' not in st.session_state:
            st.session_state.submitted = False
        if st.button("Assessments"):
                questions_list =  llm_utils.get_llm_response(questions_prompt,  self.questions , self.topic_history)
                self.questions.append(questions_list)
        #         self.assessments([
        #     {
        #         "question": "question 1",
        #         "answer": "a"
        #     },
        #     {
        #         "question": "question 2",
        #         "answer": "b"
        #     },
        #     {
        #         "question": "question 3",
        #         "answer": "c"
        #     }
        # ])
                

    def evaluate_assessment(assessment_response):
        evaluation_response = llm_utils.get_llm_response(validation_prompt, assessment_response, [])

        print(evaluation_response)