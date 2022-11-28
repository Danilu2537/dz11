"""
Почти реально сайт...
V0.0.2
"""
from flask import Flask, render_template
from utils import *

app = Flask(__name__, template_folder="templates")


@app.route("/")
def all_candidate():
    """
    Показывает страницу со всеми кандидатами
    """
    return render_template("list.html", candidates=load_candidates_from_json())


@app.route("/candidate/<int:candidate_id>")
def candidate_by_id(candidate_id):
    """
    Показывает одного кандидата по id со всей информацией
    """
    return render_template("card.html", candidate=get_candidate(candidate_id))


@app.route("/search/<candidate_name>")
def candidates_by_name(candidate_name):
    """
    Показывает всех кандидатов с искомым именем
    """
    candidates = get_candidate_by_name(candidate_name)
    return render_template("search.html", candidate_name=candidate_name, candidates_count=len(candidates),
                           candidates=candidates)


@app.route("/skill/<skill_name>")
def candidates_by_skill(skill_name):
    """
    Показывает всех кандидатов с искомым навыком
    """
    candidates = get_candidate_by_skill(skill_name)
    return render_template("skill.html", candidates_skill=skill_name, candidates_count=len(candidates),
                           candidates=candidates)


@app.route("/author")
def author():
    """
    Страничка об авторе из первой части задания
    """
    return render_template("me.html")


if __name__ == "__main__":
    app.run(debug=True)
