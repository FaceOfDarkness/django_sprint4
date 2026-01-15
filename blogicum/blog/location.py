from blog.models import Category, Location

# Проверить
print("Категории:", Category.objects.count())
for c in Category.objects.all():
    print(f"- {c.title} (опубликовано: {c.is_published})")

print("\nЛокации:", Location.objects.count())
for l in Location.objects.all():
    print(f"- {l.name} (опубликовано: {l.is_published})")

# Если нет, создать
if Category.objects.count() == 0:
    Category.objects.create(
        title="Без категории",
        slug="no-category",
        description="Категория по умолчанию",
        is_published=True
    )
    print("Создана категория по умолчанию")

if Location.objects.count() == 0:
    Location.objects.create(
        name="Планета Земля",
        is_published=True
    )
    print("Создана локация по умолчанию")