import openai
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_script(topic):
    prompt = f"{topic} বিষয় নিয়ে ১ মিনিটের ভিডিও স্ক্রিপ্ট লেখো"
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']
