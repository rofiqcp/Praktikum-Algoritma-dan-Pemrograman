# Architecture

```text
[Browser]
   |
   | GET static / user interaction
   v
[Node.js Express :3000]
   |
   | browser fetch JSON
   v
[Python Flask :5001]
   | validation + business logic
   | parameterized SQL
   v
[SQLite]
 categories (1) ───── (N) products
```

## Ownership
- Node: static web/UI delivery.
- Browser JS: interaction, fetch, UI state.
- Python: API contract, validation, business rules.
- DB: persistence, key/relationship/constraint.
