# Password Audit — policy validation
# Validates a password against an explicit policy definition.

def validate(password: str, min_length: int, require_symbol: bool) -> list[str]:
    failures = []

    if len(password) < min_length:
        failures.append(f"Minimum length is {min_length}")

    if require_symbol and password.isalnum():
        failures.append("Symbol required by policy")

    return failures


password = input("Password: ").strip()
min_length = int(input("Minimum length: ").strip())
require_symbol = input("Require symbol? (y/n): ").strip().lower() == "y"

print("\nValidating password against policy\n")

failures = validate(password, min_length, require_symbol)

if not failures:
    print("Password complies with policy")
else:
    print("Policy violations:")
    for issue in failures:
        print(f"  - {issue}")

print("\nValidation completed")
