# BankAccount类：
# 属性：账户名，账号，余额
# 方法：显示余额，存钱，取钱


class BankAccount:
    def __init__(self, accountName, accountNo):
        self.accountName = accountName
        self.accountNo = accountNo
        self.remainder = 0.0

    def showRemainder(self):
        print("Your account has %s :" % self.remainder)

    def saveMoney(self, amount):
        self.remainder = self.remainder + amount
        print("You saved %s, now your account has : %s " %
              (amount, round(self.remainder, 2)))

    def getMoney(self, amount):
        if amount <= self.remainder:
            self.remainder = self.remainder - amount
            print('You got %s, now your account has: %s' %
                  (amount, round(self.remainder, 2)))
        else:
            print("Sorry, yout account is not enough!")


myBankAccount = BankAccount('Xujn', 62258810)
myBankAccount.showRemainder()
myBankAccount.saveMoney(1234.44)
myBankAccount.getMoney(122)



# InterestAccount 子类
# 属性：rate利率
# 方法：addInterest 计算利息并更新余额


class InterestAccount(BankAccount):
    def __init__(self, accountName, accountNo, rate):
        # super().__init__( accountName, accountNo) 与下面这句作用相同，注意
        # super的时候不需要传入self
        BankAccount.__init__(self, accountName, accountNo)
        self.rate = rate

    def addInterest(self):
        __interest = self.remainder * self.rate
        print('The rate is %s ,now you got %s:' %
              (self.rate, round(__interest, 2)))
        self.saveMoney(__interest)


myInterestAccount = InterestAccount('Xujn', 62258810, 0.043)
myInterestAccount.saveMoney(230009.22)
myInterestAccount.addInterest()
