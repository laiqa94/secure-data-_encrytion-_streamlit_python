import streamlit as st
from cryptography.fernet import Fernet

# Generate or load your encryption key
@st.cache_resource
def generate_key():
    return Fernet.generate_key()

key = generate_key()
fernet = Fernet(key)

st.title("🔐 Secure Data Encryption App")

option = st.radio("Select Operation", ["Encrypt", "Decrypt"])

if option == "Encrypt":
    user_input = st.text_area("Enter the text to encrypt:")
    if st.button("Encrypt"):
        if user_input:
            encrypted_text = fernet.encrypt(user_input.encode()).decode()
            st.success("Encrypted Text:")
            st.code(encrypted_text, language='text')
        else:
            st.warning("Please enter some text to encrypt.")

elif option == "Decrypt":
    encrypted_input = st.text_area("Enter the encrypted text:")
    if st.button("Decrypt"):
        if encrypted_input:
            try:
                decrypted_text = fernet.decrypt(encrypted_input.encode()).decode()
                st.success("Decrypted Text:")
                st.code(decrypted_text, language='text')
            except Exception as e:
                st.error("Decryption failed. Invalid key or corrupted data.")
        else:
            st.warning("Please enter encrypted text to decrypt.")
