inst_ip=$(curl http://checkip.amazonaws.com)
java -cp DNSServerWithCaching-1.0-SNAPSHOT.jar:dnsjava-2.1.1.jar:sqlite-jdbc-3.30.1.jar  org.kalit.client.Query $inst_ip 8080