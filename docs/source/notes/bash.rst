*************
Shell
*************

Commands
=============
.. code-block:: bash
   tcpdump -qns 0 -A -r nstrace1.pcap

.. code-block:: bash
   zgrep -I cmd_executed ns.log* | more

.. code-block:: bash
   for i in G M K; do du -ah | grep [0-9]$i | sort -nr -k 1; done | head -n 11