import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
# pip install pyyaml


# Step 1. Import the YAML file into your script:
with open('config.yaml', 'r') as f:
    config = yaml.load(f, Loader=SafeLoader)

# for u in config['credentials']['usernames']:
#     password = config['credentials']['usernames'][u]['password']
#     hashed_passwords = stauth.Hasher([password]).generate()
#     # Replace the plain text passwords in the YAML file with the generated hashed passwords.
#     config['credentials']['usernames'][u]['password'] = hashed_passwords[0]


# Step2. Create the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Step 3. Render the login widget by providing a name for the form and its location (i.e., sidebar or main):
name, authentication_status, username = authenticator.login()
print(st.session_state)


if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')


# jsmith abc
# rbriggs def

# if st.session_state["authentication_status"]:
#     try:
#         if authenticator.reset_password(st.session_state["username"]):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)


# https://github.com/mkhorasani/Streamlit-Authenticator/blob/main/streamlit_authenticator/authenticate.py
# https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/


# streamlit run author.py --server.port 9000 --server.address 127.0.0.1
# streamlit run author.py --server.port 9000 --server.address 0.0.0.0
