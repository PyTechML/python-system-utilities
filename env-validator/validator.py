# Environment Validator — core check
# Validates presence and non-empty values for required environment keys.

from pathlib import Path


def load_env(path: Path) -> dict[str, str]:
    env = {}

    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()

    return env


env_path = Path(input("Env file path: ").strip())
required_raw = input("Required keys (comma separated): ").strip()
required = [k.strip() for k in required_raw.split(",") if k.strip()]

if not env_path.is_file():
    print("Invalid env file")
else:
    print(f"\nValidating environment file: {env_path}\n")

    env = load_env(env_path)
    missing = []
    empty = []

    for key in required:
        if key not in env:
            missing.append(key)
        elif not env[key]:
            empty.append(key)

    if not missing and not empty:
        print("Validation passed — all required keys present")
    else:
        if missing:
            print("Missing keys:")
            for key in missing:
                print(f"  {key}")

        if empty:
            print("\nEmpty values:")
            for key in empty:
                print(f"  {key}")

    print("\nValidation completed")
