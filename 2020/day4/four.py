import re

def readfile(path):

    textfile = open(path, "r")
    persons = []

    lines = textfile.readlines()
    person = Person()
    for line in lines:
        if line.strip() == "":
            persons.append(person)
            person = Person()
            continue
        line = line.split(" ")
        for div in line:
            div = div.split(":")
            div[1] = div[1].strip("\n")
            div[1] = div[1].strip(" ")
            if div[0] == "byr":
                person.byr = div[1]
            if div[0] == "iyr":
                person.iyr = div[1]
            if div[0] == "eyr":
                person.eyr = div[1]
            if div[0] == "hgt":
                person.hgt = div[1]
            if div[0] == "hcl":
                person.hcl = div[1]
            if div[0] == "ecl":
                person.ecl = div[1]
            if div[0] == "pid":
                person.pid = div[1]
            if div[0] == "cid":
                person.cid = div[1]
    persons.append(person)

    return persons


def validation1(persons):
    validated = 0
    for person in persons:
        if person.byr == 0:
            continue
        if person.iyr == 0:
            continue
        if person.eyr == 0:
            continue
        if person.hgt == 0:
            continue
        if person.hcl == 0:
            continue
        if person.ecl == 0:
            continue
        if person.pid == 0:
            continue
        validated += 1
    return validated


def validation2(persons):
    validated = 0
    for person in persons:
        if not 1920 <= int(person.byr) <= 2002:  # check if byr is in acceptable area
            continue
        if not 2010 <= int(person.iyr) <= 2020:  # check if iyr is in acceptable area
            continue
        if not 2020 <= int(person.eyr) <= 2030:  # check if eyr is in acceptable area
            continue
        if person.hgt == 0:
            continue
        if person.hgt[-2:] == "cm":  # Check if cm hgt acceptable
            if not 150 <= int(person.hgt[:-2]) <= 193:
                continue
        elif person.hgt[-2:] == "in":  # Check if in hgt acceptable
            if not 59 <= int(person.hgt[:-2]) <= 76:
                continue
        else:  # If neither cm or in hgt not acceptable
            continue
        if not (person.hcl and re.search('^#+[a-f0-9]{6}$', person.hcl)):
            continue
        if not (person.ecl and re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', person.ecl)):
            continue
        if not (person.pid and re.search('^[0-9]{9}$', person.pid)):
            continue
        validated += 1
    return validated


class Person:
    byr = 0
    iyr = 0
    eyr = 0
    hgt = 0
    hcl = 0
    ecl = 0
    pid = 0
    cid = 0


print(validation1(readfile("4.in")))
print(validation2(readfile("4.in")))