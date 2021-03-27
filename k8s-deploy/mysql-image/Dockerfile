FROM mysql
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=MyDB
COPY /table.sql /docker-entrypoint-initdb.d/
