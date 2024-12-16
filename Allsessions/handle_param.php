<?php

  $data_array = json_decode(file_get_contents('php://input'), true);
  $keys = array_keys($data_array); 
  echo print_r($keys);
  $subid = $data_array["subid"];
  echo $subid;


   if ($data_array != null)
   {
     $file = fopen("/var/www/html/gen_pilot/allparam.json", "a+") or die("Unable to open file!");
     fwrite($file, $data_array["data"]."\n");
     fclose($file);

   }
   else
   {

   }
?>
