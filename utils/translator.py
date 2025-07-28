import openai

def translate_text(text, target_lang='tl'):
    prompt = f'Translate the following to {target_lang}:\n{text}'
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=300
    )
    return response.choices[0].message['content']