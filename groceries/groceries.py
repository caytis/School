from abc import ABC

class Customer:
    def __init__(self, id, name, street, city, state, zip, phone, email):
        self.custid = id
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email
    
    def __str__(self):
        strr = "Customer ID #" + self.custid
        strr += ":\n" + self.name + ", ph. " + self.phone
        strr += ", email: " + self.email
        strr += self.street + "\n"
        strr += self.city + ", " + self.state + " " + self.zip + "\n\n"
        return strr

    def read_customers(FILE):
        global customers
        customers = {}
        with open(FILE) as file:
            for line in file:
                parts = line.split(",")
                if len(parts) == 0:
                    break
                customers[parts[0]] = Customer(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7])

class Item:
    def __init__(self, id, descrip, price):
        self.id = id
        self.descrip = descrip
        self.price = price

    def read_items(FILE):
        global items
        items = {}
        with open(FILE) as file:
            for line in file:
                parts = line.split(",")
                if len(parts) == 0:
                    break
                parts[2] = parts[2].strip()
                items[parts[0]] = Item(parts[0], parts[1], parts[2])

class LineItem:
    def __init__(self, id, qty):
        self.id = id
        self.qty = qty
        self.total = items[id].price

    def __gt__(self, other):
        if int(self.id) > int(other.id):
            return True
        return False

class Payment(ABC):
    def __init__(self, id, amount = 0.0):
        self.id = id
        self.amount = amount

class Credit(Payment):
    def __init__(self, id, expr, amount = 0.0):
        self.id = id
        self.expr = expr
        self.amount = amount

    def __str__(self):
        strr = "Amount: $" + str(round(self.amount, 2))
        strr += ", Paid by Credit card " + self.id + ", exp. " + self.expr
        return strr

class PayPal(Payment):
    def __init__(self, id, amount = 0.0):
        self.id = id
        self.amount = amount

    def __str__(self):
        strr = "Amount: $" + str(round(self.amount, 2))
        strr += ", Paid by Paypal ID: " + self.id
        return strr

class WireTransfer(Payment):
    def __init__(self, accid, bankid, amount = 0.0):
        self.accid = accid
        self.bankid = bankid
        self.amount = amount

    def __str__(self):
        strr = "Amount: $" + str(round(self.amount, 2))
        strr += ", Wire transfer, bank id: " + self.bankid + " account id: " + self.accid
        return strr

class Order:
    def __init__(self, custid, ordid, date, items, paym):
        self.ordid = ordid
        self.custid = custid
        self.paym = paym
        self.date = date
        self.items = items
    
    def total(self):
        for item in self.items:
            self.paym.amount += float(item.total) * float(item.qty)

    def print_order(self):
        strr = "===========================\n"
        strr += "Order #" + self.ordid
        strr += ", Date: " + self.date + "\n"
        self.total()
        strr += str(self.paym) + "\n"
        strr += str(customers[self.custid])
        strr += "Order Detail:\n"
        
        for item in self.items:
            strr += "        Item " + item.id
            strr += ": \"" + items[item.id].descrip
            strr += "\", " + item.qty.strip() + " @ " + item.total + "\n"
        print(strr)

    def read_orders(FILE):
        with open(FILE) as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                parts = lines[i].split(",")
                custid = parts[0]
                ordid = parts[1]
                date = parts[2]
                itemlist = []
                for item in parts[3:]:
                    pieces = item.split("-")
                    itemlist.append(LineItem(pieces[0], pieces[1]))
                itemlist.sort()
                i += 1
                pay = lines[i].split(",")
                paym = ""
                if pay[0] == "1":
                    paym = Credit(pay[1], pay[2])
                elif pay[0] == "2":
                    paym = PayPal(pay[1])
                else:
                    paym = WireTransfer(pay[1], pay[2])
                Order(custid, ordid, date, itemlist, paym).print_order()
                i += 1

if __name__ == '__main__':
    Customer.read_customers("customers.txt")
    Item.read_items("items.txt")
    Order.read_orders("orders.txt")
    
    # Now print orders to the file order_report.txt:
