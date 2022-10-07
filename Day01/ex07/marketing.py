import sys

def lltyprgrm_handler(clients, participants):
    print(list(set(clients) - set(participants)))
    return

def potclnts_handler(clients, participants):
    print(list(set(participants) - set(clients)))
    return

def ccntr_handler(clients, recipients, participants):
    part_pls_clnts = clients
    for i in participants:
        part_pls_clnts.append(i)
    print(list(set(part_pls_clnts) - set(recipients)))
    return

def main():
    if len(sys.argv) != 2:
        raise Exception("Wrang quantity of args!")
    tasks = ["call_center", "potential_clients", "loyalty_program"]
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
                'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
                'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
                    'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org',
                    'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    if sys.argv[1] == tasks[0]:
        ccntr_handler(clients, recipients, participants)
    elif sys.argv[1] == tasks[1]:
        potclnts_handler(clients, participants)
    elif sys.argv[1] == tasks[2]:
        lltyprgrm_handler(clients, participants)
    else:
        raise Exception("Wrong task")


    return

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(type(err).__name__, err, sep=': ')