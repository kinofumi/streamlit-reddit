import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import json

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-reddit-4a96e")

title = st.text_input("タイトルを入力してください")
url = st.text_input("URLを入力してください")
submit = st.button("送信する")

if title and url and submit:
    doc_ref = db.collection("posts").document(title)
    doc_ref.set({
        "title": title,
        "url": url,
    })

posts_ref = db.collection("posts")
for doc in posts_ref.stream():
    post = doc.to_dict()
    title = post["title"]
    url = post["url"]

    st.write(f"タイトル: {title}")
    st.write(f":link: [{url}]({url})")

# db = firestore.Client.from_service_account_json("firestore-key.json")

# doc_ref = db.collection("posts").document("Google")
# doc = doc_ref.get()

# st.write("This id is:", doc.id)
# st.write("The contents are:", doc.to_dict())

# doc_ref = db.collection("posts").document("Apple")
# doc_ref.set({
#     "title": "Apple",
#     "url": "www.apple.com",
# })
