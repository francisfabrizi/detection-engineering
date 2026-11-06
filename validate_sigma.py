import sys
from pathlib import Path

from sigma.rule import SigmaRule
from sigma.validation import SigmaValidator
from sigma.validators.core import validators

if len(sys.argv) != 2:
    print("Usage: python validate_sigma.py <rule.yml>")
    sys.exit(1)

rule_path = Path(sys.argv[1])

try:
    rule = SigmaRule.from_yaml(rule_path.read_text())

    validator = SigmaValidator(validators.values())

    issues = validator.validate_rule(rule)

    print("\n========== SIGMA VALIDATION ==========")
    print(f"Rule: {rule.title}")
    print(f"File: {rule_path}")
    print("YAML parsing: PASSED")
    print("Sigma parsing: PASSED")

    if issues:
        print(f"\nFindings: {len(issues)}")

        for issue in issues:
            print(f"[{issue.severity.name}] {issue}")

    else:
        print("\nValidation: PASSED")
        print("No validation findings.")

    print("======================================")

except Exception as error:
    print(f"\nVALIDATION FAILED: {error}")
    sys.exit(1)
