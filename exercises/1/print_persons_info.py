"""
***************************************************** Description ******************************************************
                                                                                                                       *
write a function that gets 3 lists as an argument                                                                      *
The first one is a list of people's names                                                                              *
The second is a list of boolean values that indicate whether the person knows Java                                     *
The third is a list of boolean values that indicate whether the person knows Python                                    *
for example charlotte knows Java but not Python                                                                        *
print all people names who knows java or python                                                                        *
                                                                                                                       *
input:                                                                                                                 *
    names = ["Oliver", "Charlotte", "William", "Sophia", "Benjamin", "Isabella", "Lucas", "Henry", "Evelyn", "Alex"]   *
    knows_java  =  [False, True, False, False, True, False, True, False, False, True]                                  *
    knows_python = [False, False, True, False, True, False, False, False, True, True]                                  *
                                                                                                                       *
output:                                                                                                                *
    Charlotte                                                                                                          *
    William                                                                                                            *
    Benjamin                                                                                                           *
    Lucas                                                                                                              *
    Evelyn                                                                                                             *
    Alex                                                                                                               *
                                                                                                                       *
***************************************************** good luck ********************************************************
"""

names = ["Oliver", "Charlotte", "William", "Sophia", "Benjamin", "Isabella", "Lucas", "Henry", "Evelyn", "Alexander"]
knows_java  =  [False, True, False, False, True, False, True, False, False, True]
knows_python = [False, False, True, False, True, False, False, False, True, True]


def get_smart_people(names, knows_java, knows_python):
    # write your code here
    pass


if __name__ == "__main__":
    get_smart_people(names, knows_java, knows_python)
