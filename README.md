The Java Code base is available at https://github.com/Abhay-at8/DHT-Based-DNS-Java-Codebase.git
The jar file created from the above code is used here for deploying

Steps for deploying on AWS and testing/comparison

1) Use the commands in setEnv.sh to deploy the code the aws instances and startup of the service

2) Once the instances are connected use loadBulk.sh to load the data on the nodes. The load data of 1,00,000 domain names is divided into 10 files stored in LOAD_DATASETS.
   To load data pass the path to the files as an argument to the above script. For eg bash loadBulk.sh LOAD_DATASETS/d1.
   Different datasets can be loaded simultaneously by passing different paths as arguments on different nodes.

3) Once data is loaded, update the dns.properties file to true on all nodes to stimulate offline mode for testing DHT-based DNS. AWS system manager can used to update file on all nodes using a single command.

4) On any one instance run the query.sh script to test the DHT-based DNS resolution using the test data present in the dataset file.

5) Run the report.py file once the above step is completed.

6) In the comparison folder, 
	i)	First run status_code_before.py file.
 	ii)	Then move the content of the temporary.txt file to the systems host file.
	iii) 	Run the status_code_after.py 
	iv)	Revert the host file content.
	v)	Analysis of status code from traditional DNS and DHT-based DNS comparison can be seen by running show.py file.


Step 6 was repeated after certain intervals for 2 months to test the longevity of DHT-based DNS. The results were plotted on a graph