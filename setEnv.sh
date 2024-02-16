#!/bin/bash
sudo apt update -y
sudo apt install openjdk-17-jre-headless -y
git clone https://github.com/Abhay-at8/DNS_RP.git
cd DNS_RP/




#cloud-boothook
#!/bin/bash
apt update -y
apt install openjdk-17-jre-headless -y
mkdir -p /home/rp/
cd /home/rp/
git clone https://github.com/Abhay-at8/DNS_RP.git
chmod -R 777  /home/rp/


#cloud-boothook
#!/bin/bash
apt update -y
apt install openjdk-17-jre-headless -y
mkdir -p /home/rp/
cd /home/rp/
git clone https://github.com/Abhay-at8/DNS_RP.git
chmod -R 777  /home/rp/
cd DNS_RP
bash connectChord.sh 3.238.148.111