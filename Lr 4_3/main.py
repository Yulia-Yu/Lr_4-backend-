from jinja2 import Template
import sqlite3
from booking_model import get_number, get_room, get_type_room_id

room_et = 2
type_room_id = 3

# устанавливаем соединение с базой данных
conn = sqlite3.connect("bd_booking.sqlite")

# открываем файл с дампом базой двнных
f_damp = open('booking.db','r', encoding ='utf-8-sig')

# читаем данные из файла
damp = f_damp.read()

# закрываем файл с дампом
f_damp.close()

# запускаем запросы
conn.executescript(damp)
# сохраняем информацию в базе данных
conn.commit()


# выбираем записи из таблиц (ДОПИСАТЬ)
df_number = get_number(conn, room_et, type_room_id)
df_room = get_room(conn)
df_type_room_id = get_type_room_id(conn)

# закрываем соединение с базой
conn.close()

# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open('template.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)

# генерируем результат на основе шаблона (ДОПИСАТЬ)
result_html = template.render(
    room_et = room_et,
    type_room_id = type_room_id,
    combo_box = df_room,
    combo_box_1 = df_type_room_id,
    relation = df_number,
    len = len)

#создаем файл для HTML-страницы
f = open('booking.html', 'w', encoding ='utf-8-sig')

# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()