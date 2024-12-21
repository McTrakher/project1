import json
def get_articles():
    with open("articles.json", "r", encoding="utf-8") as file:
        articles = json.load(file)
    return articles

def save_article(name, text):
    try:
        with open('articles.json', 'r', encoding='utf-8') as file:
            articles = json.load(file)
    except FileNotFoundError:
        articles = {}

    articles[name] = text

    with open('articles.json', 'w', encoding='utf-8') as file:
        json.dump(articles, file, ensure_ascii=False, indent=4)

def delete_article(name):
    try:
        with open('articles.json', 'r', encoding='utf-8') as file:
            articles = json.load(file)

        if name in articles:
            del articles[name]
            with open('articles.json', 'w', encoding='utf-8') as file:
                json.dump(articles, file, ensure_ascii=False, indent=2)
            print(f"Статья '{name}' была успешно удалена.")
        else:
            print(f"Статья '{name}' не найдена.")
    except FileNotFoundError:
        print("Файл articles.json не найден.")
    except json.JSONDecodeError:
        print("Ошибка чтения файла articles.json. Возможно, он повреждён.")
