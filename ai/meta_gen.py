import openai
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_metadata(topic):
    prompt = f"{topic} বিষয় নিয়ে ইউটিউব ভিডিওর জন্য একটি SEO ফ্রেন্ডলি টাইটেল, ডেসক্রিপশন ও ৫টি ট্যাগ তৈরি করো"
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    text = res['choices'][0]['message']['content']
    # Parse your output accordingly
    title = "Auto Title"
    description = "Auto description"
    tags = ["tag1", "tag2", "tag3"]
    return title, description, tags