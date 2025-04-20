import requests
import smtplib

# Step 1: Fetch vegetable data
url = "http://demo9153016.mockable.io/mydemi_data"
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    vegetable_data = response.json()
    print("Available vegetables and prices (per kg):")
    for veg, price in vegetable_data.items():
        print(f"{veg.capitalize()}: ${price}")

    selected_items = {}
    while True:
        your_vegie = input("\nEnter a vegetable you want (or type 'done' to finish): ").strip().lower()
        if your_vegie == 'done':
            break
        elif your_vegie in vegetable_data:
            try:
                quantity = float(input(f"How many kgs of {your_vegie}? "))
                if your_vegie in selected_items:
                    selected_items[your_vegie] += quantity
                else:
                    selected_items[your_vegie] = quantity
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print(f"Sorry, {your_vegie} is not available.")

    if selected_items:
        total_bill = 0
        bill_details = "\nYour Order Details:\n"

        for veg, qty in selected_items.items():
            price = vegetable_data[veg]
            cost = price * qty
            bill_details += f"{veg.capitalize()} - {qty} kg x ${price} = ${cost:.2f}\n"
            total_bill += cost

        gst_rate = 3
        gst_amount = (total_bill * gst_rate) / 100
        total = total_bill + gst_amount

        bill_details += f"\nOriginal price = ${total_bill:.2f}"
        bill_details += f"\nGST Rate(%) = {gst_rate}"
        bill_details += f"\nGST Amount = ${gst_amount:.2f}"
        bill_details += f"\nTotal Bill = ${total:.2f}"

        print("\n" + bill_details)

        # Step 2: Send email
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("am.vijay.796@gmail.com", "gvwk wuqc fnxe pdns")
            message = f"Subject: Your Vegetable Order Info\n\n{bill_details}"
            server.sendmail("am.vijay.796@gmail.com", "bvk1436@gmail.com", message)
            server.quit()
            print("Mail sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")
    else:
        print("No vegetables selected.")
else:
    print("Failed to fetch vegetable data.")