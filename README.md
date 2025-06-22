# OWASP Security Testing Lab

This repo runs security test cases based on the OWASP Testing Guide.  
Vulnerable app target: OWASP Juice Shop (running at http://localhost:3000)

## Structure
- /testcases: Python scripts for test cases
- /utils: Shared helpers (e.g., ZAP API)
- /reports: Output of scans
- /patches: Fix diffs for vulnerable apps

## Run tests

Execute all testcases using the helper script. Optional arguments like the target
`--base-url` can be provided and will be forwarded to the Python runner:

```bash
./run_tests.sh --base-url http://localhost:3000
```
