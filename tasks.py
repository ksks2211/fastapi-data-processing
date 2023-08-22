from invoke import task


@task
def start(c):
    c.run('uvicorn main:app --reload')


@task
def production(c):
    command = (
        "gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000"
    )
    c.run(command)