import openai

def summarize_text(text, max_tokens=300):
    prompt = f'Summarize this book:\n\n{text[:3000]}'
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=max_tokens
    )
    return response.choices[0].message['content']