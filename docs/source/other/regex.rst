*************
Regular Expressions
*************

Useful Regex 
=============

IPv4 Address

.. raw:: html

   <pre><code class="language-regex">(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}</code></pre> 

URL with or without protocol

.. raw:: html

   <pre><code class="language-regex">/(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/</code></pre>