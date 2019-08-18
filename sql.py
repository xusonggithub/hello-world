import mysql.connector

config = {
    'host': 'cdb-o3n4vpl0.bj.tencentcdb.com',
    'user' : 'root',
    "password" : 'zxc@123321',
    'port' : 10169,
    'database': 'test',
    'charset':'utf8'
}

try:
    cnn = mysql.connector.connect(**config)

except mysql.connector.Error as e:
    print('数据库连接失败' , str(e))
else:
    print("sucessfully")

sql_create_table = 'create table student \
( id int(10)not null auto_increment,\
name varchar(10) default null ,\
age int(3) default null,\
primary key (id))\
ENGINE=MyISAM DEFAULT CHARSET = utf8'

cursor = cnn.cursor(buffered= True)
try:
    cursor.execute(sql_create_table)
except mysql.connector.Error as e:
    print('创建失败', str(e))
else:
    print('sucessfully')

