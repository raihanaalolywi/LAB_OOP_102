class BankAccount:

    def __init__(self, account_holder, initial_balance=0):
        # احفظ لي اسم الحساب  بشكل خاص __    هنا ال private
        self.__account_holder = account_holder
# اتاكد من الرصيد باانه ليس سالبا  وبداته  من الصفر لان
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance
    def withdraw(self, amount):
        # التاكد من ان الرقم موجب 
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.__balance:
            raise Exception("Insufficient funds.") 
 # اخصم المبلغ بعد العملية
        self.__balance -= amount

        # عملية الارجاع 
        return self.__balance

    # دالة لإرجاع الرصيد الحالي في الحساب
    def get_balance(self):
        return self.__balance

    # دالة لإرجاع اسم صاحب الحساب
    def get_account_holder(self):
        return self.__account_holder
