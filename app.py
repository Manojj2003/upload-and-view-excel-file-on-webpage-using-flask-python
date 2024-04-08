from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/excel"

@app.route("/", methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        upload_excel = request.files['upload_excel']
        if upload_excel.filename != '':
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], upload_excel.filename)
            upload_excel.save(filepath)
            data = pd.read_excel(upload_excel)
            html_content = data.to_html(index=False).replace('<th>', '<th style="text-align:center">')
            return render_template("ExcelFile.html", data=html_content)  # Passing html_content as 'data' variable
    return render_template("uploadExcel.html")

if __name__ == '__main__':
    app.run(debug=True)
