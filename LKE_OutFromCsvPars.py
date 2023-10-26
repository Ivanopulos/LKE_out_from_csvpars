import pandas as pd

# Шаг 1: Прочитать CSV файл.
df = pd.read_csv('index_fedstat_515.csv', header=None, names=['Link', 'Text'])
print(df.head())

# Функция для разбора текста
def parse_text(text):
    sections = [
        "Методика расчета", "Комментарии", "Ведомство", "Разделы ФПСР",
        "Ответственный", "Характеристики", "Единицы измерения",
        "Период действия", "Признаки (классификаторы и справочники)",
        "Источники и способ формирования показателя"
    ]

    result = {}
    for i, section in enumerate(sections):
        start = text.find(section)
        end = text.find(sections[i + 1]) if i + 1 < len(sections) else len(text)
        result[section] = text[start:end].replace(section, '').strip()
    return result


# Шаг 2: Разобрать текст
parsed_data = df['Text'].apply(parse_text).tolist()
parsed_df = pd.DataFrame(parsed_data)

# Добавить столбец с ссылками
parsed_df.insert(0, 'Ссылка', df['Link'])

# Шаг 3: Записать данные в Excel файл
parsed_df.to_excel('output.xlsx', index=False)