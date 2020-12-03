class Image:
    def __init__(self, id, city, txt, user):
        self.id = id
        self.city = city
        self.txt = txt
        self.user = user
        # self.rate = 0
        self.rates = []

    def check_txt(self):
        if len(self.txt) <= 140:
            self.txtvalid = True
        else:
            return "the text is invalid!"
    def rate_img(self, rate):
        if rate <= 5 and rate >= 0:
            self.rates.append(rate)
        # else:
        #     return "invalid rate!"
