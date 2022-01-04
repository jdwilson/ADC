*************
ADC
*************

Commands
=============

Input ADC CLI to output equivalent NITRO JSON payload, execute flag is optional

.. parsed-literal::
   clicmdnitro -clicmd "sh responder policy" -execute

Use Regex to set/bind on multiple entities

.. parsed-literal::
   set service /^.*/ -netProfile <Test>

Tricks
=============

Enable verbose cloud daemon logging for AWS deployments.  Remove file when done

.. raw:: html

   <pre><code class="language-bash">touch /flash/nsconfig/.cloudlog</code></pre>