class Pwdck:

    def __init__(self, pwd):
        self.pwd = pwd

    def check_letter(self):
        if self.pwd.isalpha() == 1:
            self.hasletter = True
        else:
            self.hasletter = False

    def check_number(self):
        if self.pwd.isdigit():
            self.hasnumber = True
        else:
            self.hasnumber = False