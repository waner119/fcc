from flask import Flask, render_template


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)


user = {'username': 'Li', 'bio': 'A boy who loves movies.'}

movies = [
    {
        'name': 'Forrest Gump',
        'year': '1994'
    },
    {
        'name': 'Perfect Blue',
        'year': '1997'
    },
    {
        'name': 'The Matrix',
        'year': '1999'
    },
    {
        'name': 'Memento',
        'year': '2000'
    },
    {
        'name': 'The Bucket list',
        'year': '2007'
    },
]
