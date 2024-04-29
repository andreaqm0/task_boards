#!/bin/bash
# wait-for-mariadb.sh

set -e

host="$1"
shift
cmd="$@"

until mysqladmin ping -h "$host" --silent; do
  >&2 echo "MariaDB is unavailable - sleeping"
  sleep 1
done

>&2 echo "MariaDB is up - executing command"
exec $cmd
