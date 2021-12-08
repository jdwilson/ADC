*************
Shell
*************

Commands
=============
.. code-block:: console
   tcpdump -qns 0 -A -r nstrace1.pcap

.. code-block:: console
   zgrep -I cmd_executed ns.log* | more

.. code-block:: console
   for i in G M K; do du -ah | grep [0-9]$i | sort -nr -k 1; done | head -n 11