from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .database_manager import get_data


#######################

#######################

#vector match
# API endpoint to match question with Vision DB and return output
@csrf_exempt
def match_question(request):
    if request.method == 'POST':
        input_data = json.loads(request.body)
        original_question = input_data.get('question_text')
        # {
        #     "question_text": ques.question_text,
        #     "institute_name": ques.institute_name,
        #     "publish_date": ques.publish_date,
        #     "test_series_name": ques.test_series_name,
        #     "test_series_code": ques.test_series_code,
        #     "course_name": ques.course_name,
        #     "option_a" : ques.option_a,
        #     "option_b" : ques.option_b,
        #     "option_c" : ques.option_c,
        #     "option_d" : ques.option_d,
        #     "correct_answer" :  ques.correct_answer,
        #     "matching_score": closest
        # }
        data = get_data(original_question)
        return JsonResponse(data)
