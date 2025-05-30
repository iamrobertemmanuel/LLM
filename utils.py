from datetime import datetime
import base64
import yaml
import requests
from dotenv import load_dotenv
import streamlit as st
import os
import time
from typing import Dict, Any
load_dotenv()


def load_config() -> Dict[str, Any]:
    """Load configuration from config.yaml or environment variable."""
    # First try to load from environment variable (Replit)
    config_yaml = os.getenv('CONFIG_YAML')
    if config_yaml:
        return yaml.safe_load(config_yaml)
    
    # If not in environment, try to load from file
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    # If neither exists, try the example config
    example_config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml.example')
    if os.path.exists(example_config_path):
        with open(example_config_path, 'r') as f:
            return yaml.safe_load(f)
    
    raise FileNotFoundError("No configuration file found")

config = load_config()


def convert_ns_to_seconds(ns: int) -> float:
    """Convert nanoseconds to seconds."""
    return ns / 1e9 

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

def command(user_input):
    if user_input == "/help":
        return "Possible commands:\n- /help"
    else:    
        return """Invalid command, please use one of the following:\n
                    - /help"""

def list_openai_models():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    response = requests.get("https://api.openai.com/v1/models", headers={"Authorization": f"Bearer {openai_api_key}"}).json()
    if response.get("error", False):
        st.warning("Openai Error: " + response["error"]["message"])
        return []
    else:
        return [item["id"] for item in response["data"]]
    
def convert_bytes_to_base64(image_bytes: bytes) -> str:
    """Convert bytes to base64 string."""
    return base64.b64encode(image_bytes).decode('utf-8')
    
def convert_bytes_to_base64_with_prefix(image_bytes: bytes) -> str:
    """Convert bytes to base64 string with data URL prefix."""
    base64_str = convert_bytes_to_base64(image_bytes)
    return f"data:image/jpeg;base64,{base64_str}"

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_avatar(sender_type):
    if sender_type == "user":
        return "chat_icons/user_image.png"
    else:
       return "chat_icons/bot_image.png"

def save_config(config):
    with open("config.yaml", "w") as f:
        yaml.dump(config, f, default_flow_style=False)