<html>
<head>
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="css/custom.css">
<link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
<link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
<title>Home</title>

<body>
<nav class="navbar navbar-custom navbar-default navbar-fixed-top" role="navigation">
  <div class="container-fluid">
    <div class="navbar-header page-scroll">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#main-nav-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a href="index.php" class="navbar-brand">TDGP</a>
    </div>
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
          <li><a href="insert.html">New Post</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="subscriber.html">Subscribe</a></li>
        </ul>
    </div>
  </div>
</nav>

<header class = "intro-header" style="background-image: url('img/home-bg.jpg')">

<div class = "container">
  <div class = "row">
    <div class = "col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
      <div class = "site-heading">
        <h1>THE DO GOOD PROJECT</h1>
        <h2>We will end world hunger</h2>
        <hr class="small">
        <span class = "subheading">No, we're not kidding.</span>
      </div>
    </div>
  </div>
</div>
</header>
    
<h1 class = 'text-center'>Latest Posts</h1>
<?php include 'insertx.php';

$con = mysql_connect("localhost","root","");
 
if (!$con)
{
  die('Could not connect: ' . mysql_error());
}

$db_name = 'Blog';

mysql_select_db("$db_name");

$query = "SELECT * FROM blog_post order by sid DESC LIMIT 10";

$comments = mysql_query($query) or trigger_error(mysql_error().$query);;
    
while($row = mysql_fetch_array($comments, MYSQL_ASSOC))
{
  $rname = $row['rname'];
  $Title = $row['Title'];
  $content = $row['content'];
  $datex = $row['datex'];
  
  $rname = htmlspecialchars($row['rname'],ENT_QUOTES);
  $Title = htmlspecialchars($row['Title'],ENT_QUOTES);
  $content = htmlspecialchars($row['content'],ENT_QUOTES);
  $datex = htmlspecialchars($row['datex'],ENT_QUOTES);
  
  echo " 
  <div class = 'container'>
    <div class = 'row'>
      <div class = 'col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1'>
        <div class = 'post-preview'>
        <a>
        <h2 class ='post-title'>
          Restaurant: $rname
          </h2>
        <h3 class = 'post-subtitle'>
        Title: $Title<br />
        Description: $content<br />
        </h3>
        Posted: $datex
        </div>
        </a>
      </div>
    </div>
  </div>
  ";
}
?>
</body>
</head>
</html>