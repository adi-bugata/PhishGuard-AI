import json
from app import inspect_message

with open("synthetic_test_cases.json", encoding="utf-8") as f:
    cases = json.load(f)

passed = 0
for case in cases:
    found = {item["title"] for item in inspect_message(case["message"])}
    expected = set(case["expected_indicators"])
    ok = expected.issubset(found)
    print(f'{case["id"]}: {"PASS" if ok else "CHECK"}')
    if not ok:
        print("  Expected:", sorted(expected))
        print("  Found:   ", sorted(found))
    passed += int(ok)

print(f"\n{passed}/{len(cases)} cases passed the expected-indicator check.")
print("This is a small synthetic smoke test, not a validated security accuracy score.")
