var1=$(date)
while IFS= read -r line; do
    nslookup $line
done < dataset

echo $var1
echo "after"
date