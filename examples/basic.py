import concurrent.interpreters as interpreters
from textwrap import dedent

interp = interpreters.create()

# Run in the current OS thread.

interp.exec('print("spam!")')

interp.exec(
    """if True:
    print('spam!')
    """
)

interp.exec(
    dedent(
        """
    print('spam!')
    """
    )
)


def run():
    print("spam!")


interp.call(run)

# Run in new OS thread.

t = interp.call_in_thread(run)
t.join()
