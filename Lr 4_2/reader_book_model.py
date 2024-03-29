import pandas as pd

def get_reader(conn):
 return pd.read_sql("SELECT * FROM reader", conn)


def get_book_reader(conn, reader_id):
 return pd.read_sql('''SELECT title AS Название, author_name AS Авторы, borrow_date AS Дата_выдачи, return_date AS Дата_возврата 
                     FROM reader INNER JOIN book_reader USING (reader_id)
                     INNER JOIN book USING (book_id)
                     INNER JOIN book_author USING (book_id)
                     INNER JOIN author USING (author_id)
                     WHERE reader_id == :reader_id  
                     ''', conn, params={"reader_id": reader_id})