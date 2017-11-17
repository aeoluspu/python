#########################################################################
# File Name: baoli_kill.sh
# Author: zhaohongpu
# mail: idbalife@gmail.com
# Created Time: 二 10/31 10:18:42 2017
#########################################################################
#!/bin/bash

host=$1
query_type=$2
mysql -h$host -e "show processlist"  |grep $query_type  |awk '{print "kill " $1 ";"}'|mysql -h$host
