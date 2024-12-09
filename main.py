from flask import Flask, render_template
import os

# إنشاء تطبيق Flask
app = Flask(__name__)

# الصفحة الرئيسية
@app.route("/")
def home():
    # الحصول على متغير البيئة
    app_env = os.getenv("APP_ENV", "development")  # القيمة الافتراضية 'development'
    return render_template("index.html", app_env=app_env)

# نقطة تشغيل التطبيق
if __name__ == "__main__":
    # تشغيل التطبيق
    app.run(host="0.0.0.0", port=5000)
