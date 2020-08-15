import re


def extract_question(input, filename):
    question_dict = {"question": "", "wrongAnswers": [], "correctAnswers": []}
    question_pattern = r"""^(.|\n)+?(?=\n{3})"""
    wrong_answer_pattern = r"\[ \]\s*(.+(\n?(?!\[( |X)\]|\Z).+)+)"
    correct_answer_pattern = r"\[X\]\s*(.+(\n?(?!\[( |X)\]|\Z).+)+)"

    # Seperate the string into its different parts.
    question = re.search(question_pattern, input)

    if (not question):
        raise SyntaxError("No question found in file: " + filename)
    if (re.search(wrong_answer_pattern, input) is None):
        raise SyntaxError(
            "Found a question, but no wrong answers found for: " + filename)
    if (re.search(correct_answer_pattern, input) is None):
        raise SyntaxError(
            "Found a question, but no correct answers found for: " + filename)

    wrong_answers = re.finditer(wrong_answer_pattern, input)
    correct_answers = re.finditer(correct_answer_pattern, input)

    # Save the different parts in the dict.
    question_dict["question"] = question.group()

    for match in wrong_answers:
        answer = match.group(1)
        question_dict["wrongAnswers"].append(answer)

    for match in correct_answers:
        answer = match.group(1)
        question_dict["correctAnswers"].append(answer)

    return question_dict


def debug():
    import pprint
    pp = pprint.PrettyPrinter(indent=4)

    test_str = ("    #include <stdio.h>\n\n"
                "    int main()\n"
                "    {\n"
                "        int i;\n"
                "        for (i = 10; i; i--)\n"
                "            printf(\".\");\n"
                "        return 0;\n"
                "    }\n"
                "Wie viele Punkte gibt das oben gezeigte Programm aus?\n\n\n"
                "[ ] Das Programm terminiert nicht. Es gibt so lange Punkte aus, bis es manuell abgebrochen wird.\n"
                "Die Antwort geht hier weiter\n"
                "[X] Dies ist ein Test\n"
                "Hier geht er weiter\n"
                "[ ] 11\n"
                "[ ] Keine.\n"
                "test\n"
                "test\n"
                "test\n\n"
                "[ ] test\n\n"
                "[ ]\n"
                "jnn\n\n"
                "\\[ \\](.*)")

    # pp.pprint(extract_question(test_str))


# debug()
