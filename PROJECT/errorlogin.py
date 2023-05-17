```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ERROR</title>
    <link rel="stylesheet" href="/static/errorlogin.css">
</head>
<body>
    <h1> &#128681; UPS! Something went wrong with your login &#128681;</h1>
    <br><br>
    <h2> Check for the following mistakes that might be preventing you from loging into &#128218;LITPALS&#128218;:</h2>
    <br><br>
    <p> &#128270; Incorrect password.</p>
    <br><br>
    <p> &#128270; Incorrect username</p>
    <br><br>
    <p> &#128270; Check any misspellings in your login information</p>
    <br><br>
    <h3> Please try again! Click the following button to return to the login screen: </h3>
    <button type="button" class="button1">
            <a href="{{ url_for("welcome")}}">Log in</a>
    </button>
</body>
</html>
```.py
