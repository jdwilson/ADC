*************
Shell
*************

Commands
=============
Read pcap directly from CLI

.. raw:: html

   <pre><code class="language-bash">tcpdump -qns 0 -A -r nstrace1.pcap</code></pre>

Search for string in all ns.log files including zipped 

.. raw:: html

   <pre><code class="language-bash">zgrep -I cmd_executed ns.log* | more</code></pre>

Find the top 10 largest directories and files

.. raw:: html

   <pre><code class="language-bash">for i in G M K; do du -ah | grep [0-9]$i | sort -nr -k 1; done | head -n 11</code></pre>

Generate random base64 string with OpenSSL

.. raw:: html

   <pre><code class="language-bash">openssl rand -base64 20</code></pre>

Remove passphrase from key

.. raw:: html

   <pre><code class="language-bash">openssl rsa -in privateKey.pem -out newPrivateKey.pem</code></pre>