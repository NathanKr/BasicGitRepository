<?php

$strWeatherReport = "";
$Error = "";


if($_POST)
{
    $strCity=$_POST["city"];

    $str = @file_get_contents("http://www.weather-forecast.com/locations/".$strCity."/forecasts/latest");

    if($str)
    {
        $strEnd="span";

        $strStart="3 Day Weather Forecast Summary";


        // -- 103 is size 
        $startOfWeatherPos = strpos($str,$strStart) + 119;
        $startOfWeatherEndPos = strpos($str,$strEnd,$startOfWeatherPos);
        $len = $startOfWeatherEndPos - $startOfWeatherPos +1;
        $strWeatherReport = substr($str , $startOfWeatherPos ,  $len);
    }
    
        if($strWeatherReport)
        {
            $Error = "";
        }
        else
        {
            $Error = "Could not get weather";
        }
}



?>



<!DOCTYPE html>
<html>

    <head>
        <script type="text/javascript" src="jquery.min.js"></script>
        <title>Weather Scraper</title>
         <!-- Required meta tags always come first -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta http-equiv="x-ua-compatible" content="ie=edge">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.3/css/bootstrap.min.css" integrity="sha384-MIwDKRSSImVFAZCVLtU0LMDdON6KVCrZHyVQQj6e8wIEJkW4tvwqXrbMIya1vriY" crossorigin="anonymous">

        <style type="text/css">
            
            body
            {
                width: 100%;
                height: 100%;
                background-image:url("photo_weather_scrapper1.jpg");
                background-size: cover;
            }
            
            .container
            {
                padding-top: 100px;
                text-align: center;
                width: 400px;
            }
            
            form
            {
                margin-bottom: 20px;
            }
            
            .alert
            {
                display: none;
            }
        </style>

    </head>
    
    <body>
        <!-- jQuery first, then Tether, then Bootstrap JS. -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.0.0/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.2.0/js/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.3/js/bootstrap.min.js" integrity="sha384-ux8v3A6CPtOTqOzMKiuo3d/DomGaaClxFYdCu2HPMBEkf6x2xiDyJ7gkXU0MWwaD" crossorigin="anonymous"></script>

        <div class="container">
            <h2>What's the Weather ?</h2>
            <p>Enter the name of city</p>
            
            <form method="post">
                <div class="form-group">
                    <input type="text" class="form-control" name="city" placeholder="E.g. Tokyo">
                </div>
  
               <button type="submit" class="btn btn-primary">Submit</button>
            </form>
            
            <div id="success" class="alert alert-success" role="alert">
                You successfully read this important alert message.
            </div>
        
            <div id="error" class="alert alert-danger" role="alert">
                <strong>Error !</strong>
            </div>
        </div>
        
        <script type="text/javascript">	
           
            var strWeatherReport = "<?php echo $strWeatherReport ?>";
            var strError = "<?php echo $Error ?>";
            
            if(strWeatherReport)        
                {
                    $("#success").html(strWeatherReport);
                    $("#success").show();
                }
            else if(strError)
                {
                    $("#error").html(strError);
                    $("#error").show();
                }
		</script>
        
    </body>

</html>
