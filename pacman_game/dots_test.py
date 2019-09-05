from dots import Dots


def test_constructor():
    ds = Dots(600, 600, 150, 450, 150, 450)
    assert ds.WIDTH == 600
    assert ds.HEIGHT == 600
    assert ds.TH == 150
    assert ds.BH == 450
    assert ds.LV == 150
    assert ds.RV == 450
    assert len(ds.bottom_row) == len(ds.top_row) == ds.WIDTH//ds.SPACING + 1
    assert len(ds.left_col) == len(ds.right_col) == ds.HEIGHT//ds.SPACING + 1
    for i in range(len(ds.left_col)):
        assert ds.left_col[i].x == ds.LV
        assert ds.left_col[i].y == ds.SPACING * i
    for i in range(len(ds.right_col)):
        assert ds.right_col[i].x == ds.RV
        assert ds.right_col[i].y == ds.SPACING * i
    for i in range(len(ds.top_row)):
        assert ds.top_row[i].x == ds.SPACING * i
        assert ds.top_row[i].y == ds.TH
    for i in range(len(ds.bottom_row)):
        assert ds.bottom_row[i].x == ds.SPACING * i
        assert ds.bottom_row[i].y == ds.BH


def test_eat():
    """Tests the number of dots that will remain after
    Pacman reaches certain x,y coordinates"""
    ds = Dots(600, 600, 150, 450, 150, 450)

    assert len(ds.total) == 36
    ds.eat(0, ds.TH)
    assert len(ds.total) == 35
    ds.eat(0, ds.BH)
    assert len(ds.total) == 34
    ds.eat(ds.LV, 150)
    assert len(ds.total) == 32
    ds.eat(ds.RV, 225)
    assert len(ds.total) == 31
    ds.eat(ds.RV, 200)
    assert len(ds.total) == 31
    ds.eat(ds.RV, 49)
    assert len(ds.total) == 30


def test_dots_left():
    ds = Dots(600, 600, 150, 450, 150, 450)
    dl = ds.dots_left()
    assert dl == ((ds.WIDTH//ds.SPACING + 1) * 2 +
                  (ds.HEIGHT//ds.SPACING + 1) * 2)
