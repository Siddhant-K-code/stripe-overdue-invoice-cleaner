import stripe
import time

# Set your secret key
stripe.api_key = "your_stripe_secret_key"

# List of invoice IDs to be voided
invoice_ids = [
    "inv_1JkZtyG8NAbcdEF1",
    "inv_1JkZtyG8NAbcdEF2",
    # Add more invoice IDs here
]

def void_invoices(invoice_ids):
    for invoice_id in invoice_ids:
        try:
            # Retrieve the invoice
            invoice = stripe.Invoice.retrieve(invoice_id)

            # Check if the invoice is overdue
            if (
                invoice.status == "open"
                and invoice.due_date
                and invoice.due_date < time.time()
            ):
                # Void the invoice
                voided_invoice = stripe.Invoice.void_invoice(invoice_id)
                print(f"Voided invoice {invoice_id}: {voided_invoice.status}")
            else:
                print(f"Invoice {invoice_id} is not overdue or already closed/voided")
        except stripe.error.StripeError as e:
            print(f"Failed to void invoice {invoice_id}: {e.user_message}")


# Execute the function
void_invoices(invoice_ids)
