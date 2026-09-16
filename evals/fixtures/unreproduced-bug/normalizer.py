def normalize_rows(rows: list[str]) -> list[str]:
    return [row.strip().lower() for row in rows if row.strip()]
