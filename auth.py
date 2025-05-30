import streamlit as st
import sqlite3
import hashlib
import os

def make_hashed_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(str.encode(password)).hexdigest()

def create_default_admin():
    """Create a default admin user if it doesn't exist."""
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    
    # Check if admin user exists
    c.execute("SELECT username FROM users WHERE username=?", ("admin",))
    if c.fetchone() is None:
        # Create default admin user
        c.execute("INSERT INTO users VALUES (?,?,?)", 
                 ("admin", make_hashed_password("admin123"), "admin@example.com"))
        conn.commit()
    conn.close()

def init_auth_db():
    """Initialize the authentication database."""
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT, email TEXT)''')
    conn.commit()
    conn.close()
    
    # Create default admin user
    create_default_admin()

def add_user(username, password, email):
    """Add a new user to the database."""
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES (?,?,?)", 
                 (username, make_hashed_password(password), email))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def check_user(username, password):
    """Verify user credentials."""
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    if result is not None:
        return result[0] == make_hashed_password(password)
    return False

def login_page():
    """Display the login page."""
    st.title("Welcome to Local Multimodal AI Chat")
    
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            st.subheader("Login")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Login"):
                if check_user(username, password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.success("Logged in successfully!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
        
        with tab2:
            st.subheader("Sign Up")
            new_username = st.text_input("Username", key="signup_username")
            new_password = st.text_input("Password", type="password", key="signup_password")
            confirm_password = st.text_input("Confirm Password", type="password")
            email = st.text_input("Email")
            
            if st.button("Sign Up"):
                if new_password != confirm_password:
                    st.error("Passwords do not match!")
                elif not new_username or not new_password or not email:
                    st.error("Please fill in all fields!")
                else:
                    if add_user(new_username, new_password, email):
                        st.success("Account created successfully! Please login.")
                    else:
                        st.error("Username already exists!")
        
        return False
    
    return True

def logout():
    """Log out the current user."""
    st.session_state.authenticated = False
    st.session_state.username = None 