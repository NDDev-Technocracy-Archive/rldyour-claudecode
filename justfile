set shell := ["bash", "-euo", "pipefail", "-c"]

# List the retained workflow-source commands.
default:
    @just --list

# Check workflow/command source offline; native validation remains in its existing jobs.
check:
    just --fmt --check
    actionlint
    zizmor --offline --no-progress .github/workflows/validate.yml .github/workflows/claude-cli-drift.yml .github/workflows/cross-platform.yml .github/workflows/dependency-check.yml .github/workflows/pytest.yml .github/workflows/security.yml .github/workflows/security-daily.yml .github/dependabot.yml

# Retain the integration/manual source gate and complete-history secret scan.
verify: check
    betterleaks git --no-banner --redact .

# Format only the owned command source.
fix:
    just --fmt
