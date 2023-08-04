class CC:

  def __init__(self):
    self.m_name = ""
    self.m_ccNUM = 0
    self.m_cvv = 0
    self.m_exMM = 0
    self.m_exYY = 0

  def prnNumber(self):
    x = 1000000000000
    a1 = self.m_ccNUM // x
    print(a1, end=" ")

    b = self.m_ccNUM % x
    a2 = b // 100000000
    print(f"{a2:04d}", end=" ")

    c = b % 100000000
    a3 = c // 10000
    print(f"{a3:04d}", end=" ")
    a4 = c % 10000
    print(f"{a4:04d}", end=" ")

  def set(self):
    self.m_ccNUM = 0
    self.m_cvv = 0
    self.m_name = None
    self.m_exMM = 0
    self.m_exYY = 0

  def isEmpty(self):
    if (self.m_name == None):
      return True
    else:
      return False

  def set(self, name, ccNum, cvv, exMM, exYY):
    if (validate(name, ccNum, cvv, exMM, exYY)):
      self.m_name = name
      self.m_cvv = cvv
      self.m_exMM = exMM
      self.m_exYY = exYY
      self.m_ccNUM = ccNum

  def read(self):
    ret = False
    tempName = ""
    tempCardNum = 0
    tempCvv = 0
    tempExMn = 0
    tempExYr = 0

    tempName = input("Card holder name: ")

    if tempName:
      try:
        tempCardNum = int(input("Credit card number: "))
        tempCvv = int(input("Card Verification Value (CVV): "))
        tempExMn, tempExYr = map(
          int,
          input("Expiry month and year (MM/YY): ").split("/"))

        self.set(tempName, tempCardNum, tempCvv, tempExMn, tempExYr)
        ret = True
      except ValueError:
        pass

    return ret

  def display(self, row=-1):
    if self.isEmpty():
      print("Invalid Credit Card Record")
    elif row > 0:
      tempName = self.m_name[:30]

      print(f"| {row:4} | {tempName:31} | ", end=" ")
      self.prnNumber()
      print(f" | {self.m_cvv:3} | {self.m_exMM:2}/{self.m_exYY:2} |")
    else:
      print("Name:", self.m_name)
      print("Creditcard No: ", end="")
      self.prnNumber()
      print()
      print("Card Verification Value:", self.m_cvv)
      print(f"Expiry Date: {self.m_exMM}/{self.m_exYY}")


#Validation of data
def validate(name, cardNo, cvv, exMM, exYY):
  if (name is not None and len(name) > 2
      and (cardNo >= 4000000000000000 and cardNo <= 4099999999999999)
      and (cvv > 99 and cvv < 1000) and (exMM >= 1 and exMM <= 12)
      and (exYY >= 22 and exYY <= 32)):
    return True
  else:
    print("Invalid Data")
    return False


print("Test Data")
cc = CC()
cc.set("Hubert Blaine", 4098765423457896, 123, 9, 23)
print("Valid credit card record: ")
cc.display()
print(
  "--------------------------------------------------------------------------------"
)

cc.set("Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr.",
       4066448300229357, 793, 5, 25)
cc.display()
print(
  "--------------------------------------------------------------------------------"
)

#Test by User Input
cd = CC()
cd.read()
print()
cd.display()

print()
print("Reading CSV Data From File")
c1 = CC()
file = open("csd.csv", "r")

print(
  "|      |                                 |                       |     | Expiry|"
)
print(
  "| Row  | Card holder name                | Credit card number    | CVV | MM/YY |"
)
print(
  "+------+---------------------------------+-----------------------+-----+-------+"
)
row = 1
for line in file:
  data = line.strip().split(',')
  if (len(data) == 5):
    name, no, cvv, expMon, expYear = data
    try:

      no = int(no)
      cvv = int(cvv)
      expMon = int(expMon)
      expYear = int(expYear)
      cc.set(name, no, cvv, expMon, expYear)
      cc.display(row)
      row += 1
    except ValueError:
      print("Error Reading file")
      pass
