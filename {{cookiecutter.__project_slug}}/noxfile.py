import nox


@nox.session(python=["3.10"], reuse_venv=True)
def tests(session):
    session.install('pytest')
    session.run('pytest')


@nox.session(python=["3.10"], reuse_venv=True)
def coverage(session):
    session.install('coverage[toml]')
    session.run('coverage', 'combine')
    session.run('coverage', 'report')


@nox.session(python=["3.10"], reuse_venv=True)
def mypy(session):
    session.install('mypy')
    session.run('mypy', 'src')


@nox.session(python=["3.10"], reuse_venv=True)
def pre_commit(session):
    session.install('pre-commit')
    session.run('pre-commit', 'run', '--all-files')


@nox.session(python=["3.10"], reuse_venv=True)
def docs(session):
    session.install('sphinx', 'sphinx-rtd-theme')
    session.run(
        'sphinx-build',
        '-T',
        '-b',
        'html',
        'docs',
        'docs/_build/html',
    )
    session.run(
        'sphinx-build',
        '-T',
        '-b',
        'doctest',
        'docs',
        'docs/_build/html',
    )
