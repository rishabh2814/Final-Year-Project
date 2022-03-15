from sqlalchemy.orm import sessionmaker
from project_orm import User_Command, Command
from sqlalchemy import create_engine
import streamlit as st

engine = create_engine('sqlite:///project_db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

st.title("Using database with SQLAlchemy")

actions = st.text_input('enter the action to perform')

keyCode = st.number_input('enter key_code')

uploaded_on =  st.date_input("enter the uploading date")
st.write(uploaded_on)

submit = st.button("Submmit")

if submit:
    try:
        entry = User_Command(actions=actions,
                      key_code=keyCode,
                      uploaded_on = uploaded_on)
        sess.add(entry)
        sess.commit()
        st.success("data added to database")
    except Exception as e:
        st.error(f"some error occurred : {e}")


if st.checkbox("view data"):
    results = sess.query(User_Command).all()
    for item in results:
        st.subheader(item.actions)
        st.text(item.key_code)
        st.text(item.uploaded_on)