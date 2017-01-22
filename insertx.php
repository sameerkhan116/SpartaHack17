<?php

$db_host = 'localhost';
$db_username = 'root';
$db_password = '';
$db_name = 'Blog';

mysql_connect( $db_host, $db_username, $db_password) or die(mysql_error());

mysql_select_db($db_name);

if (isset($_POST['submit'])) {
$rname = $_POST['rname'];
$city = $_POST['city'];
$Title = $_POST['Title'];
$content = $_POST['content'];
$datex = date( 'Y-m-d H:i:s' );

$order = mysql_query("INSERT INTO blog_post (rname, city, Title, content, datex) VALUES ('$rname', '$city', '$Title', '$content', '$datex') ");

if ($order) {
    echo '<br>Input data is successful';
    $command = escapeshellcmd('sparta.py');
    $output = shell_exec($command);
} else {
    echo '<br>Input data is not valid';
}
}
?>