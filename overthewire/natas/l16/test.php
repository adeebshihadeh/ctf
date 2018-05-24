<?php

$key = "$(cat test.php)";

$cmd = "grep -i \"$key\" dictionary.txt" . "\n";
echo $cmd;
passthru($cmd);

// -i = ignore case distinctions

?>