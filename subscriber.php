<?php

$db_host = 'localhost';
$db_username = 'root';
$db_password = '';
$db_name = 'Blog';

mysql_connect( $db_host, $db_username, $db_password) or die(mysql_error());

mysql_select_db($db_name);

if (isset($_POST['submit'])) {
$city = $_POST['city'];
$phonen = $_POST['phonen'];
$carrier = $_POST['carrier'];

$order = mysql_query("INSERT INTO subscribers (city, phonen, carrier) VALUES ('$city', '$phonen', '$carrier') ");

if ($order) {
    echo '<br>Input data is successful';
} else {
    echo '<br>Input data is not valid';
}
}
?>