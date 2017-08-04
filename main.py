import sqlite3
import os, os.path, threading
from tkinter import *
import inspect
import ctypes

<<<<<<< HEAD
__DATAFILENAME = 'database.db'

=======
>>>>>>> d952391df711e6803e5c4d664c3218e638ee2a1d
def initFinder(dir):
    global current
    current = 0
    _l_conn = init()
    _l_conn.execute('delete from filedata where filepath like \'%' + dir + '%\'')
    _l_conn.commit()
    findPath(dir)
    var1.set('扫描结束 %d 个文件已索引到数据库中' % current)  
    _l_conn.close()  

def findPath(dir):
    global current, var1, conn
    content.set(dir)
    listdir = os.listdir(dir)
    for i in listdir:
        # print('%s - %s = %s' % ('/'.join((dir, i)), os.path.isdir('/'.join((dir, i))), os.path.isfile('/'.join((dir, i)))))
        if os.path.isdir('/'.join((dir, i))) and os.access('/'.join((dir, i)), os.R_OK):
            try:
                findPath('/'.join((dir, i)))
            except:
                pass
                # print('%s add failed' % '/'.join((dir, i)))
        if os.path.isfile('/'.join((dir, i))):
            conn.execute('insert into filedata(filepath, filename) VALUES(?, ?)', ('/'.join((dir, i)), i))
            current += 1
            var1.set(str(current))
            # print('%s pushed' % '/'.join((dir, i)))
    conn.commit()

def startTask():
    global pool, current
    current = 0
    th = threading.Thread(target=initFinder, args=(content.get(), ))
    pool.append(th)
    th.setDaemon(True)
    th.start()
def stopTask():
    global pool
    for t in pool:
        stop_thread(t)
        pool.remove(t)
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
def main():
    global var1
    frame1 = Frame(tk)
    entry1 = Entry(textvariable = content)
    entry1.pack(side = TOP, padx = 20, pady = 20)
    label = Label(textvariable = var1)
    button1 = Button(text = '开始扫描', command = startTask)
    button2 = Button(text = '停止扫描', command = stopTask)
    label.pack()
    button1.pack(side = LEFT)
    button2.pack(side = RIGHT)
    var1.set('任务开始')
    tk.mainloop()
def init():
    global conn, cur
<<<<<<< HEAD
    conn = sqlite3.connect(__DATAFILENAME)
=======
    conn = sqlite3.connect('datebase.db')
>>>>>>> d952391df711e6803e5c4d664c3218e638ee2a1d
    cur = conn.cursor()
    conn.execute('''CREATE TABLE IF NOT EXISTS `filedata` (
    `id`  int AUTO_INCREMENT,
    `filepath`  text NULL ,
    `filename`  text NULL ,
    PRIMARY KEY (`id`)
    )
    ;''')
    return conn
pool = []
current = 0
tk = Tk()
var1 = StringVar()
content = StringVar()
content.set('D:')


if __name__ == '__main__':
    main()