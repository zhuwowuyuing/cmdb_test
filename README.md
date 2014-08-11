#所需包
Django==1.6.2
MySQL-python==1.2.5
South==1.0.0
django-grappelli==2.5.3

---------------------------------------------------------------------------------
yum install -y httpd httpd-devel mysql-server mysql-devel git mod_wsgi

wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz
tar xvfz Python-2.7.8.tgz
cd Python-2.7.8
./configure --prefix=/usr/local
make && make altinstall
cd ..

wget --no-check-certificate https://pypi.python.org/packages/source/d/distribute/distribute-0.6.49.tar.gz
tar xvfz distribute-0.6.49.tar.gz
cd distribute-0.6.49
python2.7 setup.py install
cd ..
wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.6.tar.gz#md5=f61cdd983d2c4e6aeabb70b1060d6f49
tar zxvf virtualenv-1.11.6.tar.gz
cd virtualenv-1.11.6
python2.7 setup.py install
cd ..

创建python虚拟环境
mkdir -p /data/webroot/
virtualenv -p /usr/local/bin/python2.7 /data/webroot/env_python2.7

获取代码
cd /data/webroot/env_python2.7
git clone https://github.com/zhuwowuyuing/cmdb_test.git

#激活python虚拟环境，安装相关包
source /data/webroot/env_python2.7/bin/activate
pip install -r cmdb_test/README.md

新增http配置文件
cat /etc/httpd/conf.d/cmdb.conf << EOF
<VirtualHost *:80>
        ServerName 192.168.1.226
        ServerAlias 192.168.1.226
        WSGIScriptAlias / /data/webroot/env_python2.7/cmdb_test/cmdb/wsgi.py

#        <Directory "/var/www/html/mysite">
#            Order Deny,Allow
#            Allow from all
#        </Directory>

        Alias /static/ /data/webroot/env_python2.7/cmdb_test/static/
        <Location "/cmdb/static/">
            Options -Indexes
        </Location>
</VirtualHost>
EOF

新建mysql数据库assets，用户assets，导入assets.sql（来源于0.35）。
mysqldump -h192.168.0.35 -uassets -passets > assets.sql
mysql -uassets -passets assets < assets1.sql

#修改/data/webroot/env_python2.7/cmdb_test/cmdb/wsgi.py 参数路径
#修改/data/webroot/env_python2.7/cmdb_test/cmdb/settings.py 数据库信息