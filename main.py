#  اعمل استيراد للكلاس حقي من الملف الثاني 
from bank_account import BankAccount

try: # ابتداها با  try  
    # انشاء حساب بااسم ايلا 
    account1 = BankAccount("ella",1000)
    print("Account Holder:", account1.get_account_holder())
    print("Current Balance:", account1.get_balance())
 # إاودع بحسابي ال 500 
    print("\nDepositing 500...")
    account1.deposit(500)
    print("Balance after deposit:", account1.get_balance())
# سعملية السحب
    print("\nWithdrawing 300...")
    account1.withdraw(300)
    print("Balance after withdrawal:", account1.get_balance())
    print("\nTrying to withdraw 2000...")
    account1.withdraw(2000)

# التقاط أي خطأ (Exception) يحدث أثناء العمليات وانهيها
except Exception as e:
    print("Error:", e)
