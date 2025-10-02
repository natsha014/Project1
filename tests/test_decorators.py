from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    result = capsys.readouterr()
    assert result.out == "my_function ok\n\n"


def test_log_err(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    result = capsys.readouterr()
    assert (
        result.out == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n\n"
    )


def test_log_err_file():
    @log(filename="mylogerr.txt")
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    with open("mylogerr.txt") as f:
        line = f.readline()
        assert line == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"


def test_log_file():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("mylog.txt") as f:
        line = f.readline()
        assert line == "my_function ok\n"
