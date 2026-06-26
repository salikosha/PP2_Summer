import re

text = open("./Practice5/row.txt", "r", encoding="utf-8").read()

# 1. Extract all prices from the receipt
prices = re.findall(r'\d[\d ]*,\d{2}', text)

print("All prices:")
for price in prices:
    print(price)

# --------------------------------------------------

# 2. Find all product names
products = re.findall(
    r'\d+\.\s*\n(.*?)\n\d+,\d{3}\s*x',
    text,
    re.DOTALL
)

print("\nProduct names:")
for product in products:
    print(product.replace("\n", " ").strip())

# --------------------------------------------------

# 3. Calculate total amount
total = re.search(r'ИТОГО:\s*\n([\d ]+,\d{2})', text)

if total:
    print("\nTotal amount:")
    print(total.group(1))

# --------------------------------------------------

# 4. Extract date and time information
datetime = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})', text)

if datetime:
    print("\nDate:", datetime.group(1))
    print("Time:", datetime.group(2))

# --------------------------------------------------

# 5. Find payment method
payment = re.search(r'(Банковская карта|Наличные)', text)

if payment:
    print("\nPayment method:")
    print(payment.group())

# --------------------------------------------------

# 6. Create structured output
print("\n-STRUCTURED OUTPUT-")

print("Date:", datetime.group(1))
print("Time:", datetime.group(2))
print("Payment method:", payment.group())
print("Total:", total.group(1))

print("\nProducts:")

for product, price in zip(products, prices):
    print(f"- {product.replace(chr(10), ' ').strip()} : {price}")