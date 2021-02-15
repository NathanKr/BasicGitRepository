<?php



if($_POST)
{
    $myMail="natankrasney@gmail.com";
    
    $to = $myMail;
    $subject = $_POST["subject"];
    $txt =  $_POST["question"];
    $headers = "From: ".$_POST["email"];

    
    $bServerMailStatus = mail($to,$subject,$txt,$headers);
    

}

?>

<!DOCTYPE html>
<html>

    <head>
        <script type="text/javascript" src="jquery.min.js"></script>
        
         <!-- Required meta tags always come first -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta http-equiv="x-ua-compatible" content="ie=edge">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.3/css/bootstrap.min.css" integrity="sha384-MIwDKRSSImVFAZCVLtU0LMDdON6KVCrZHyVQQj6e8wIEJkW4tvwqXrbMIya1vriY" crossorigin="anonymous">

        <style type="text/css">
            .alert
            {
                display: none;
            }
            
        </style>

    </head>
    
    <body>
        
        
        <div class="container">
            <h1>Get In Touch !</h1>
            <div id="success" class="alert alert-success" role="alert">
              <strong>Well done!</strong> Submit is success.
            </div>
            <div id="errorEmail" class="alert alert-danger" role="alert">
                <strong>Error !  </strong>Email is not valid
            </div>
            <div id="errorSubject" class="alert alert-danger" role="alert">
                <strong>Error !  </strong>Subject can not be empty
            </div>
            <div id="errorQuestion" class="alert alert-danger" role="alert">
                <strong>Error !  </strong>Question can not be empty
            </div>
            
            <form  method="post">
              <div class="form-group">
                <label for="exampleInputEmail1">Email address</label>
                <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" name="email">
                <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
              </div>
  
                <div class="form-group">
                    <label for="formGroupExampleInput2">Subject</label>
                    <input type="text" class="form-control" id="formGroupExampleInput2" name="subject">
                </div>
                
              <div class="form-group">
                <label for="exampleTextarea">What would you like to ask us ?</label>
                <textarea class="form-control" id="exampleTextarea" rows="3" name="question"></textarea>
              </div>
                
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
  	   </div>

        
          <!-- jQuery first, then Tether, then Bootstrap JS. -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.0.0/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.2.0/js/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.3/js/bootstrap.min.js" integrity="sha384-ux8v3A6CPtOTqOzMKiuo3d/DomGaaClxFYdCu2HPMBEkf6x2xiDyJ7gkXU0MWwaD" crossorigin="anonymous"></script>

        
        <script type="text/javascript">	
            var elemjQuerySuccess = $("#success"),
                elemjQueryEmail =  $("#exampleInputEmail1"),
                elemjQuerySubject = $("#formGroupExampleInput2"),
                elemjQueryQuestion = $("#exampleTextarea");
            
            
          var  serverMailStatus = "<?php echo $bServerMailStatus?>";
          
            
          if(serverMailStatus)
              {
                    elemjQuerySuccess.show();
              }
            
		  $("button").click(function(){
              
              $(".alert").hide();
              
              
              if(!emailValidationIsOk())
                  {
                      $("#errorEmail").show();
                  }
              
                if(!subjectValidationIsOk())
                  {
                      $("#errorSubject").show();
                  }
                  
                  if(!questionValidationIsOk())
                  {
                      $("#errorQuestion").show();
                  }
          })
          
          // --- if false then info will not be submitted to server
          $("form").submit(function(){
              return validationIsOk();
          });
		
          
          
          function emailValidationIsOk()
          {
              var regex = 
                    /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
              return regex.test(elemjQueryEmail.val());     
          }
            
          function subjectValidationIsOk()
          {
                return (elemjQuerySubject.val() != "");
          }
        
          function questionValidationIsOk()
          {
                return (elemjQueryQuestion.val() != "");
          }
            
          function validationIsOk()
          {
                var bIsValid =  emailValidationIsOk() &&
                       subjectValidationIsOk() &&
                       questionValidationIsOk();
              
              console.log("bIsValid : "+bIsValid);
             
              return bIsValid;
          }
		
		</script>
        
    </body>

</html>
