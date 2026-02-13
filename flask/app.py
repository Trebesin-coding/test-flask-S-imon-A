from flask import Flask, request, render_template, url_for, redirect
import json

app = Flask(__name__)

data: list[dict] = []

def load_file_data() -> list[dict]:
    loaded_data: list[dict] = []

    with open("data/recenze.json", "r", encoding="UTF-8") as file:
        loaded_data = json.load(file)

    return loaded_data

def save_data_to_file(data_to_save: list[dict]) -> None:
    with open("data/recenze.json", "w", encoding="UTF-8") as file:
        json.dump(data_to_save, file, indent=4)

@app.route("/")
def vitej() -> str:
    return render_template("vitej.html")

@app.route("/form", methods=["GET", "POST"])
def form() -> str:
    if request.method == "POST":
        login: str = request.form.get("login")
        recenze: str = request.form.get("recenze")

        #if recenze == "nic":
        if len(recenze) <= 3:
            recenze = "uživatel byl příliš líný na napsání recenze"
        
        recenze_data: dict = {
            "login": login,
            "recenze": recenze
        }

        data.append(recenze_data)

        save_data_to_file(data)

        return render_template("form.html", login=login, recenze=recenze)

    return render_template("form.html", login="", recenze="")

#tato část kódu se zpustí, pokuď je tento soubor spuštěn jako, hlavní (není jenom importován)
if __name__ == "__main__":
    data = load_file_data()

    #tato část zpustí aplikaci, jako local development server a bude v debug módu
    app.run(debug=True)
