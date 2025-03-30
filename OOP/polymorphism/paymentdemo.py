# PaymentDemo
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")
    
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")

class BankTransferPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount:.2f}")

def checkout(total_amount, payment_method):
    print(f"Total amount to be paid: ${total_amount:.2f}")
    payment_method.process_payment(total_amount)

def main():
    total_amount = 1000.50
    payment_method = CreditCardPayment()
    checkout(total_amount, payment_method)
    
    payment_method = BankTransferPayment()
    checkout(total_amount, payment_method)

if __name__ == "__main__":
    main()