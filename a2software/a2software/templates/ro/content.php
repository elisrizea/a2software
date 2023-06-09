<?php
if (isset($_GET['acasa']))
include('pagini/acasa.php');
elseif (isset($_GET['contact']))
include('pagini/contact.php');
elseif (isset($_GET['despre-noi']))
include('pagini/despre-noi.php');
elseif (isset($_GET['faqs']))
include('pagini/faqs.php');
elseif (isset($_GET['partener']))
include('pagini/partener.php');
elseif (isset($_GET['platforma-noastra']))
include('pagini/platforma-noastra.php');
elseif (isset($_GET['cookie']))
include('pagini/cookie.php');
elseif (isset($_GET['webapp']))
include('pagini/webapp.php');
elseif (isset($_GET['partener']))
echo"<script type='text/javascript'>window.open('http://www.example.com target=_blank');</script>";
//include('pagini/partener.php');

else include('pagini/acasa.php');





?>
