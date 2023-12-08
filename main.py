def find_paragraphs_with_word(paragraphs, word):
    result = []
    for paragraph in paragraphs:
        if paragraph.strip() == '\n\n':
            break
        if word.lower() in paragraph.lower():
            result.append(paragraph)
    return result

if __name__ == "__main__":
    file_path = input("Введіть назву файлу:")
    word_to_find = input("Введіть слово:")

    try:
        paragraphs = open(file_path)
        matching_paragraphs = find_paragraphs_with_word(paragraphs, word_to_find)

        if matching_paragraphs:
            print("\nЗнайдені абзаци:")
            for i, paragraph in enumerate(matching_paragraphs, 1):
                print(f"{i}. {paragraph}")
        else:
            print(f"\nСлово '{word_to_find}' не знайдено")
    except FileNotFoundError:
        print(f"Файл'{file_path}' не знайдено")
    except Exception as e:
        print(f"Виникла помилка: {e}")
