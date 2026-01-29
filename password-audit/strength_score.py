# Password Audit — strength scoring
# Assigns a simple strength score based on composition.

def score(password: str) -> int:
    points = 0

    if len(password) >= 8:
        points += 2
    if len(password) >= 12:
        points += 2
    if any(c.isupper() for c in password):
        points += 2
    if any(c.isdigit() for c in password):
        points += 2
    if not password.isalnum():
        points += 2

    return points


password = input("Password to score: ").strip()

print("\nScoring password strength\n")

points = score(password)

print(f"Score: {points} / 10")

if points >= 8:
    print("Strength: strong")
elif points >= 5:
    print("Strength: moderate")
else:
    print("Strength: weak")

print("\nScoring completed")
