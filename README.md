# Bestbuy
Masterschool's projects: create an engine for powering a tech equipment store like “Best Buy” 💻. Using the program you can list products and make an order.


![BestBuy](https://apollo-media.codio.com/media%2F1%2F284f269493493e2a92f2885570a14304-2176a4123b286acb.gif "BestBuy")

*A visual demo of the BestBuy 2.0 app in action, showcasing the interactive product menu and order placement.*

Demo:

   Store Menu
   ----------
1. List all active products in store
2. Show total available stock
3. Make an order
4. Quit
Please choose a number: 

<file name=1 path=bestbuy.2.0 – README.md — Editor 2># 🛍️ BestBuy 2.0 – Inventory Management Console App

*A visual demo of the BestBuy 2.0 app in action, showcasing the interactive product menu and order placement.*

A Python console application simulating a retail store inventory system inspired by Best Buy 🖥️📱🎧. 
This program allows users to view products, place orders, and track available quantities using different types of products and promotions.

---

## 🚀 Features

- 📦 Support for multiple product types:
  - Regular products
  - Limited purchase products
  - Non-stocked digital products
- 💸 Promotions engine:
  - 30% off
  - Second Half Price
  - Third One Free
- 🔄 Inventory tracking
- 🔒 Products automatically deactivate when quantity reaches 0
- ✅ Clean and modular architecture

---

## 📋 Store Menu

```
   Store Menu
   ----------
1. List all active products in store
2. Show total available stock
3. Make an order
4. Quit
```

---

## 🧪 Example Product List

```
1. MacBook Air M2, Price: $1450, Quantity: 100, Promotion: Second Half price!
2. Bose QuietComfort Earbuds, Price: $250, Quantity: 500, Promotion: Third One Free!
3. Google Pixel 7, Price: $500, Quantity: 250, Promotion: None
4. Windows License, Price: $125, Quantity: Unlimited, Promotion: 30% off!
5. Shipping, Price: $10, Limited to 1 per order!, Promotion: None
```

---

## 🧠 Technologies Used

- Python 3.x
- Object-Oriented Programming
- Command-line interface (CLI)

---

## 📦 Project Structure

- `main.py` – Starts the app and manages user interaction
- `products.py` – Defines all product types and promotion classes
- `store.py` – Inventory and order logic
- `test_product.py` – Unit tests for product behavior

---

## ✅ How to Run

```bash
python main.py
```

## 👨‍🎓 Developed as part of Masterschool’s Software Engineering Curriculum
