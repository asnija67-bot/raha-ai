import google.generativeai as genai

# المفتاح السليم بتاعك
genai.configure(api_key="AIzaSyAGZ5i0aQ25dO-GLxeLL3dasNpOdofbSRY")

# اخترنا أحدث وأسرع موديل متاح عندك
model = genai.GenerativeModel('gemini-2.5-flash')

print("جاري الاتصال بالذكاء الاصطناعي... ⏳")

# بنبعتله الرسالة
response = model.generate_content("اكتب جملة ترحيب وتحفيز قصيرة جدا لمبرمج مصري اسمه عبد بيبدأ مشروع جديد.")

print("\nالذكاء الاصطناعي بيقولك: 🤖")
print(response.text)
