from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# حط مفتاحك هنا
client = Groq(api_key="PUT_YOUR_KEY_HERE")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    user_msg = data.get('message')

    instructions = (
        f"أنت استشاري نفسي خبير ومباشر. المستخدم هو {name} ({age} سنة). "
        "مطورك هو المبرمج عبد الرحمن أحمد. "
        "قدم حلول عملية مباشرة باللهجة المصرية."
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

        reply = completion.choices[0].message.content
        return jsonify({'reply': reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({'reply': "فيه ضغط على العيادة، ابعت تاني يا بطل."})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
