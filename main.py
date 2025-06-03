from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv


def load_cred():
    # Load env variables
    load_dotenv()
    return {
        "email": os.getenv("EMAIL_ADDRESS"),
        "password": os.getenv("EMAIL_PASSWORD"),
        "smtp_server": os.getenv("SMTP_ADDRESS"),
        "to_email": os.getenv("TO_EMAIL", os.getenv("EMAIL_ADDRESS"))
    }


def fetch_price(url, header):

    response = requests.get(url, headers=header)
    # website = response.text
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        price_data = soup.find(class_="a-price-whole")
        price_fraction = soup.find(class_="a-price-fraction")
        title = soup.find(id="productTitle").getText().strip()

        if not price_data or price_fraction:
            raise ValueError("Price data not found.")

        price_string = f"{price_data.getText()}{price_fraction.getText()} "
        price_float = float(price_string.replace(",","").strip())
        return title, price_float
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None, None


def send_mail(title, price, url, credentials):
    # Send email notification.
    message = f"{title} is on flash sale for ${price}!"

    # ========================use env variable to send mail =====================#
    with smtplib.SMTP("smtp_server", port=587) as connection:
        connection.starttls()
        result = connection.login("email", "password")
        connection.sendmail(
            from_addr="email",
            to_addrs="to_email",
            msg=f"Subject:Amazon Price Drop Alert!\n\n{message}\n{url}".encode("utf-8")
        )
    print("✔️Message delivered successfully")


def track_price():
    url = input("Place the Link of Product!\n\n")
    buy_price = int(input("Lock the Price..\n\n"))

    credentials = load_cred()

    header = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
      }

    print(" Checking the product price")

    title, current_price = fetch_price(url, header)

    if title and current_price:
        print(f"📌 {title}\n💲 Current Price: ${current_price}")
        if current_price < buy_price:
            send_mail(title, current_price, url, credentials)
        else:
            print("📉 No price drop yet. Wait for the right time!")
    else:
        print("❌ Could not fetch price or title. Check the URL or network.")


if __name__ == "__main__":
    track_price()




