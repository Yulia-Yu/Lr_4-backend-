from jinja2 import Template
import sqlite3
from library_model import get_publisher, get_genre, get_reader, get_author, get_book_author, get_book, get_book_reader

# устанавливаем соединение с базой данных (
conn = sqlite3.connect("library.sqlite")

# выбираем записи из таблицы publisher
df_publisher = get_publisher(conn)
df_genre = get_genre(conn)
df_reader = get_reader(conn)
df_author = get_author(conn)
df_book_author = get_book_author(conn)
df_book = get_book(conn)
df_book_reader = get_book_reader(conn)

# закрываем соединение с базой
conn.close()

# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open('library_templ.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)

# генерируем результат на основе шаблона
result_html = template.render(
 name_1 = "publisher",
 relation_1 = df_publisher,
 name_2 = "genre",
 relation_2 = df_genre,
 name_3 = "reader",
 relation_3 = df_reader,
 name_4 = "author",
 relation_4 = df_author,
 name_5 = "book_author",
 relation_5 = df_book_author,
 name_6 = "book",
 relation_6 = df_book,
 name_7 = "book_reader",
 relation_7 = df_book_reader,
 len = len
 )
#создаем файл для HTML-страницы
f = open('library.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()

