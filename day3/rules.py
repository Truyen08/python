#rule_01: the first character: letter of an underscore
"""

    _var = 1    #valid
    var = 2     #valid
    45home = 2 # invalid variable
"""


#rule_02: after of them (rule01) is composed of letters, digits or underscores

#rule_03: identifiers should not be the same
'''
myVar = 19
MyVar = 2024
--> it will cause confusion
'''

#rule_04: keyworks cannot be used as indentifiers
# eg: if, for, while, ..... 

#rule_05: indentifiers should be meaningful for understand
# person_age = 21

#rule_06: It should be nerther too long nor too short
'''
list_name = ....    # good 
list_name_of_my_company = ....  # too long 
lt = ...    # too short
'''

# --> NOTE: difference between indentifier and variable:
'''
    identifier: use to define the name object. it doesn't have a datatype
    variable:   use to store values and data in program. it have a datatpye
'''
