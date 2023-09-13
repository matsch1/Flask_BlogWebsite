from flask_sqlalchemy import SQLAlchemy
import os

from website.static.python.LineCounter import LineCounter


db = SQLAlchemy()


def count_lines():
    number_of_python_lines = get_number_of_lines('py')
    number_of_html_lines = get_number_of_lines('html')

    number_of_lines = {'python': number_of_python_lines,
                       'html': number_of_html_lines}

    return number_of_lines


def get_number_of_lines(coding_language):

    app_directory = os.getcwd()

    spacer = detect_spacer(app_directory)

    app_directory = app_directory + spacer + "website"

    line_counter = LineCounter(app_directory, coding_language, spacer)

    return line_counter.number_of_lines


def detect_spacer(directory):
    if "/" in directory:
        return "/"
    elif "\\" in directory:
        return "\\"
    else:
        return None
