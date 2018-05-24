<?
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in, $key) {
    // $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$cookie = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw");
$in = json_encode($defaultdata);

// get the key

$key = xor_encrypt($cookie, $in);

echo "key: " . $key . "\n";
echo "should be default data: " . (xor_encrypt($cookie, $key)) . "\n";


// get the new cookie

$key = "qw8J";
$defaultdata['showpassword'] = "yes";
$new = base64_encode(xor_encrypt(json_encode($defaultdata), $key));
echo "new cookie: " . $new . "\n";

?>