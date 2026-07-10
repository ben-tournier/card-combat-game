import random

BOSS_LINES = ['The shadows themselves run in fear...', 
              'Cries of agony scrape along the walls...', 
              'A splitting headache of imeasurable pain...', 
              'Deep breaths hint at a near end, but for who...']

ELITE_LINES = ['An eerie presence is watching you...', 
               'The room ahead feels cold...', 
               'Do you really dare to wander ahead?...']

def floor_display(floor):
    if floor % 10 == 0:
        print("##################################################")
        print(f"##############  BOSS FLOOR {floor}  ###################")
        print("##################################################")

        print(f"\n \n {random.choice(BOSS_LINES)}")

    elif floor % 5 ==0:
        print("==========================================")
        print(f"=======         ELITE FLOOR {floor}        =====")
        print("==========================================")

        print(f"\n \n {random.choice(ELITE_LINES)}")

    else:
        print("==========================================")
        print(f"                 FLOOR {floor}")
        print("==========================================")
