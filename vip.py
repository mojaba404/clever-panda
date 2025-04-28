from jdatetime import datetime, set_locale
from threading import Timer
from time import time
import sqlite3


def connect_db(database):
    data = sqlite3.connect(database)
    curs = data.cursor()
    return data, curs


def save_db(data):
    data.commit()
    data.close()


def get_time(chat_id):
    data, curs = connect_db('vip.db')
    curs.execute('SELECT out_time FROM vips WHERE chat_id = ?',
                 (int(chat_id),))
    res = curs.fetchone()
    data.close()
    if res is None:
        return 'this group is not valid!'
    else:
        set_locale('fa_IR')
        ti = datetime.now().fromtimestamp(
            res[0]).strftime('%A, %d %B 14%y - %H:%M')
        return f'<code>{res[0]}</code> \n=> \n{ti}'


def add_gp(chat_id,tedad):
    t = int(time()) + (60 * 60 * 24 * 30 * tedad)
    gt = get_time(chat_id)
    if gt == 'this group is not valid!':
        data, curs = connect_db('vip.db')
        curs.execute('INSERT INTO vips VALUES(?,?)', (int(chat_id), t))
        save_db(data)
        return 'ok added'

    else:
        return 'this group already existed :)'


def up_gp(chat_id,c:int()): 
    t = int(time()) + (60 * 60 * 24 * 30 * c) 
    gt = get_time(chat_id) 
    if gt == 'this group is not valid!': 
        return gt 
     
    else: 
        data, curs = connect_db('vip.db') 
        curs.execute('UPDATE vips SET out_time = {} WHERE chat_id = {}'.format(t,int(chat_id))) 
        save_db(data) 
        return 'ok updated'


def del_gp(chat_id):
    data, curs = connect_db('vip.db')
    curs.execute('DELETE FROM vips WHERE chat_id = ?', (int(chat_id),))
    save_db(data)
    return 'ok deleted.'


def get_gps():
    data, curs = connect_db('vip.db')
    curs.execute('SELECT chat_id FROM vips')
    res = [i[0] for i in curs.fetchall()]
    data.close()
    return res


def check_group():
    t = int(time())
    data, curs = connect_db('vip.db')
    curs.execute('SELECT chat_id FROM vips WHERE out_time <= ?', (t,))
    chats = [i[0] for i in curs.fetchall()]
    data.close()
    if chats == []:
        pass

    else:
        for i in chats:
            del_gp(i)

    Timer((3600*24), check_group).start()


data, curs = connect_db('vip.db')
curs.execute('''
    CREATE TABLE IF NOT EXISTS vips(
        chat_id int prymary key,
        out_time int not null)
    ''')
save_db(data)
check_group()
