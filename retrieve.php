<?php
   $dbhost = 'localhost';
   $dbuser = 'root';
   $dbpass = '';
   $db_name = 'Blog';

   $conn = mysql_connect($dbhost, $dbuser, $dbpass);
   
   if(! $conn ) {
      die('Could not connect: ' . mysql_error());
   }
   
   $sql = 'SELECT * FROM blog_post';
   mysql_select_db($db_name);
   $retval = mysql_query( $sql, $conn );
   
   if(! $retval ) {
      die('Could not get data: ' . mysql_error());
   }
   
   while($row = mysql_fetch_assoc($retval)) {
      echo "Restaurant:{$row['rname']}  <br> ".
         "Location: {$row['city']} <br> ".
         "Title: {$row['Title']} <br> ".
         "Description: {$row['content']} <br> ".
         "--------------------------------<br>";
   }
   
   echo "Fetched data successfully\n";
   
   mysql_close($conn);
?>