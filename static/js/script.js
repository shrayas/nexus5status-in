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

  function setUpdateTime(timestamp){
    $("#last-updated-string").html("");
    $("#last-updated-string").html(timestamp);
  }

  function clearUpdateTime(){
    $("#last-updated-line").html("");
  }

  function checkStatus(){

    function checkStatusSuccess(json){

      if (json.status){
        setAvailable();
      }
      else{
        setUnAvailable();
      }

      setUpdateTime(json.timestamp);

    }

    function checkStatusFailure(){
      setError();
      clearUpdateTime();
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
