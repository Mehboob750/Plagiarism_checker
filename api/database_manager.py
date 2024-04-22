import chromadb
import uuid
# from .models import McqTable
from openai import OpenAI
import openai
import json
import numpy as np
from decouple import config


chroma_client = chromadb.HttpClient()
collection_name = "sample_space"
chroma_collection = chroma_client.get_or_create_collection(collection_name)


# from openai import OpenAI
# openai_client = openai.api_key = config('API_KEY')
client = OpenAI(api_key= config('API_KEY'))
print(config('API_KEY'),'087543579-')

def get_questions_from_sql():
    # data = []
    # rows = McqTable.objects.all()
    # # print(rows,'098645790')
    # for row in rows:
    #     # print(row,'-0976545780-')
    #     data.append(row)
    # return data
    data = [
        {
            "id": '1',
            "question_text": "Consider the following statements regarding soil types in India: 1. Black soil is ideal for growing cotton and is primarily found in the Deccan plateau. 2. Alluvial soil is the most fertile and covers the majority of northern India. 3. Red soil is typically acidic and not very fertile. How many of the statements above are accurate?",
            "institute_name": "Vision IAS",
            "publish_date": "",
            "test_series_name": "Test Series 2",
            "test_series_code": "TS002",
            "course_name": "UPSC"
        },
        {
            "id": '2',
            "question_text": "Consider the following statements about the Himalayan mountains: 1. The Himalayas form a natural barrier for India against external invasions. 2. They are geologically the oldest mountain range in India. 3. The Himalayas play a crucial role in influencing the climate of India. How many of the statements above are accurate?",
            "institute_name": "Vision IAS",
            "publish_date": "",
            "test_series_name": "Test Series 3",
            "test_series_code": "TS003",
            "course_name": "UPSC"
        },
        {
            "id": '3',
            "question_text": "Consider the following statements about Indian rivers: 1. The Ganges is the longest river in India. 2. Most of the major rivers in India flow towards the east. 3. Rivers in India do not have any significant religious importance. How many of the statements above are accurate?",
            "institute_name": "Vision IAS",
            "publish_date": "",
            "test_series_name": "Test Series 4",
            "test_series_code": "TS004",
            "course_name": "UPSC"
        },
        {
            "id": '4',
            "question_text": "Consider the following statements regarding India's climate: 1. The Thar Desert is the hottest region in India. 2. The northeast monsoon primarily affects the south of India. 3. Coastal areas in India experience a temperate climate. How many of the statements above are accurate?",
            "institute_name": "Vision IAS",
            "publish_date": "",
            "test_series_name": "Test Series 5",
            "test_series_code": "TS005",
            "course_name": "UPSC"
        },
        {
            "id": '5',
            "question_text": "Consider the following statements about the Indian economy: 1. Agriculture is the largest sector of the Indian economy. 2. India is the world's largest producer of milk. 3. The service sector contributes the least to the GDP of India. How many of the statements above are accurate?",
            "institute_name": "Vision IAS",
            "publish_date": "",
            "test_series_name": "Test Series 6",
            "test_series_code": "TS006",
            "course_name": "UPSC"
        }
    ]

    return data

def save_questions():
    rows = get_questions_from_sql()
    questions = []
    embeddings = []
    ids = []
    metadatas = []
    for row in rows:
        questions.append(row["question_text"])
        embeddings.append(get_embedding(row["question_text"]))
        ids.append(row["id"])
        metadatas.append(
            {
                "institute_name": row["institute_name"],
                "publish_date": row["publish_date"],
                "test_series_name": row["test_series_name"],
                "test_series_code": row["test_series_code"],
                "course_name": row["course_name"]
            }
        )
    chroma_collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=questions,
        metadatas=metadatas,
    )


def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding


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


def get_data(question: str):
    # print(question)
    question_embedding = get_embedding(question)
    print(question_embedding,'98765q35790')
    results = chroma_collection.query(
        query_embeddings=question_embedding,
        n_results=5
    )
    print(results["ids"],'0975446789')
    [print(doc) for doc in results["documents"][0]]
    # print(results["documents"][0][0], "\n\n\n", question, "\n\n\n")
    similarity = cosine_similarity(results["documents"][0][0], question)

    return {
        "similarity": similarity,
        "matching_question": results["documents"][0][0],
        "metadata": results["metadatas"][0][0]
    }


def remove_db():
    chroma_client.delete_collection(collection_name)

# remove_db()
# save_questions()
