import os
import sqlite3

DB_PATH = r"C:\Users\Admin1\PycharmProjects\PythonLangchainTest1\testMiddle\ecommerce.db"

print(f"DB_PATH = {DB_PATH}")
print(f"文件是否存在: {os.path.exists(DB_PATH)}")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# 查询所有表
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print(f"数据库内的表: {tables}")

if ('orders',) in tables:
    cur.execute("SELECT * FROM orders;")
    rows = cur.fetchall()
    print(f"orders表数据: {rows}")
else:
    print("❌ 不存在orders表！初始化没执行成功")

conn.close()
