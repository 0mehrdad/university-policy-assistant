import os
from dotenv import load_dotenv
from qa import get_answer
import json

load_dotenv()

def evaluate():
    #load evaluation questions
    with open('src/eval_data.json', 'r') as f:
        eval_data = json.load(f)
    source_hits = 0
    page_hits = 0
    for item in eval_data:
        question = item['query']
        expected_pdf = item['correct_source']
        expected_page = item['correct_page']
        answer , sources = get_answer(question)
        answer_sources = [(s['source'], s['page']) for s in sources]
        if any(expected_pdf in src for src, _ in answer_sources):
            source_hits += 1
        if any(expected_page == page for _, page in answer_sources):
            page_hits += 1
    total = len(eval_data)
    print(f"Source Accuracy: {source_hits}/{total} = {source_hits/total:.2%}")
    print(f"Page Accuracy: {page_hits}/{total} = {page_hits/total:.2%}")

if __name__ == "__main__":
    evaluate()

