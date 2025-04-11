import os
import sqlite3

# 从环境变量获取数据库路径，默认使用 /tmp/db.sqlite3
DB_PATH = os.getenv("DB_PATH", "/tmp/db.sqlite3")

# 确保数据库目录存在
db_dir = os.path.dirname(DB_PATH)
if not os.path.exists(db_dir):
    print(f"Directory {db_dir} does not exist. Creating it...")
    os.makedirs(db_dir, exist_ok=True)

# 打印数据库路径以调试
print(f"Database Path: {DB_PATH}")

# 连接到 SQLite 数据库
try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 创建表：reminders
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        message TEXT,
        time TEXT
    )
    """)

    # 创建表：tasks
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        task TEXT
    )
    """)

    # 创建表：chat_logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_logs (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 提交更改
    conn.commit()
except sqlite3.OperationalError as e:
    print(f"SQLite OperationalError: {e}")
    raise
finally:
    # 关闭数据库连接
    if 'conn' in locals():
        conn.close()