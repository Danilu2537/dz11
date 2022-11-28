import json

CANDIDATES_PATH = "candidates.json"
"""Путь к json файлу с кандидатами"""


def load_candidates_from_json(path=CANDIDATES_PATH):
    """
    Загружает кандидатов из файла.
    :param path: Путь к файлу с кандидатами.
    :return: Список со словарями кандидатов.
    """
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)


def get_candidate(candidate_id):
    """
    Возвращает одного кандидата с искомым id
    :param candidate_id: id кандидата
    :return: Словарь с информацией о кандидате
    """
    for candidate in load_candidates_from_json():
        if candidate.get("id") == candidate_id:
            return candidate
    return


def get_candidate_by_name(candidate_name):
    """
    Возвращает список кандидатов с искомым именем.
    :param candidate_name: Имя искомого кандидата.
    :return: Список кандидатов.
    """
    candidates = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate.get("name").lower():
            candidates.append(candidate)
    return candidates


def get_candidate_by_skill(skill_name):
    """
    Возвращает список кандидатов, владеющих искомым навыком.
    :param skill_name: Навык.
    :return: Список кандидатов.
    """
    candidates = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate.get("skills").lower().split(", "):
            candidates.append(candidate)
    return candidates
