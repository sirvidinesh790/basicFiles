<?php
if(isset($_GET['count'])){
    
    $current_count = $_GET['count'];
    
    $file = fopen("count.txt", "w") or die("can't open file");
    fwrite($file, $current_count);
    fclose($file);

}

?>

<html>
  <head>      
    
    
    <title>LED for Khushbu</title>
      
  </head>
  <body>
       <h1>See coount.txt page for counter </h1>

  </body>
</html>

