from invoke import task

@task
def run(ctx, script="pipeline.py"):
    """Runs the specified script (default is main Pipeline)"""
    ctx.run(f"python {script}")

@task
def format(ctx):
    """Format the code using ruff"""
    ctx.run("ruff format .")

@task
def install(ctx):
    """Install the required packages"""
    ctx.run("pip install -r requirements.txt")