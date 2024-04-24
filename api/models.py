# In your Django project's models.py
from django.db import models

class McqTable(models.Model):
    institute_name = models.CharField(max_length=100)
    publish_date = models.DateField()
    test_series_name = models.CharField(max_length=100)
    test_series_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/', null=True)
    question_text = models.TextField()
    option_a = models.CharField(max_length=100, null=True)
    option_b = models.CharField(max_length=100, null=True)
    option_c = models.CharField(max_length=100, null=True)
    option_d = models.CharField(max_length=100, null=True)
    correct_answer = models.CharField(max_length=1, null=True)

    class Meta:
        """meta class to store table name and unique constrants"""

        db_table = "mcq_questions_plag"