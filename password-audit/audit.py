# Password Audit — full evaluation
# Audits a password against common security expectations.

def audit(password: str) -> list[str]:
    issues = []

    if len(password) < 8:
        issues.append("Password is shorter than 8 characters")

    if password.islower() or password.isupper():
        issues.append("Password must mix upper and lower case letters")

    if not any(c.isdigit() for c in password):
        issues.append("Password must include at least one digit")

    if password.isalnum():
        issues.append("Password should include at least one symbol")

    return issues


password = input("Password to audit: ").strip()

print("\nRunning password audit\n")

issues = audit(password)

if not issues:
    print("Audit passed — password meets basic security expectations")
else:
    print("Audit failed:")
    for issue in issues:
        print(f"  - {issue}")

print("\nAudit completed")
