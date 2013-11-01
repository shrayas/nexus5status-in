$(function(){

  function setAvailable(){
    $("#status").html("");
    $("#status").html("available!!");
  }

  function setUnAvailable(){
    $("#status").html("");
    $("#status").html("unavailable");
  }

  function setError(){
    $("#status").html("");
    $("#status").html("unknown");
  }

  function checkStatus(){

    function checkStatusSuccess(json){

      if (json.status){
        setAvailable();
      }
      else{
        setUnAvailable();
      }

    }

    function checkStatusFailure(){
      setError();
    }

    URL = "/up";

    $.ajax({
      url:URL,
      success:checkStatusSuccess,
      error:checkStatusFailure,
      dataType:"json"
    });
  }

  checkStatus();

});
