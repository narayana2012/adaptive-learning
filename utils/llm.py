import os
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
os.environ["GROQ_API_KEY"] = "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"
llm = ChatGroq(temperature=0, model_name="llama-3.2-90b-text-preview")
class llm_utils:
    
    # Function to get LLM response
    def get_llm_response(prompt,input, history):
        chat_prompt = ChatPromptTemplate.from_template(prompt)
        # Combine history and question into a single context
        context = "\n".join(history) + f"\nUser: {input}"
        
        # Get response from the LLM
        runnable = chat_prompt | llm | StrOutputParser()

        inputs = {
            "input": context
        }

        response = runnable.invoke(inputs)

        print(response)
        
        # Extract the response text
        return response.strip()