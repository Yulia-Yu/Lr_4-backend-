import pandas as pd

def get_room(conn):
 return pd.read_sql('''SELECT DISTINCT room_et FROM room 
                    ORDER BY 1''', conn)

def get_type_room_id(conn):
    return pd.read_sql('''SELECT * FROM type_room''', conn)

def get_number(conn, room_et, type_room_id):
    return pd.read_sql('''
     SELECT
     room_name AS Номер,
     type_room_name AS Тип_номера,
     price AS Цена
     FROM room
     INNER JOIN type_room USING (type_room_id)
     where room_et == :room_et and type_room_id == :type_room_id 
     ORDER BY 3, 1 
    ''', conn, params={"room_et": room_et, "type_room_id": type_room_id})
