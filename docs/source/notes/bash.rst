*************
Shell
*************

Commands
=============
Read pcap directly from CLI

.. parsed-literal::
   tcpdump -qns 0 -A -r nstrace1.pcap

Search for string in all ns.log files including zipped 

.. parsed-literal::
   zgrep -I cmd_executed ns.log* | more

Find the top 10 largest directories and files

.. parsed-literal::
   for i in G M K; do du -ah | grep [0-9]$i | sort -nr -k 1; done | head -n 11

Generate random base64 string with OpenSSL

.. parsed-literal::
   openssl rand -base64 20

Remove passphrase from key 

.. parsed-literal::
   openssl rsa -in privateKey.pem -out newPrivateKey.pem
