students = [
    {"id": 1, "name": "An", "score": 8.5},
    {"id": 2, "name": "Bình", "score": 7.2},
    {"id": 3, "name": "Chi", "score": 9.0}
]
def find_by_id(data: list[dict], id: int) -> dict | None:
    for sv in data:
        if sv["id"] == id:
            return sv
    return None

def filter_by_score(data, min_score):
    return [sv for sv in data if sv["score"] >= min_score]

def sort_by_score(data, reverse=False):
    return sorted(data, key=lambda sv: sv["score"], reverse=reverse)

def add_student(data, student):
    if find_by_id(data, student["id"]) is None:
        data.append(student)
    return data

def remove_student(data, id):
    return [sv for sv in data if sv["id"] != id]

def statistics(data):
    mean = sum(sv["score"] for sv in data) / len(data)
    highest = max(data, key=lambda sv: sv["score"])
    lowest = min(data, key=lambda sv: sv["score"])
    return mean, highest, lowest

print(find_by_id(students, 3))
print(filter_by_score(students, 8.0))
print(sort_by_score(students))
print(add_student(students, {"id": 4, "name": "Dũng", "score": 6.8}))
print(remove_student(students, 1))
print(statistics(students))