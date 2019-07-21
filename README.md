# scapyHttpConvoExtract
python script for extracting the HTTP conversations in a packet capture




You should first run 'pip install scapy' or 'easy_install scapy' from your terminal to install the tool. 

Then you should get your packet capture file and replace the 'attack.pcap' strings in the python file with the name of your pcap file. Then:

> python tSharkPayloadExtract.py

The output should look something like this:

GET /phantom/OpBro.asp? HTTP/1.1
Host: phantomOpBro.org
Accept: */*


HTTP/1.1 302 Object moved
Cache-Control: private
Content-Length: 999
Content-Type: text/html
Location: OpBro.asp?
Server: Server
Set-Cookie: cookieMonster; path=/
Date: Sun, 21 Jul 2019 13:43:11 UTC

<head><title>Erro_Page</title></head>
<body><h1>You have encountered an error <a HREF="index.asp?"></a>.</body>
