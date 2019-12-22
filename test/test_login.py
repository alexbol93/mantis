
def test_login(app):
    # app.session.login("administrator", "root")
    pass
    assert app.session.is_logged_as("administrator")