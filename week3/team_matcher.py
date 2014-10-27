import requests
import random


def get_request():
    r = requests.get("https://hackbulgaria.com/api/students/", verify=False)
    return r


def find_courses():
    students = get_request()
    list_for_courses = []
    for courses in range(len(students.json())):
        for name in range(len(students.json()[courses]["courses"])):
            list_for_courses.append(students.json()[courses]["courses"][name]["name"])
    list_of_courses = sorted(list(set(list_for_courses)))
    return list_of_courses


def print_list_of_courses():
    print("Here are the courses:")
    for index, name_of_course in enumerate(find_courses()):
        print("[" + str(index) + "] " + name_of_course)


def list_of_courses():
    table_of_courses = {}
    for index, name_of_course in enumerate(find_courses()):
        table_of_courses[index] = name_of_course
    return table_of_courses


def match_teams(course_id, team_size, group_time):
    students = get_request()
    list_of_names = []
    courses = list_of_courses()
    for course in range(len(students.json())):
        for name in range(len(students.json()[course]["courses"])):
            names_in_course = students.json()[course]["courses"][name]["name"]
            group_in_course = students.json()[course]["courses"][name]["group"]
            available = students.json()[course]["available"]
            if courses[course_id] == names_in_course and group_in_course == group_time:
                if available is True:
                    list_of_names.append(students.json()[course]["name"])

    while len(list_of_names) != 0:
        for i in range(team_size):
            if len(list_of_names) > 0:
                random_student = random.randrange(len(list_of_names))
                print(list_of_names[random_student])
                list_of_names.remove(list_of_names[random_student])
        print(10 * "-")


def team_match():
    print("Hello, you can use one the the following commands:")
    print("list_courses - this lists all the courses that are available now.")
    print("exit - to quit the program")
    print("match_teams <course_id>, <team_size>, <group_time>")
    while True:
        command = input("enter command: ")
        list = command.split()
        if command == "list_courses":
            print_list_of_courses()
        if list[0] == "match_teams":
            match_teams(int(list[1]), int(list[2]), int(list[3]))
        if command == "exit":
            break


team_match()
