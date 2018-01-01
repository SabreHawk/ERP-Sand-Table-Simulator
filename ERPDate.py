class ERPDate(object):

    def __init__(self, in_year, in_quarter):
        self.__quarter_num = 4
        self.__year = in_year
        self.__quarter = in_quarter
        self.__check_quarter()

    def __check_quarter(self):
        if self.__quarter > 4:
            self.__quarter = 4
        elif self.__quarter < 1:
            self.__quarter = 1

    def add_date(self, in_quarter):
        self.__year += in_quarter // self.__quarter_num
        self.__quarter += in_quarter % self.__quarter_num
        return ERPDate(self.__year, self.__quarter)

    def display_info(self):
        print("<Object : ERPDate")
        print("Date : %s - %s>" % self.__year,self.__quarter)