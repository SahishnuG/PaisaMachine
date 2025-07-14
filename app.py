from flask import Flask, render_template, request
import razorpay
import random

app = Flask(__name__)

# Replace with your Razorpay test keys
RAZORPAY_KEY_ID = 'rzp_test_yourkeyid'
RAZORPAY_KEY_SECRET = 'yourkeysecret'

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pay', methods=['POST'])
def pay():
    amount = int(request.form['amount']) * 100  # convert to paise
    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1,
        "receipt": f"receipt_{random.randint(1000, 9999)}"
    })
    return render_template('pay.html', 
                           key=RAZORPAY_KEY_ID,
                           order=payment,
                           amount=amount)

@app.route('/success', methods=['POST'])
def success():
    return "Payment successful! ✅"

if __name__ == '__main__':
    app.run(debug=True)
