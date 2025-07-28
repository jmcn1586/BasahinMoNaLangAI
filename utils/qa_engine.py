import openai

def ask_question(context, question, max_tokens=300):
    prompt = f'Based on the following book, answer the question clearly:\n\nBOOK:\n{context[:3000]}\n\nQUESTION: {question}'
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=max_tokens
    )
    return response.choices[0].message['content']