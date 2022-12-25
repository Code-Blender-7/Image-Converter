import time

from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, BarColumn


# for i in track(range(20), description="Working..."):
#     time.sleep(1)

progress = Progress(
    SpinnerColumn(),
    *Progress.get_default_columns(), # get default settings
    "Elapsed:", TimeElapsedColumn(), # this is a slacked display. Read Docs of Rich before making changes.
    transient=True # clear progress bar + others after completion/end
    )

# with Progress(transient=True, expand=True) as progress:
with progress:
    task1 = progress.add_task("[red]Scanning your DMS....", total=10)
    

    while not progress.finished:
        progress.update(task1, advance=1)
        time.sleep(1)
