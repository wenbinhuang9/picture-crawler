// Setup the main game logic.
(function () {
  console.log("main js starts here ");
  var submitBtn = document.getElementById('submit-url');
  var urlTxt = document.getElementById('search-str');
  submitBtn.addEventListener('click',   function submitUlr(e) {
    log.console("begin submiturl")
    url = "http://127.0.0.1:5000/download";
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open( "POST", url, true ); // false for synchronous request
    xmlHttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    var urldata = urlTxt.value;
    console.log(urldata);
    var encodeurl =  window.btoa(urldata);
    console.log(encodeurl)
    var data = 'encodeurl=' + encodeurl;

    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4) {
            if (xmlHttp.status == 200) {
                var data = xmlHttp.responseText;
                console.log(data)
            }
        }
    };
    xmlHttp.send(data);
  });


 }
)();
