from groq import Groq
from quiz_params import no_questions , category
import json


client = Groq(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"""generate a quiz json of {no_questions} questions and category {category} with choices and correct answer like this format:

    
    "question": "Which Formula One driver was nicknamed &#039;The Professor&#039;?",
    "correct_answer": "Alain Prost",
    "incorrect_answers": [
        "Ayrton Senna",
        "Niki Lauda",
        "Emerson Fittipaldi"
    ]
"""
        }
    ],
    model="llama3-8b-8192"  
)

print(chat_completion.choices[0].message.content)


response = chat_completion.choices[0].message.content ;

start = response.find('[')
end = response.rfind(']') + 1
if start != -1 and end != 0:
    response = response[start:end]

print("CLEAN PROMPT ____________")
print(response)

question_data_groq = json.loads(response);