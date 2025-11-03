from kivy.app import App  # import the App base class from Kivy to create the application
from kivy.uix.boxlayout import BoxLayout  # import BoxLayout widget for main layout
from kivy.uix.stacklayout import StackLayout  # import StackLayout (not used directly here) for possible layouts
from kivy.properties import StringProperty  # import StringProperty (not used currently) for reactive properties
from kivy.metrics import sp  # import sp helper to set scalable pixel font sizes
import re  # import the regular expressions module for parsing expressions

class MainBoxLayout(BoxLayout):  # define the main layout class inheriting from BoxLayout
    def __init__(self, **kwargs):  # constructor receiving keyword arguments
        super().__init__(**kwargs)  # call parent constructor to initialize layout
    
    def text_validator(self, text):  # method to validate a single-character input
        print(text)  # debug-print the input character
        self.valid_int = ['1','2','3','4','5','6','7','8','9','0']  # list of valid numeric characters
        self.valid_symbols = ['+','-','/','x','.','%']  # list of valid operator/decimal characters
        if text in self.valid_int or text in self.valid_symbols:  # check if input is in allowed lists
            
            return True  # valid input -> return True
        else:
            return False  # invalid input -> return False

    def delete_btn(self, text_input):  # handler for delete/backspace button, accepts a TextInput widget
        curr_text_str = text_input.text  # get current text from the TextInput
        if len(curr_text_str) > 0:  # only modify if there is at least one character
            curr_text_str = curr_text_str[:-1]  # remove the last character from the string
            print(curr_text_str)  # debug-print the updated string
        text_input.text = curr_text_str  # put the updated string back into the TextInput

    def clear_btn(self, text_input):  # handler for clear/AC button, accepts a TextInput widget
        text_input.font_size = sp(50)  # reset the font size to the default large size
        text_input.text = ""  # clear the TextInput content

    def number_btn(self, text_input, number):  # handler for numeric button presses
        if self.text_validator(number):  # validate the pressed character before appending
            text_input.text += number  # append the valid number to the TextInput text
        else:
            return  # invalid input -> no action

    def check_decimal(self, last_segment):  # helper to check if a segment already contains a decimal
        if '.' in last_segment:  # if a decimal point is already present
            print("decimal error")  # debug-print decimal error
            return False  # indicate decimal cannot be added
        else:
            return True  # decimal can be added

        
    
    def operator_btn(self, text_input, operator):  # handler for operator and decimal button presses
        curr_text = text_input.text         # read current text from the TextInput        
        segments = re.split(r"[+\-x/%]", curr_text)  # split the current text into segments by operators
        last_segment = segments[-1]  # get the last numeric segment after splitting
        if self.text_validator(operator) and len(curr_text) > 0:  # only proceed if operator is valid and text not empty
            
            if curr_text[-1] in self.valid_symbols:  # if last character is already an operator
                if curr_text[-1] == '-':  # allow a minus if it is already a minus (handles negatives)
                    pass  # allow the minus to remain (no-op)
                else:
                    return  # disallow adding another operator after a non-minus operator
            if operator == '.':  # special handling when the operator is the decimal point
                if '.' in last_segment:  # if decimal already exists in the current number segment
                    print("decimal error")  # debug-print decimal error
                    return  # do not add another decimal
                else:
                    text_input.text += operator  # append decimal to the current input
            else:
                text_input.text += operator  # append other operators to the current input
        else:
            return  # invalid operator or empty input -> no action

    def result_btn(self, text_input):  # handler for the equals/result button
        print(type(text_input.text))  # debug-print the type of the TextInput content
        curr_text = text_input.text  # read the current expression string
        percentage_pattern = r"(\d+(?:\.\d+)?)%(\d+(?:\.\d+)?)"  # regex to match patterns like "a%b"
        match_percentage_pattern = re.findall(percentage_pattern,curr_text)  # find all percentage-based matches
        
        #print(first_percentage_item,second_percentage_item)
        if len(curr_text) > 0:  # only compute if there's something to evaluate
            
            if 'x' in curr_text:  # convert the custom multiplication symbol 'x' to Python '*'
                new_text = curr_text.replace('x','*')  # replace all 'x' with '*'
                curr_text = new_text  # update the expression string to use Python operator
            try:
                if match_percentage_pattern:  # if a percentage pattern was matched
                    first_percentage_item, second_percentage_item = match_percentage_pattern[0]  # unpack the first match
                    res = round(eval(first_percentage_item)*eval(second_percentage_item)/100,12)  # compute percentage result and round
                    if len(str(res)) > 8:  # if the result string is long, reduce font size
                        text_input.font_size = sp(20)  # set smaller font size
                    else:
                        text_input.font_size = sp(50)  # set default font size
                else:
                    res = round(eval(curr_text),12)  # evaluate the expression and round to 12 decimals
                    if len(str(res)) > 8:  # adjust font size for long results
                        text_input.font_size = sp(20)  # smaller font for long results
                    else:
                        text_input.font_size = sp(50)  # default font size for shorter results
                text_input.text = str(res)  # update the TextInput with the computed result
            except SyntaxError:  # catch syntax errors from eval
                return  # on syntax error, do nothing and return
                

class CalculatorApp(App):  # define the App class for the calculator
    def build(self):  # build method returns the root widget for the app
        return MainBoxLayout()  # instantiate and return the main layout

CalculatorApp().run()  # create the app instance and start the Kivy event loop
