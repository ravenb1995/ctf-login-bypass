# 🧩 CTF Challenge: Simple Web Login Bypass

## 📝 Description
Your mission is to bypass a vulnerable login page using SQL Injection. The goal is to access the admin dashboard without valid credentials.

## 🔍 Target
- Web form: `login.html`
- Username: `admin`
- Password: Any input

## 🧠 Hint
Try injecting `' OR '1'='1` in the password field.

## 🎯 Goal
See the text: **Welcome, admin!**

## 🚀 Start the Docker container and visit:
http://localhost:5000

## 🔓 Flag
The flag will be shown on the dashboard upon successful login.
