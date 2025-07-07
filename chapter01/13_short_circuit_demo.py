name = "Bob"

print("--------------or-----------")

valid_user = None or "User"
print("Hello", valid_user)

print("-" * 20)

valid_user = name or "User"
print("Hello", valid_user)

print("--------------and-----------")

email = "example@email.gr"

valid_email = email and email != ""

print("Valid email", valid_email)

if valid_email:
    print(f"Hello {valid_user}, your email is {valid_email}")
else:
    print(f"Hello {valid_user}, please provide your email.")