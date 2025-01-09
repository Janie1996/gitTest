conn_params = {
    'host': '101.37.20.199',  # ECS 实例的公网 IP 地址
    'port': 15432,           # ECS 实例上映射的端口
    'database': 'llpt',      # 新创建的数据库名称
    'user': 'huangzy',           # 数据库用户名
    'password': 'owQ1sCZ^vnxeQiX2025'  # 数据库密码
}

# 连接到数据库
import psycopg2
conn = psycopg2.connect(**conn_params)

# 创建游标对象
cur = conn.cursor()

# 执行查询
cur.execute('SELECT version();')

# 获取查询结果
db_version = cur.fetchone()
print('Database version:', db_version)

# 关闭游标和连接
cur.close()
conn.close()