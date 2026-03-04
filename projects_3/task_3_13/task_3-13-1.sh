#!/bin/bash

TARGET_FILE="settings.php"

if [ ! -f "$TARGET_FILE" ]; then
    echo "Ошибка: Файл $TARGET_FILE не найден в текущей директории."
    exit 1
fi

sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' "$TARGET_FILE"

echo "Путь к базе данных в файле $TARGET_FILE успешно обновлен."
exit 0
