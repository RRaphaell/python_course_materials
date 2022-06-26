"""
************************************************ Description ****************************************************
                                                                                                                *
write a function calculate_grade that takes student information as a list of dictionaries                       *
In each dictionary, we have each student's name, assignment, tests and lab scores                               *
You should calculate the average score for each student by using the following proportions                      *
10 % for assignments                                                                                            *
20 % for labs                                                                                                   *
70 % for tests                                                                                                  *
                                                                                                                *
then map the average score to the final letter grade as follows:                                                *
1. score >= 90 : "A"                                                                                            *
2. score >= 80 : "B"                                                                                            *
3. score >= 70 : "C"                                                                                            *
4. score >= 60 : "D"                                                                                            *
5. score >= 50 : "E"                                                                                            *
5. score >= 50 : "F"                                                                                            *
                                                                                                                *
at the end return list of dictionaries where we have the name and the final letter grade                        *
                                                                                                                *
argument:                                                                                                       *
    [{"name": "Jack Frost",    "assignment": [80, 50, 40, 20], "test": [75, 75], "lab": [78.20, 77.20]},        *
     {"name": "James Potter",  "assignment": [82, 56, 44, 30], "test": [90, 80], "lab": [87.90, 78.72]}         *
     {"name": "Dylan Rhodes",  "assignment": [87, 82, 93, 89], "test": [98, 87], "lab": [92, 94]}               *
     {"name": "Jessica Stone", "assignment": [67, 55, 77, 21], "test": [40, 50], "lab": [59, 44.56]}            *
output:                                                                                                         *
    [{"name": "Jack Frost", score: C},                                                                          *
    {"name": "James Potter", score: B},                                                                         *
    {"name": "Dylan Rhodes", score: A},                                                                         *
    {"name": "Jessica Stone", score: E}]                                                                        *
                                                                                                                *
here is an example how to calculate Jack's final score                                                          *
score = (80+50+40+20)÷4×0,1 + (75+75)÷2×0,7 + (78.2+77.2)÷2×0,2 = 72,79                                         *
since 72,79 > 70 then the final letter grade is C                                                               *
                                                                                                                *
************************************************* good luck *****************************************************
"""


def calculate_grade():  # fill arguments
    # write your code here
    pass
