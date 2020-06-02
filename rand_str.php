<?php
function random($length) {
	$hash = '';
	$chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz';
	$max = strlen($chars) - 1;
	PHP_VERSION < '4.2.0' && mt_srand((double)microtime() * 1000000);
	for($i = 0; $i < $length; $i++) {
		$hash .= $chars[mt_rand(0, $max)];
	}
	return $hash;
}
$fp = fopen('result1.txt', 'r');
$fp2 = fopen('result2.txt', 'a');
while(!feof($fp)){
	$b = fgets($fp, 4096);
	if(preg_match("/([=\s].*[=\s])(\d+)[\s]/", $b, $matach)){
		$m = $matach[2];
	}else{
		continue;
	}
	// var_dump($matach);
	// var_dump($m);
	mt_srand($m);
	fwrite($fp2, random(10)."\n");
}
fclose($fp);
fclose($fp2);