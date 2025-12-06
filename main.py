from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.metrics import sp
import re

class MainBoxLayout(BoxLayout):
    """
    Main layout for the calculator containing button logic, input validation,
    expression handling, and dynamic UI updates such as font resizing.
    """

    disp_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # ---------------------------------------------------------
    # Deletes the last character from the TextInput
    # ---------------------------------------------------------
    def delete_btn(self, text_input):
        curr_text_str = text_input.text
        if len(curr_text_str) > 0:
            curr_text_str = curr_text_str[:-1]
        text_input.text = curr_text_str

    # ---------------------------------------------------------
    # Clears the entire input and resets font size
    # ---------------------------------------------------------
    def clear_btn(self, text_input):
        text_input.font_size = sp(50)
        text_input.text = ""

    # ---------------------------------------------------------
    # Handles number button presses after validating input
    # ---------------------------------------------------------
    def number_btn(self, text_input, number):
        if self.text_validator(number, text_input):
            text_input.text += number
            self.dynamic_font_size(text_input)

    # ---------------------------------------------------------
    # Dynamically adjusts font size based on input length
    # ---------------------------------------------------------
    def dynamic_font_size(self, text_input):
        length = len(text_input.text)
        if length <= 6:
            text_input.font_size = sp(50)
        elif length <= 12:
            text_input.font_size = sp(25)
        else:
            text_input.font_size = sp(20)

    # ---------------------------------------------------------
    # Validates numeric and operator inputs before insertion
    # ---------------------------------------------------------
    def text_validator(self, text, curr_str_of_text):
        self.valid_int = ['1','2','3','4','5','6','7','8','9','0']
        self.valid_symbols = ['+','-','/','%','x','.']
        self.dynamic_font_size(curr_str_of_text)

        if text in self.valid_int or text in self.valid_symbols:
            if text == '-' and len(curr_str_of_text.text) == 0:
                curr_str_of_text.text += '-'
                return True
            else:
                return True
        else:
            return False

    # ---------------------------------------------------------
    # Handles operator inputs including decimals and minus logic
    # ---------------------------------------------------------
    def operator_btn(self, text_input, operator):
        curr_text = text_input.text
        segments = re.split(r"[+\-x/%]", curr_text)
        last_segment = segments[-1]

        if operator == '.' and curr_text == '':
            text_input.text += '0.'

        if self.text_validator(operator, text_input) and len(curr_text) > 0:

            if operator == '.':
                if '.' in last_segment:
                    return
                if operator == '.' and curr_text[-1] in self.valid_symbols[0:5]:
                    text_input.text += '0.'
                if str(curr_text[-1]).isnumeric():
                    text_input.text += operator

            else:
                if curr_text[-1] in self.valid_symbols[0:5]:
                    if operator == '-':
                        if (curr_text[-1] == '/') or (curr_text[-1] == 'x') or (curr_text[-1].isdigit()) or (curr_text[-1] in self.valid_symbols[4:6]):
                            text_input.text += '-'
                else:
                    text_input.text += operator

            self.dynamic_font_size(text_input)

    # ---------------------------------------------------------
    # Computes the result of the current expression
    # ---------------------------------------------------------
    def result_btn(self, text_input):
        curr_text = text_input.text
        percentage_pattern = r"(\d+(?:\.\d+)?)%(\d+(?:\.\d+)?)"
        match_percentage_pattern = re.findall(percentage_pattern, curr_text)

        if len(curr_text) > 0:
            if 'x' in curr_text:
                curr_text = curr_text.replace('x', '*')

            try:
                if match_percentage_pattern:
                    first_percentage_item, second_percentage_item = match_percentage_pattern[0]
                    res = round(eval(first_percentage_item) * eval(second_percentage_item) / 100, 12)
                    text_input.text = str(res)
                    self.dynamic_font_size(text_input)

                else:
                    try:
                        res = round(eval(curr_text), 12)
                        text_input.text = str(res)
                        self.dynamic_font_size(text_input)
                    except ZeroDivisionError:
                        text_input.text = ""

            except SyntaxError:
                return


class CalculatorApp(App):
    """
    Main Kivy App launcher for the calculator.
    """
    def build(self):
        return MainBoxLayout()


CalculatorApp().run()
