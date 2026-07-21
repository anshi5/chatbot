import random

chatbot = {
    ("hii", "hello", "hey", "good morning", "good evening"): [
        "hello! how can i assist you today",
        "how may i help you ?",
        "hey! welcome to my chatbot",
        "hey what can i do for you?"
    ],

    ("order", "track order", "where is my order", "why is my order delay"): [
        "sure! can you provide me with your order number?",
        "you can check your order status from the 'my order' section",
        "of course! please share your order details!",
        "Your order is out for delivery"
    ],

    ("delivery", "when will my order arrive", "track delivery", "delivery status"): [
        "Your order is on the way!",
        "Expected delivery is within 2-3 business days",
        "Please check the 'delivery status' in your account",
        "Can you share your order number to confirm delivery?"
    ],

    ("refund", "money back", "return money", "refund status"): [
        "Please provide your order number to initiate refund",
        "Refunds are processed within 5-7 business days",
        "You can request a refund from the 'my orders' section",
        "Refund has been initiated successfully"
    ],

    ("return", "replace", "exchange", "wrong size", "return product"): [
        "Sure! please share your order details",
        "You can request a return/replacement from 'my orders'",
        "Return pickup will be scheduled soon",
        "Replacement order will be shipped once we receive the returned item"
    ],

    ("offer", "discount", "sale", "coupon", "promo code"): [
        "Check out the latest offers in the 'offers' section",
        "Apply coupon codes at checkout for discounts",
        "We have exciting deals running right now!",
        "Would you like me to share current promo codes?"
    ],

    ("cancel", "cancel order", "stop order", "abort order"): [
        "Please share your order number to cancel",
        "You can cancel your order from 'my orders' before it is shipped",
        "Order cancellation request has been received",
        "Your order has been cancelled successfully"
    ],

    ("wrong product", "damaged product", "broken item", "incorrect item"): [
        "Sorry for the inconvenience! Please share your order details",
        "You can raise a complaint from 'my orders'",
        "We will arrange a replacement for the damaged product",
        "Our support team will contact you shortly"
    ],

    ("payment", "transaction", "billing", "payment failed", "payment issue"): [
        "Please provide your order ID to check payment status",
        "You can view payment history in the 'payments' section",
        "Payment failed — please try again",
        "Your payment has been received successfully"
    ],

    ("feedback", "review", "suggestion", "complaint", "rate service"): [
        "We value your feedback! Please share your thoughts",
        "You can submit feedback in the 'feedback' section",
        "Thanks for helping us improve!",
        "Your feedback has been recorded"
    ],

    ("bye", "exit", "goodbye", "quit"): [
        "Thank you for visiting! Have a great day",
        "Goodbye! Looking forward to serving you again",
        "Take care! See you soon",
        "Exiting now — thanks for your time"
    ],
}


def get_response(message):
    message = message.lower().strip()
    for questions, answers in chatbot.items():
        if message in questions:
            return random.choice(answers)
    return "Sorry, i didnt understood!I am being in development will like to add that soon!"
