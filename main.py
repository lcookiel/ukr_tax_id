from datetime import date
import math


def birthcode(birth_date):
    birth_date = birth_date.split("-")
    birth_date = date(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
    delta = birth_date - date(1899, 12, 31)
    return delta.days

# 3726903919
def control_digit(taxid):
    control_sum = int(taxid[0])*(-1) + int(taxid[1])*5 + int(taxid[2])*7 + int(taxid[3])*9 + int(taxid[4])*4 + int(taxid[5])*6 + int(taxid[6])*10 + int(taxid[7])*5 + int(taxid[8])*7
    # control_digit = control_sum - (11 * math.floor(control_sum/11))
    # print(control_sum)
    control_digit = (control_sum%11)%10
    return str(control_digit)


def possible_taxid(birthcode, sex):
    m = [1, 3, 5, 7, 9]
    f = [0, 2, 4, 6, 8]
    possible_taxid = []
    if sex == "m":
        for i in range(0, 1000):
            for n in m:
                taxid = str(birthcode) + (3 - len(str(i))) * "0" + str(i) + str(n)
                taxid = str(taxid) + control_digit(taxid)
                possible_taxid.append(taxid)
    elif sex == "f":
        for i in range(0, 1000):
            for n in f:
                taxid = str(birthcode) + (3 - len(str(i))) * "0" + str(i) + str(n)
                taxid = str(taxid) + control_digit(taxid)
                possible_taxid.append(taxid)
    else:
        pass
    return possible_taxid


if __name__ == '__main__':
    birth_date = input("Date of birth (e.g. 1999-12-31): ")
    sex = input("Sex (m/f): ").lower()
    # first 5 digits of tax id
    birthcode = birthcode(birth_date)
    possible_taxid = possible_taxid(birthcode, sex)
    for id in possible_taxid:
        print(id)
    # print(control_digit("372690391"))
