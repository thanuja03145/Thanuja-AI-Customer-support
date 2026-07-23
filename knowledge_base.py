KNOWLEDGE_BASE = {
    "Product Inquiry": "We offer top-grade AI and tech products. All items come with a 1-year standard warranty.",
    "Order Status": "You can track your order status using your Order ID on our website under 'My Orders'. Shipping takes 3-5 business days.",
    "Returns & Refunds": "Returns are accepted within 14 days of purchase. Refunds will be processed within 5-7 working days after return verification.",
    "Technical Support": "If you face technical issues, try restarting your device or updating to the latest software version. Contact support for further aid.",
    "General Query": "Our customer support team is available Monday to Friday, 9 AM to 6 PM IST to assist you with any questions."
}

def get_knowledge_response(intent: str) -> str:
    return KNOWLEDGE_BASE.get(intent, KNOWLEDGE_BASE["General Query"])
