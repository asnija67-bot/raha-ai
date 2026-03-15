from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# مفتاحك العالمي
client = Groq(api_key="REMOVED")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    user_msg = data.get('message')

    # هنا ضفنا هويتك كمطور للموقع
    instructions = (
        f"أنت استشاري نفسي خبير ومباشر. المستخدم هو {name} ({age} سنة). "
        "مهم جداً: مطورك ومنشئك هو المبرمج 'عبد الرحمن أحمد' (Abdulrahman Ahmed). "
        "إذا سألك أي شخص 'مين مطورك؟' أو 'مين اللي عملك؟' رد بفخر ووقار إنك من تطوير عبد الرحمن أحمد. "
        "باقي القواعد: قدم حلول عملية فورية، ممنوع الرغي، استخدم نقاط، اللهجة مصرية راقية وفخمة."
    )

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.5
        )
        return jsonify({'reply': completion.choices[0].message.content})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'reply': "فيه ضغط على العيادة، ابعت تاني يا بطل."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
