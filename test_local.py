
import json
from app import analyse

with open("synthetic_test_cases.json", encoding="utf-8") as f:
    cases = json.load(f)

passed = 0

for case in cases:
    direct, contextual = analyse(case["message"])

    found = {
        item[0] for item in direct + contextual
    }

    expected = set(case["expected_indicators"])

    missing = expected - found
    unexpected = found - expected

    ok = not missing and not unexpected

    print(f'{case["id"]}: {"PASS" if ok else "CHECK"}')

    if missing:
        print("  Missing:", sorted(missing))

    if unexpected:
        print("  Unexpected:", sorted(unexpected))

    passed += int(ok)

print(f"\n{passed}/{len(cases)} cases passed.")

print(
    "Note: This is a small synthetic test, "
    "not a validated security accuracy score."
)
