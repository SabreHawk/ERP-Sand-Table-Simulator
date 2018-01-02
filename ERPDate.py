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
        temp_year = self.__year + (self.__quarter + in_quarter) // self.__quarter_num
        temp_quarter = (self.__quarter + in_quarter) % self.__quarter_num
        if temp_quarter is 0:
            temp_year -= 1
            temp_quarter = 4
        return ERPDate(temp_year, temp_quarter)

    def display_info(self):
        print("<Object : ERPDate")
        print("Date : %s - %s>" % (str(self.__year), str(self.__quarter)))

    def to_string(self):
        return str(self.__year) + '-' + str(self.__quarter)
