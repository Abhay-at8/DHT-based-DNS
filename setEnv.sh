


#MANNUAL STEPS

#FIRST NODE

#cloud-boothook
#!/bin/bash
apt update -y
apt install openjdk-17-jre-headless -y
mkdir -p /home/rp/
cd /home/rp/
git clone https://github.com/Abhay-at8/DHT-based-DNS.git
chmod -R 777  /home/rp/
bash startServer.sh


#OTHER NODES

#cloud-boothook
#!/bin/bash
apt update -y
apt install openjdk-17-jre-headless -y
mkdir -p /home/rp/
cd /home/rp/
git clone https://github.com/Abhay-at8/DHT-based-DNS.git
chmod -R 777  /home/rp/
cd DNS_RP
bash connectChord.sh <IP OF ANY CONNECTED NODE>

------------------------------------------------------------------------------------------------------------------
#FOR AUTOMATION

#USER DATA FOR LAUNCHING AWS INSTANCES OR CREATING INSTANCE TEMPLATE FOR LAUNCHING MULTIPLE INSTANCES

#cloud-boothook
#!/bin/bash
apt update -y
apt install openjdk-17-jre-headless -y
mkdir -p /home/rp/
cd /home/rp/
git clone https://github.com/Abhay-at8/DHT-based-DNS.git
chmod -R 777  /home/rp/


#AWS SYSTEM MANANGER SCRIPT TO RUN COMMAND ON MULTIPLE NODES

cd /home/rp/DNS_RP; nohup bash connectChord.sh "(IP OF ANY CONNECTED NODE)" < /dev/null 2> /dev/null > /dev/null &