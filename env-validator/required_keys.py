# Environment Validator — required key comparison
# Checks an env file against a required key list file.

from pathlib import Path


def load_keys(path: Path) -> set[str]:
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        return {line.strip() for line in f if line.strip() and not line.startswith("#")}


def load_env_keys(path: Path) -> set[str]:
    keys = set()

    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if "=" in line and not line.strip().startswith("#"):
                keys.add(line.split("=", 1)[0].strip())

    return keys


env_path = Path(input("Env file path: ").strip())
required_path = Path(input("Required keys file path: ").strip())

if not env_path.is_file() or not required_path.is_file():
    print("Invalid file path")
else:
    print(f"\nComparing env file against required keys\n")

    env_keys = load_env_keys(env_path)
    required_keys = load_keys(required_path)

    missing = sorted(required_keys - env_keys)

    if not missing:
        print("All required keys are present")
    else:
        print("Missing keys:")
        for key in missing:
            print(f"  {key}")

    print("\nComparison completed")
