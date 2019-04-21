from app import app


def test_home_route():
    result = app.test_client().get('/')
    app.config['Testing'] = True
    data = result.data.decode()
    assert result.status_code == 200
    assert isinstance(data, str)

def test_vocab_route():
    result = app.test_client().get('/vocabulary')
    app.config['Testing'] = True
    data = result.data.decode()
    assert result.status_code == 200
    assert isinstance(data, str)
