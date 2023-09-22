from abc import ABC, abstractmethod

class Customer:
    def __init__(self, cust_id, name, street, city, state, zip, phone, email):
        int = cust_id
        string = name
        string = street
        string = city
        string = state
        string = zip
        string = phone
        string = email
    
    def __str__(self):
        strr = "Customer ID #" + self.cust_id
        strr += ":\n" + self.name + ", ph.", self.phone
        strr += ", email:", self.email
        strr += "\n" + self.street + "\n"
        strr += self.city + ",", self.state, self.zip
        return strr

def read_customers(FILE):
    customers = []
    with open(FILE) as file:
        for line in file:
            parts = line.split(",")
            if len(parts) == 0:
                break
            customers.append(Customer(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]))
    return customers

customers = read_customers("online groceries\customers.txt")

# int find_cust_idx(int cust_id) {
#     for (int i = 0; i < customers.size(); ++i)
#         if (cust_id == customers[i].cust_id)
#             return i;
#     throw runtime_error("Customer not found")

class Item:
    def __init__(self, item_id, descrip, price):
        self.item_id = item_id
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

int find_item_idx(int item_id) {
    for (int i = 0; i < items.size(); ++i)
        if (item_id == items[i].item_id)
            return i;
    throw runtime_error("Item not found");
}

class LineItem {
    int item_id;
    int qty;
    friend class Order;
public:
    LineItem(int id, int q) {
        item_id = id;
        qty = q;
    }
    double sub_total() const {
        int idx = find_item_idx(item_id);
        return items[idx].price * qty;
    }
    friend bool operator<(const LineItem& item1, const LineItem& item2) {
        return item1.item_id < item2.item_id

class Payment(ABC):
    amount = 0
    friend class Order
public:
    Payment() = default;
    virtual ~Payment() = default;
    virtual string print_detail() const = 0;
};

class Credit : public Payment { // I did this
    string id;
    string exp;
    double amount;
public:
    ~Credit() override{};
    Credit(string nid, string expr, double amoun) {
        id = nid;
        exp = expr;
        amount = amoun;
    }
    string print_detail() const override {
        stringstream stream;
        stream << fixed << setprecision(2);
        stream << amount;
        string sAmount = stream.str();

        string str = "Amount: $" + sAmount + ", ";
        str += "Paid by Credit card " + id + ", exp. " + exp;
        return str;
    }
};

class Paypal : public Payment { // I did this
    string id;
    double amount;
public:
    ~Paypal() override{};
    Paypal(string nid, double amoun) {
        id = nid;
        amount = amoun;
    }
    string print_detail() const override {
        stringstream stream;
        stream << fixed << setprecision(2);
        stream << amount;
        string sAmount = stream.str();

        string str = "Amount: $" + sAmount + ", ";
        str += "Paid by Paypal " + id;
        return str;
    }
};

class WireTransfer : public Payment { // I did this
    string bank;
    string account;
    double amount;
public:
    ~WireTransfer() override{};
    WireTransfer(string ban, string accoun, double amoun) {
        bank = ban;
        account = accoun;
        amount = amoun;
    }
    string print_detail() const override {
        stringstream stream;
        stream << fixed << setprecision(2);
        stream << amount;
        string sAmount = stream.str();

        string str = "Amount: $" + sAmount + ", ";
        str += "Wire transfer, bank id: " + bank + " account id: " + account;
        return str;
    }
};

///////////////
// Order code /
///////////////
class Order {
    int order_id;
    string order_date;
    int cust_id;
    vector<LineItem> line_items;
    Payment* payment;
public:
    Order(int id, const string& date, int c_id, const vector<LineItem>& items, Payment* p) // I didn't do this
    : order_date(date), line_items(items) {
        order_id = id;
        cust_id = c_id;
        payment = p;
        sort(line_items.begin(), line_items.end());
    }
    ~Order() {
        delete payment;
    }
    double total() const {
        return payment->amount;
    }
    string print_order() const {
        int index = find_cust_idx(cust_id); //I did this
        Customer cust = customers.at(index);
        string str;
        stringstream bValue(order_id);
        string orderid;
        bValue >> orderid;

        str += "===========================\n";
        str += "Order #" + orderid;
        str += ", Date: " + order_date + "\n";
        str += payment->print_detail() + "\n\n";
        str += cust.print_detail() + "\n\n";
        str += "Order detail:\n";

        for (int i = 0; i < line_items.size(); i++) {
            string descrip = items.at(find_item_idx(line_items.at(i).item_id)).description;
            double temp = items.at(find_item_idx(line_items.at(i).item_id)).price;

            stringstream stream;
            stream << fixed << setprecision(2);
            stream << temp;
            string price = stream.str();

            stringstream check(line_items.at(i).item_id);
            string item_id;
            check >> item_id;

            stringstream chek(line_items.at(i).qty);
            string qty;
            chek >> qty;

            str += "Item " + item_id;
            str += ": \"" + descrip + "\", ";
            str += qty + " @ " + price + "\n";
        }

        return str;
    }
};
list<Order> orders;

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
