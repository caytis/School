from abc import ABC

class Customer:
    def __init__(self, custid, name, street, city, state, zip, phone, email):
        self.custid = custid
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email
    
    def __str__(self):
        strr = "Customer ID #" + self.custid
        strr += ":\n" + self.name + ", ph.", self.phone
        strr += ", email:", self.email
        strr += "\n" + self.street + "\n"
        strr += self.city + ",", self.state, self.zip
        return strr

def read_customers(FILE):
    global customers
    customers = []
    with open(FILE) as file:
        for line in file:
            parts = line.split(",")
            if len(parts) == 0:
                break
            customers.append(Customer(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]))

# int find_cust_idx(int cust_id) {
#     for (int i = 0; i < customers.size(); ++i)
#         if (cust_id == customers[i].cust_id)
#             return i;
#     throw runtime_error("Customer not found")

class Item:
    def __init__(self, itemid, descrip, price):
        self.item_id = itemid
        self.descrip = descrip
        self.price = price


def read_items(FILE):
    items = []
    with open(FILE) as file:
        for line in file:
            parts = line.split(",")
            if (parts.size() == 0):
                break
            items.append(Item(parts[0], parts[1], parts[2]))
    return items

items = read_items("online groceries\items.txt")

# int find_item_idx(int item_id) {
#     for (int i = 0; i < items.size(); ++i)
#         if (item_id == items[i].item_id)
#             return i;
#     throw runtime_error("Item not found");
# }

class LineItem:
    def __init__(self, id, qty):
        self.id = id
        self.qty = qty
    # def sub_total():
    #     # int idx = find_item_idx(item_id)
    #     return items[idx].price * qty

class Payment(ABC):
    def __init__(self, id, amount = 0):
        self.id = id
        self.amount = amount

class Credit(Payment):
    def __init__(self, id, expr, amount = 0):
        super(self).__init__(id, amount)
        self.expr = expr

    def __str__(self):
        strr = "Amount: $" + self.amount
        strr += ", Paid by Credit card", id + ", exp.", self.exp
        return strr

class PayPal(Payment):
    def __init__(self, id, amount = 0):
        super(self).__init__(id, amount)

    def __str__(self):
        strr = "Amount: $" + self.amount
        strr += ", Paid by Paypal ID:", id
        return strr

class WireTransfer(Payment):
    def __init__(self, accid, bankid, amount = 0):
        super(self).__init__(accid, amount)
        self.bankid = bankid

    def __str__(self):
        strr = "Amount: $" + self.amount
        strr += ", Wire transfer, bank id:", self.bankid, "account id:", self.accid
        return strr

# payments = [] TODO

class Order:
    # vector<LineItem> line_items;
    # Payment* payment
    def __init__(self, ordid, date, custid, items, paym):
        # order_date(date), line_items(items)
        self.ordid = ordid
        self.custid = custid
        self.paym = paym
        self.date = date
        self.items = items
        # sort(line_items.begin(), line_items.end());
    
    # double total() const {
    #     return payment->amount;
    # }

    def print_order(self):
        # int index = find_cust_idx(cust_id); //I did this
        # Customer cust = customers.at(index);

        str = "===========================\n"
        str += "Order #" + self.ordid
        str += ", Date:", self.date + "\n"
        str += str(payments) + "\n\n"
        str += cust.print_detail() + "\n\n";
        str += "Order detail:\n";

        for item in line_items:
            # string descrip = items.at(find_item_idx(line_items.at(i).item_id)).description;
            # double temp = items.at(find_item_idx(line_items.at(i).item_id)).price;

            # stringstream stream;
            # stream << fixed << setprecision(2);
            # stream << temp;
            # string price = stream.str();

            # stringstream check(line_items.at(i).item_id);
            # string item_id;
            # check >> item_id;

            # stringstream chek(line_items.at(i).qty);
            # string qty;
            # chek >> qty;

            strr += "Item", item.id #TODO WHATS THIS???
            strr += ": \"" + item.descrip + "\", "
            strr += item.qty, "@", item.price + "\n"

        return str

# orders = [] TODO

void read_orders(const string& fname) {
    ifstream file(fname);
    string line;
    while (getline(file, line)) {
        // split line
        vector<string> parts = split(line, ',');
        if (parts.size() == 0) {
            break;
        }
        int cus_num = stoi(parts.at(0));
        int ord_num = stoi(parts.at(1));
        string date = parts.at(2);
    

        // Extract cust_id, order_id, and date

        // Create line item vector
        vector<LineItem> line_items; // I did not do this
        for (int i = 3; i < parts.size(); i++) { // I did this
            string item = parts.at(i);
            vector<string> two = split(item, '-');
            line_items.push_back(LineItem(stoi(two.at(0)), stoi(two.at(1))));
        }

        sort(begin(line_items), end(line_items)); //I did not do this

        getline(file, line); //every other (this is the second) // I did this
        if (parts.size() == 0) {
            break; //send to payment and have it return string
        }

        vector<string> parts2 = split(line, ',');
        if (parts2.size() == 0) {
            break;
        }
        stringstream strValue(parts2.at(0));
        char first;
        strValue >> first;
        string id;
        string exp;


        double total = 0.0; // I did this
        for (int i = 0; i < line_items.size(); i++) {
            total += line_items.at(i).sub_total();
        }

        Payment* pmt;
        switch (first)
        {
        case '1':
            id = parts2.at(1);
            exp = parts2.at(2);
            pmt = new Credit(id, exp, total);
            
            break;
        case '2':
            id = parts2.at(1);
            pmt = new Paypal(id, total);
            break;
        case '3':
            id = parts2.at(1);
            exp = parts2.at(2);
            pmt = new WireTransfer(id, exp, total);
            break;
        
        default:
            break;
        }

        orders.emplace_back(ord_num, date, cus_num, line_items, pmt); //given

        
    }
}

if __name__ == '__main__':
    Customer.read_customers("customers.txt")
    Item.read_items("items.txt")
    Order.read_orders("orders.txt")
    
    # Now print orders to the file order_report.txt:
