# inspo from https://gist.github.com/Ignas/1676353

# init makefile for linux users ;)

# Niko: I had trouble with my sockets so put the socket in /tmp
# should work if pg installed with package manager

# the makefile serves to handle the files more easily
# for example running access control setup: creating users
# and roles happens with: make access_control

DB_NAME = bidi
DB_USER = $(shell whoami)
DB_DATA = $(HOME)/postgres/data
DB_SOCKET = /tmp
DB_LOG = $(DB_DATA)/pg.log
PSQL    = psql -U $(DB_USER) -h $(DB_SOCKET)

start:
	pg_ctl -D $(DB_DATA) -o "-k $(DB_SOCKET)" -l $(DB_LOG) start 

setup:
	test -d $(DB_DATA) || initdb -D $(DB_DATA)
	$(MAKE) start

connect:
	$(PSQL) $(DB_NAME)

# Execute sql files
init:
	$(PSQL) $(DB_NAME) -f database_create_files/init.sql

access_control:
	$(PSQL) $(DB_NAME) -f database_create_files/access_control.sql

tables:
	$(PSQL) $(DB_NAME) -f database_create_files/tables.sql


# reset and stop
reset: start
	$(PSQL) $(DB_NAME) -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
	$(MAKE) init

stop: 
	pg_ctl -D $(DB_DATA) stop

