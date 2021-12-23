*************
Windows
*************

Cmd Prompt
=============

Find MSS size to endpoint; add 28-bytes typically for MTU

.. raw:: html

   <pre><code class="language-batch">ping test.consonto.com -f -l 1472</code></pre>

Show configured MTU of NICs

.. raw:: html

   <pre><code class="language-batch">netsh int ip show int</code></pre>

Show configured TCP parameters

.. raw:: html

   <pre><code class="language-batch">netsh interface tcp show global</code></pre>