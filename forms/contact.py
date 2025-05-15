import re

import streamlit as st
import requests  # pip install requests


WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTY4MDYzMDA0MzM1MjY5NTUzMjUxMzIi_pc"


def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Ad")
        email = st.text_input("Email")
        message = st.text_area("Mesaj")
        submit_button = st.form_submit_button("Göndər")

    if submit_button:
        if not WEBHOOK_URL:
            st.error("Email servisi quraşdırılmayıb. Sonra bir daha yoxlayın.", icon="📧")
            st.stop()

        if not name:
            st.error("Adınızı daxil edin.", icon="🧑")
            st.stop()

        if not email:
            st.error("Emailinizi daxil edin.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Emailinizi düzgün daxil edin.", icon="📧")
            st.stop()

        if not message:
            st.error("Mesajınızı daxil edin.", icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {"email": email, "name": name, "message": message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Mesajınız uğurla çatdırıldı! 🎉", icon="🚀")
        else:
            st.error("Mesaj çatdırılırkən xəta baş verdi.", icon="😨")
