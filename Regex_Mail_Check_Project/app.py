from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    matches = []
    highlighted_string = ""

    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")
        case_insensitive = request.form.get("case_insensitive") is not None

        flags = re.IGNORECASE if case_insensitive else 0

        try:
            matches = list(re.finditer(regex_pattern, test_string, flags))
            highlighted_string = ""
            last_end = 0

            for match in matches:
                start, end = match.span()

                if last_end < start:
                    highlighted_string += (f"<span style='background-color: yellow;'>{test_string[last_end:start]}</span>")

                highlighted_string += (f"<span style='background-color: green;'><b>{test_string[start:end]}</b></span>")
                last_end = end
            
            if last_end < len(test_string):
                highlighted_string += (f"<span style='background-color: yellow;'>{test_string[last_end:]}</span>")
                
        except re.error:
            matches = "Invalid regex pattern."

    return render_template("regex_check.html", matches=matches, highlighted_string=highlighted_string)

@app.route("/validate_email", methods=["GET", "POST"])
def validate_email():
    email = ""
    is_valid = None
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  

    if request.method == "POST":
        email = request.form.get("email")
        if re.match(email_regex, email):
            is_valid = True
        else:
            is_valid = False

    return render_template("mail_check.html", email=email, is_valid=is_valid)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')