import threading 
# import time
import json

# def printNumbers():
#     for i in range(1,6):
#         print(i)
#         time.sleep(1)

# def printLetters():
#     for i in "ABCDE":
#         print(i)
#         time.sleep(1)

# if __name__ == "__main__":
#     t1 = threading.Thread(target=printNumbers)
#     t2 = threading.Thread(target=printLetters)

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join() 


#     print("Program sonlandı")


def add_customer(database, name, email, phone):
    new_customer = {
        "name": name,
        "email": email,
        "phone": phone
    }
    with threading.Lock():

        try:
            with open(database, 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            data = []

        data.append(new_customer)

        with open(database, 'w') as file:
            json.dump(data, file)
    

if __name__ == "__main__":
    DATABASE_FILE = "customer.json"

    threads = []
    for i in range(5):
        name = f"Customer {i}"
        email = f"Customer_{i}@example.com"
        phone = f"000-123-456{i:02}"

        thread = threading.Thread(target=add_customer, args=(DATABASE_FILE, name, email, phone))

        threads.append(thread)
    for thread in threads:
        thread.start()
        thread.join()

    with open(DATABASE_FILE, 'r') as file:
        all_customers = json.load(file)
        print("Customer Database: ")

        for customer in all_customers:
                print(f"Name: {customer['name']}, Email: {customer['email']}, Phone: {customer['phone']}")





