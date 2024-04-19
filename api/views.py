from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import McqTable
import numpy as np
import openai



#######################
import json
# from openai import OpenAI
openai_client = openai.api_key = "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"

def get_questions():

    data = []
    rows = McqTable.objects.all()
    # print(rows,'098645790')
    for row in rows:
        # print(row,'-0976545780-')
        data.append(row)
    return data


def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
#    print('098654345680-')
   return openai.Embedding.create(input=[text], model=model).data[0].embedding


def cosine_similarity(existing_question, new_question):
    vec1 = get_embedding(existing_question)
    vec2 = get_embedding(new_question)

    # Calculate the dot product between the two vectors
    dot_product = np.dot(vec1, vec2)
    # Calculate the norm (magnitude) of each vector
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    # Calculate the cosine similarity
    similarity = dot_product / (norm_vec1 * norm_vec2)
    # print(similarity,'-09764335680-')
    return similarity

#######################

#vector match
# API endpoint to match question with Vision DB and return output
@csrf_exempt
def match_question(request):
    if request.method == 'POST':
        input_data = json.loads(request.body)
        original_question = input_data.get('question_text')
        # print(original_question)
        # cosine_similarity
        questions_data = get_questions()
        # print(questions_data)

        closest = 0
        similar_question = ''
        # print(questions_data,'987534579')
        for ques in questions_data:
            # print('8764346790', ques, ques.question_text)
            calculated_closest = cosine_similarity(new_question=original_question, existing_question=ques.question_text)
            if  calculated_closest > closest:
                closest = calculated_closest
                similar_question = ques.question_text
                response_data = {
                    "question_text": ques.question_text,
                    "institute_name": ques.institute_name,
                    "publish_date": ques.publish_date,
                    "test_series_name": ques.test_series_name,
                    "test_series_code": ques.test_series_code,
                    "course_name": ques.course_name,
                    "option_a" : ques.option_a,
                    "option_b" : ques.option_b,
                    "option_c" : ques.option_c,
                    "option_d" : ques.option_d,
                    "correct_answer" :  ques.correct_answer,
                    "matching_score": closest
                }
        return JsonResponse(response_data)
