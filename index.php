<?php
if (isset($_GET['shop'])){
header("Location: https://store.a2.software/ro/");
die();
}
include('header.php');
include('menu.php');
include('content.php');
include('footer.php');
?>