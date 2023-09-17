#!/usr/bin/perl -wT
print "Content-type: text/html\n\n";
print "Hello, world!\n"
print "<html><head><title>Hello World</title></head>\n";
print "<body>\n";
print "<h2>Hello, world!</h2>\n";
print "</body></html>\n";
print <<EndOfHTML;
<html><head><title>Test Page</title></head>
<body>
<h2>Hello, world!</h2>
</body></html>
EndOfHTML
