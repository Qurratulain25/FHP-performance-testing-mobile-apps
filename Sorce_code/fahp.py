import sys
sys.path.append('E:/Qurratulain/FHP-performance-testing-mobile-apps')
from applications.ali_express import run_fahp_for_aliexpress
from applications.air_bnb import run_fahp_for_airbnb
from applications.easy_paisa import run_fahp_for_easy_paisa
from applications.daraz import run_fahp_for_daraz
from applications.github import run_fahp_for_github
from applications.payoneer import run_fahp_for_payoneer
from applications.ubl import run_fahp_for_ubl
from applications.uber import run_fahp_for_uber
from applications.food_panda import run_fahp_for_food_panda

# Call each application's FAHP process with print statements

print("Starting AliExpress FAHP")
run_fahp_for_aliexpress()   # AliExpress FAHP
print("AliExpress FAHP completed\n")

print("Starting Airbnb FAHP")
run_fahp_for_airbnb()      # Airbnb FAHP
print("Airbnb FAHP completed\n")

print("Starting Daraz FAHP")
run_fahp_for_daraz()       # Daraz FAHP
print("Daraz FAHP completed\n")

print("Starting Easypaisa FAHP")
run_fahp_for_easy_paisa()   # Easypaisa FAHP
print("Easypaisa FAHP completed\n")

print("Starting FoodPanda FAHP")
run_fahp_for_food_panda()   # FoodPanda FAHP
print("FoodPanda FAHP completed\n")

print("Starting Payoneer FAHP")
run_fahp_for_payoneer()    # Payoneer FAHP
print("Payoneer FAHP completed\n")

print("Starting GitHub FAHP")
run_fahp_for_github()      # GitHub FAHP
print("GitHub FAHP completed\n")

print("Starting Uber FAHP")
run_fahp_for_uber()        # Uber FAHP
print("Uber FAHP completed\n")

print("Starting UBL FAHP")
run_fahp_for_ubl()         # UBL FAHP
print("UBL FAHP completed\n")

print("All FAHP processes completed successfully.")

# Call each application's FAHP process
run_fahp_for_aliexpress()
run_fahp_for_airbnb()
run_fahp_for_daraz()
run_fahp_for_easy_paisa()
run_fahp_for_food_panda()
run_fahp_for_payoneer()
run_fahp_for_github()
run_fahp_for_ubl()
run_fahp_for_uber()
