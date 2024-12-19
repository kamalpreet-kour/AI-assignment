
import random

colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "purple": "#800080"
}

def get_color_question():
    color_name, color_code = random.choice(list(colors.items()))
    return {"name": color_name, "code": color_code}

def check_answer(user_answer):
    user_answer = user_answer.lower().strip()
    correct_color = next((name for name, code in colors.items() if user_answer == name), None)
    if correct_color:
        return True, f"Correct! The color was {correct_color.capitalize()}."
    return False, "Incorrect! Please try again."
            