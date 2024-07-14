# 🧹 Stripe Overdue Invoice Cleaner

Welcome to the Stripe Overdue Invoice Cleaner! This handy Python script helps you automatically void those pesky overdue invoices with ease, saving you time and effort.

## ❓ Why Void Invoices?

Voiding invoices is a crucial task for maintaining clean and accurate financial records. Here are some cases where voiding invoices can help:

- **Avoiding Confusion**: Overdue invoices can clutter your financial records and lead to confusion during audits or bookkeeping.
- **Preventing Unintentional Payments**: Voiding overdue invoices ensures that customers do not accidentally pay old invoices that are no longer valid.
- **Improving Cash Flow Management**: By voiding overdue invoices, you can focus on collecting payments for current invoices, thereby improving your cash flow management.
- **Maintaining Customer Relations**: Clearing up old, unresolved invoices can help maintain a good customer relationship by avoiding disputes over outdated charges.

## 🚀 Features

- **Void Overdue Invoices**: Automatically voids overdue invoices based on their status and due date.
- **Error Handling**: Catches and displays errors for smooth execution.
- **Easy Setup**: Just plug in your Stripe API key and a list of invoice IDs, and you're good to go!

## 📋 Prerequisites

- Python 3.x
- Stripe account with API key

## 📦 Installation

First, you'll need to install the Stripe Python library. Open your terminal and run:

```bash
pip install stripe
```

## 🛠️ Usage

1. **Set Up Your API Key**: Replace `"your_stripe_secret_key"` with your actual Stripe secret key.
2. **Add Invoice IDs**: Populate the `invoice_ids` list with the IDs of the invoices you want to void.
3. **Run the Script**: Execute the script in your Python environment.

### 📄 Script

Here's the [script](./void_invoices.py) you need.

### Running the Script

To run the script, use the following command in your terminal:

```bash
python void_invoices.py
```

## 🤔 Need Help?

If you run into any issues or have questions, feel free to open an issue or reach out via [Twitter](https://x.com/siddhant_K_code) or [LinkedIn](https://www.linkedin.com/in/siddhantkhare24/).
