from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# قراءة مفتاح الذكاء الاصطناعي من السيرفر
API_KEY = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=API_KEY)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json

    name = data.get("name")
    age = data.get("age")
    message = data.get("message")

    # تعليمات الذكاء الاصطناعي
    instructions = (
        f"أنت مستشار نفسي هادئ ومحترف. "
        f"المستخدم اسمه {name} وعمره {age}. "
        "تحدث باللهجة المصرية بشكل محترم ومختصر. "
        "قدم نصائح واضحة ومفيدة. "
        "إذا سألك أي شخص من صنعك أو من مطورك قل له: "
        "تم تطويري بواسطة عبدو."
    )

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": message}
            ],
            temperature=0.6
        )

        reply = completion.choices[0].message.content

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        print(e)

        return jsonify({
            "reply": "حصل ضغط على السيرفر، حاول تاني بعد شوية."
        })


# تشغيل السيرفر
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
