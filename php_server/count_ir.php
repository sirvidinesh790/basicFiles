<?php
if(isset($_GET['light'])){
    $light = $_GET['light'];
    
    if($light == "on") {
      $file = fopen("bulb.txt", "w") or die("can't open file");
      fwrite($file, '1');
      fclose($file);
    } 
    else if ($light == "off") {
      $file = fopen("bulb.txt", "w") or die("can't open file");
      fwrite($file, '0');
      fclose($file);
    }

}

?>

<html>
  <head>      
    
    
    <title>LED for Khushbu</title>
  
  </head>
  <body>
        <a href="google.com" >Turn On</a>
        <br />

        <a href="google.com/search/?q=rishikesh" >Turn Off</a>
        <br />

  </body>
</html>

