# Environment Validator — sample comparison
# Compares a real env file against a sample template.

from pathlib import Path


def load_keys(path: Path) -> set[str]:
    keys = set()

    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if "=" in line and not line.strip().startswith("#"):
                keys.add(line.split("=", 1)[0].strip())

    return keys


env_path = Path(input("Env file path: ").strip())
sample_path = Path(input("Sample env path: ").strip())

if not env_path.is_file() or not sample_path.is_file():
    print("Invalid file path")
else:
    print("\nComparing env file with sample template\n")

    env_keys = load_keys(env_path)
    sample_keys = load_keys(sample_path)

    missing = sorted(sample_keys - env_keys)
    extra = sorted(env_keys - sample_keys)

    if not missing and not extra:
        print("Env file matches sample structure")
    else:
        if missing:
            print("Missing keys:")
            for key in missing:
                print(f"  {key}")

        if extra:
            print("\nExtra keys:")
            for key in extra:
                print(f"  {key}")

    print("\nComparison completed")
