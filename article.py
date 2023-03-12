import openai
import os

with open('api.txt') as f:
    openai.api_key = f.readlines()[0].replace('chatgpt: ', '').strip()

model_engine = "text-davinci-003"

def ask(prompt):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return completion.choices[0].text

folder = 'article-wip'
keyword = 'workplace bullying effects'

def generate_title_ideas():
    response = ask(f'write 10 click-baity, captivating and thought-provoking title ideas for a blog post for the following keyword: "{keyword}". the keyword must be inside the title as exact match.')
    with open(f'./{folder}/title-ideas.txt', 'w') as f: f.write(response.strip())
    print(response)

def generate_h2():
    response = ask(f'''write a blog post outline for {keyword}.
        do NOT include introduction.
        do NOT include conclusion.
        do NOT include definition.
        do NOT repeat yourself.
        use an engaging and casual tone of voice.
    ''')
    with open(f'./{folder}/outline.txt', 'w') as f: f.write(response)
    print()
    print()
    print(response)


def generate_h3():
    with open('./article-wip/draft/h2.txt') as f: lines = f.readlines()
    for line in lines:
        response = ask(f'write a complete list of {line}.')
        print(line)
        print(response)
        print()
        print()

# use an engaging and casual tone of voice.

# generate_title_ideas()
# generate_h2()
# generate_h3()


response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": "write an essay about penguins"}
    ],
)

print(response.choices[0].message.content)