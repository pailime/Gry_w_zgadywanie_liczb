from flask import Flask, request


app = Flask(__name__)

HTML_ONE = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guess The Number</title>
</head>
<body>
<h1>Imagine number between 0 and 1000!</h1>
<h2>I'll try to guess in 10 tries. </h2>
<p>The rules are simple: <br>
press correct button if the number is too small or too big.<br>
Hit "You WON!" if I guess.<br>
Just don't cheat :-)<br><br>
Press "OK!" if you are ready</p>

<form action="" method="POST">
    <input type="hidden" name="min" value="{}">
    <input type="hidden" name="max" value="{}">
    <input type="submit" name="OK!" value="OK!">
</form>
</body>
</html>
"""


HTML_TWO = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guess The Number</title>
</head>
<body>
<h1>Imagine number between 0 and 1000!</h1>
<h2>I'll try to guess in 10 tries. </h2>
<p>The rules are simple: <br>
press correct button if the number is too small or too big.<br>
Hit "You WON!" if I guess.<br>
Just don't cheat :-)<br><br></p>
<h3>Is it number {guess}??</h3>

<form action="" method="POST">
    <input type="submit" name="user" value="TOO SMALL!">
    <input type="submit" name="user" value="TOO BIG!">
    <input type="submit" name="user" value="YOU WON!">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""

HTML_THREE = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guess The Number</title>
</head>
<body>
<h1>Hurra! I guess!</h1>
<h2>Your number is {guess}!</h2>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    if request.method == "GET":
        return HTML_ONE.format(0, 1001)
    else:
        min_num = int(request.form.get("min"))
        max_num = int(request.form.get("max"))
        user = request.form.get("user")
        guess = int(request.form.get("guess", 500))

        if user == "TOO SMALL!":
            min_num = guess
        elif user == "TOO BIG!":
            max_num = guess
        elif user == "YOU WON!":
            return HTML_THREE.format(guess=guess)

        guess = (max_num - min_num) // 2 + min_num

        return HTML_TWO.format(guess=guess, min=min_num, max=max_num)


if __name__ == '__main__':
    app.run()
