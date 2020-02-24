<?php
header("Content-Type:application");
require "data.php";

if(!empty($_GET['name']))
{
	$name=$_GET['name'];
	$price = get_price($name);

	if(empty($price))
	{
		response(NULL);
	}
	else
	{
		response($price);
	}
}
else
{
	response(NULL);
}

function response($data)
{
	header("HTTP/1.1 ");
	
	echo $data;
}

?>
