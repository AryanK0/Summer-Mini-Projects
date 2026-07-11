# Import Modules
import mysql.connector
import random
import base64

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import bcrypt

# Database Connection
DATABASE = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#YOUR_DB_PASSWORD#"
)

cursor = DATABASE.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS userPasswords")
cursor.execute("USE userPasswords")

# Create Tables if Needed
cursor.execute("SHOW TABLES LIKE 'entries'")
result = cursor.fetchone()
if not result:
    cursor.execute(
        """
        CREATE TABLE entries(
            id VARCHAR(4),
            title VARCHAR(32),
            profile VARCHAR(32),
            password VARCHAR(100),
            notes VARCHAR(512)
        )
        """
    )

cursor.execute("SHOW TABLES LIKE 'master'")
result = cursor.fetchone()
if not result:
    cursor.execute(
        """
        CREATE TABLE master(
            keyName VARCHAR(128),
            keyValue VARCHAR(512)
        )
        """
    )
    cursor.execute(
        "INSERT INTO master VALUES(%s, %s)",
        ("masterPassword", "")
    )

DATABASE.commit()

MASTER_PASS = ""

# Crypto Functions
def hash_SHA256(text):
    return SHA256.new(text.encode()).hexdigest()


def derive_key(password):
    b64pwd = base64.b64encode(SHA256.new(password.encode()).digest())
    bcrypt_hash = bcrypt(b64pwd, 12, b"salt for bcrypt1")
    return bcrypt_hash[:32]


def encrypt_AES(text, key):
    cipher = AES.new(key, AES.MODE_CFB, key[::-1][:16])
    return base64.b64encode(cipher.encrypt(text.encode())).decode()


def decrypt_AES(text, key):
    cipher = AES.new(key, AES.MODE_CFB, key[::-1][:16])
    return cipher.decrypt(base64.b64decode(text)).decode()

# UI Helpers
def print_title():
    print("""
 ░█▀▀░█▀▀░█▀▀░█░█░█▀▄░█▀▀   ░█▀█░█▀█░█▀▀░█▀▀
 ░▀▀█░█▀▀░█░░░█░█░█▀▄░█▀▀   ░█▀▀░█▀█░▀▀█░▀▀█
 ░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀   ░▀░░░▀░▀░▀▀▀░▀▀▀
    """)

# Main Logic
def main():
    global MASTER_PASS

    print("=" * 53)
    print_title()
    print("=" * 53)

    cursor.execute(
        "SELECT keyValue FROM master WHERE keyName='masterPassword'"
    )
    master_password = cursor.fetchone()[0]

    if not master_password:
        while True:
            pwd = input("Create Master Password: ")
            confirm = input("Re-Enter Master Password: ")
            if pwd == confirm:
                break
            print("Password mismatch.\n")

        master_password = hash_SHA256(pwd)
        cursor.execute(
            "UPDATE master SET keyValue=%s WHERE keyName='masterPassword'",
            (master_password,)
        )
        DATABASE.commit()
        print("New Master Password Set.\n")

    entered = input("Enter Master Password: ")
    if hash_SHA256(entered) != master_password:
        print("Access Denied.")
        cursor.close()
        DATABASE.close()
        exit()

    MASTER_PASS = master_password
    menu_showMain()

# Menus
def menu_showMain():
    print_title()
    print("""
 1] List Profiles
 2] Add Profile
 3] Edit Profile
 4] Delete Profile
 Any other key to exit
    """)

    ch = input(">> ").strip()

    if ch == "1":
        showProfiles()
    elif ch == "2":
        addProfile()
    elif ch == "3":
        editProfile()
    elif ch == "4":
        deleteProfile()
    else:
        cursor.close()
        DATABASE.close()
        exit()

# Profile Functions
def showProfiles():
    cursor.execute("SELECT * FROM entries")
    results = cursor.fetchall()

    if not results:
        print("No profiles added.")
        return menu_showMain()

    for i, entry in enumerate(results, 1):
        print(f"[ID #{i}] {entry[1]}")
        print("Profile:", entry[2])
        print("Password:", decrypt_AES(entry[3], derive_key(MASTER_PASS)))
        print("Notes:", entry[4])
        print("-" * 30)

    input("Press Enter to go back")
    menu_showMain()


def addProfile():
    title = input("Title: ")
    profile = input("Username: ")

    while True:
        pwd = input("Password: ")
        confirm = input("Confirm Password: ")
        if pwd == confirm:
            break
        print("Password mismatch.\n")

    notes = input("Notes: ")
    enc_pwd = encrypt_AES(pwd, derive_key(MASTER_PASS))
    uid = title[0] + str(random.randint(100, 999))

    cursor.execute(
        "INSERT INTO entries VALUES(%s,%s,%s,%s,%s)",
        (uid, title, profile, enc_pwd, notes)
    )
    DATABASE.commit()
    print("Profile added.\n")
    menu_showMain()


def editProfile():
    cursor.execute("SELECT * FROM entries")
    results = cursor.fetchall()

    if not results:
        print("No profiles found.")
        return menu_showMain()

    for i, e in enumerate(results, 1):
        print(f"[{i}] {e[1]} | {e[2]}")

    idx = int(input("Select ID: ")) - 1
    data = list(results[idx])

    new_title = input("New Title (blank to skip): ")
    new_profile = input("New Username (blank to skip): ")
    new_notes = input("New Notes (blank to skip): ")

    if new_title:
        data[1] = new_title
    if new_profile:
        data[2] = new_profile
    if new_notes:
        data[4] = new_notes

    cursor.execute("DELETE FROM entries WHERE id=%s", (data[0],))
    cursor.execute(
        "INSERT INTO entries VALUES(%s,%s,%s,%s,%s)",
        tuple(data)
    )
    DATABASE.commit()
    print("Profile updated.\n")
    menu_showMain()


def deleteProfile():
    cursor.execute("SELECT * FROM entries")
    results = cursor.fetchall()

    for i, e in enumerate(results, 1):
        print(f"[{i}] {e[1]}")

    idx = int(input("Select ID to delete: ")) - 1
    cursor.execute(
        "DELETE FROM entries WHERE id=%s",
        (results[idx][0],)
    )
    DATABASE.commit()
    print("Profile deleted.\n")
    menu_showMain()

# Run App
main()