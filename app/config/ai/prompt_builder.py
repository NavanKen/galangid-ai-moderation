def build_user_prompt(
    intro: str,
    title: str,
    description: str,
    goal_amount: int | None = None,
    category: str | None = None,
    category_label: str = "Kategori",
) -> str:
    parts = [
        intro,
        f"Judul: {title}",
        f"Deskripsi:\n{description}",
    ]

    if goal_amount is not None:
        parts.append(f"Target Donasi: Rp {goal_amount:,}")

    if category:
        parts.append(f"{category_label}: {category}")

    return "\n".join(parts)