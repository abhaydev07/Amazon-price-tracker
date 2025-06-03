# 🛒 Amazon Price Tracker with Email Alerts

A Python-based tool to track the price of any Amazon product and send you an email alert when the price drops below your target.

---

## 🚀 Features

- ✅ Scrapes real-time product price and title from Amazon
- ✅ Sends alert emails using SMTP when the price is below your set threshold
- ✅ Secure credential management with `.env` file
- ✅ Clean, modular code using functions
- ✅ Optional daily automation via cron, Task Scheduler, or Python `schedule`

---

## 🧰 Tech Stack

- Python 3.7+
- BeautifulSoup (for HTML parsing)
- Requests (for HTTP requests)
- smtplib (for email)
- dotenv (for secure env variable loading)

---

## 📦 Installation & Setup

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/price-tracker.git
cd price-tracker
