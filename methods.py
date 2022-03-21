import math
from variables import *

# ====================
#      DEFINITIONS :
# ====================


def TOTAL_BALANCE():
    list_of_questions = [questions_INCOME, questions_SPENDS]
    OUTCOME = int()
    for item in list_of_questions:
        for question in item:
            input_scanner = input(f'\n.. {question}\n> $')
            if item == questions_SPENDS:
                OUTCOME -= int(input_scanner)
            else:
                OUTCOME += int(input_scanner)
    return OUTCOME

# +++++++ ===== CONRTINUE HERE


# def saves():
#     INCOME = INCOME_BALANCE()
#     SPENDINGS = SPENDS_BALANCE()

#     print(f'\nYou have ${MONEY_LEFT} left')
#     user_choice = input('Would you rather save, invest or both? \n>> ')

#     if user_choice.lower() == 'invest':
#         INVEST = MONEY_LEFT * major_invest
#         SAVINGS = MONEY_LEFT * minor_invest
#         FUN = MONEY_LEFT * left_from_invest
#     elif user_choice.lower() == 'save':
#         SAVINGS = MONEY_LEFT * major_invest
#         INVEST = MONEY_LEFT * minor_invest
#     elif user_choice.lower() == 'both':
#         SAVINGS = INVEST = MONEY_LEFT * equal_invest
#         INVEST = MONEY_LEFT * minor_invest
#     else:
#         print('Enter "SAVE" OR "INVEST"')
#     FUN = MONEY_LEFT * left_from_invest

#     print(f"""
#     You can save ${CHILDREN} FOR THE CHILDREN each months
# You can save ${SAVINGS} in case of emmergency each months
#     You will need {time_to_back_up} months({time_to_back_up/month_per_year} years)to reach a 6 months safe capital of ${back_up_need}
# You can invest ${INVEST} per Months
# Each Months :
# You should invest ${bitcoin} in Bitcoin
# You should invest ${ethereum} in Ethereum
# You should invest ${BNB} in BNB
# You should invest ${another_crypto} in another crypto
# You should invest ${gold} in Gold
# You should invest ${formation} to improve yourself)
# You have ${FUN} left to enjoy
#     """)
