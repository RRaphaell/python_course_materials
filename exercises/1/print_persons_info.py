"""
მოცემული გაქვთ სამი ლისტი
პირველი (names) არის სადაც წერია ადამიანის სახელები
მეორე (knows_java) სადაც წერია boolean ტიპები ანუ True ან False იმის და მიხედვით იცის თუ არა ჯავა
მესამე (knows_python) სადაც წერია boolean ტიპები ანუ True ან False იმის და მიხედვით იცის თუ არა პითონი
ინდექსით შეგიძლიათ გაარკვიოთ რომელიმე ადამიანმა იცის თუ არა პითონი ან ჯავა მაგალითად მე3 ინდექსზე მყოფმა ადამიანმა
იცის ჯავა თუ knows_java ლისტში მე3 ინდექსზე წერია True
დაპეჭდეთ ისეთი ადამიანის სახელები რომლებმაც იციან ან ჯავა ან პითონი ანუ ერთი მაინც ან ორივე

input:
    names = ["Oliver", "Charlotte", "William", "Sophia", "Benjamin", "Isabella", "Lucas", "Henry", "Evelyn", "Alexander"]
    knows_java  =  [False, True, False, False, True, False, True, False, False, True]
    knows_python = [False, False, True, False, True, False, False, False, True, True]

output:
    Charlotte
    William
    Benjamin
    Lucas
    Evelyn
    Alexander

*********************************** წარმატებები ***********************************
"""

names = ["Oliver", "Charlotte", "William", "Sophia", "Benjamin", "Isabella", "Lucas", "Henry", "Evelyn", "Alexander"]
knows_java  =  [False, True, False, False, True, False, True, False, False, True]
knows_python = [False, False, True, False, True, False, False, False, True, True]


def get_smart_people(names, knows_java, knows_python):
    # write your code here
    pass


if __name__ == "__main__":
    get_smart_people(names, knows_java, knows_python)
