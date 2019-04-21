from backend_epithet_generator.app import app


def test_home_route():
    result = app.test_client().get('/')
    app.config['Testing'] = True
    data = result.data.decode()
    assert result.status_code == 200
    assert isinstance(data, str)

def test_vocab_route():
    result = app.test_client().get('/vocabulary')
    app.config['Testing'] = True
    assert result.status_code == 200
    data = result.data.decode()
    assert isinstance(data, str)


def test_random_route():
    result = app.test_client().get('/random')
    app.config['Testing'] = True
    assert result.status_code == 200
    data = result.data.decode()
    assert isinstance(data, str)