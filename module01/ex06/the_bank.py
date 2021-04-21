class Account:
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank:
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        if not (isinstance(origin, int) or isinstance(origin, str)):
            print("origin invalid")
            return
        if not (isinstance(dest, int) or isinstance(dest, str)):
            print("dest invalid")
            return
        """ if not (isinstance(origin, Account) and isinstance(dest, Account)):
            print("wrong origin or desination accounts")
            return """

        o = None
        d = None
        for ac in self.account:
            if (isinstance(origin, int) and ac.id == origin) or (isinstance(origin, str) and ac.name == origin):
                o = ac
            if (isinstance(dest, int) and ac.id == dest) or (isinstance(dest, str) and ac.name == dest):
                d = ac
        if not o:
            print("origin account does not exist")
            return False
        if not d:
            print("destination account does not exist")
            return
        """ if len(o.__dict__) % 2 == 0 or len(d.__dict__) % 2 == 0:
            print("dest or origin account are corrupted") """
        cnd1 = True  # is an attribute starting with b
        cnd2 = False  # is no attribute starting with zip or addr in origin account
        cnd3 = False  # is no attribute starting with zip or addr in dest account
        cnd4 = True  # is no attribute name, id and value
        for a in o.__dict__:
            if a[0] == 'b':
                cnd1 = False
            if a.startswith("zip") or a.startswith("addr"):
                cnd2 = True
        for a in d.__dict__:
            if a[0] == 'b':
                cnd1 = True 
            if a.startswith("zip") or a.startswith("addr"):
                cnd3 = True
        if ("name" not in o.__dict__) or ("id" not in o.__dict__) or ("value" not in o.__dict__):
            cnd4 = False
        if ("name" not in d.__dict__) or ("id" not in d.__dict__) or ("value" not in d.__dict__):
            cnd4 = False
        if not (cnd1 and cnd2 and cnd3 and cnd4):
            print("dest or origin account are corrupted zzzzzzzzzzz")
            return False
        if o.value < 0 or amount > o.value:
            print("insufficent sender account funds to make the transfer")
            return False
        o.value -= amount
        d.value += amount
        return True



a1 = Account("khalil", value=0, zip=None)
a1.transfer(6)
a2 = Account("god", value=0, addr=None)
a2.transfer(999999999999999999)
b = Bank()
b.add(a1)
b.add(a2)
b.transfer("god", "khalil", 9999999999)
print(a1.value)
print(a2.value)