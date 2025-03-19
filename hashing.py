import argon2

password = input("Enter Password:")

ph = argon2.PasswordHasher()

hashed_password = ph.hash(password)

print("Hashed Password", hashed_password)
