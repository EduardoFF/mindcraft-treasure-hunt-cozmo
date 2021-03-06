.. _quickstart:

Quickstart
=============

Eager to get started? This page gives a good introduction. It assumes you
already have the library installed. If you do not, head over to the
:ref:`installation` section.


A Minimal Application (The Standard way)
-----------------------------------------------

A minimal application looks something like this:

.. literalinclude:: /../examples/demo_helloworld.py

So what did that code do?

1. First we imported the library.
2. Next we define a function that will represent our script.
3. Inside the function we use the :meth:`~say` make Cozmo saying "hello".
4. Lastly, in the main part of the file, we use the :meth:`run_program_with_viewer` passing our function as argument to execute our script.

Just save it as :file:`hello.py` or something similar.

To run the application you can either use the :command:`python` command or run
it inside your IDE.
.. Before you can do that probably need to our the mindcraft_treasure_hunt_with_cozmo folder to your PYTHONPATH.

A Minimal Application (Using PyCozmo)
-----------------------------------------

A minimal application using the PyCozmo tool looks something like this:

.. literalinclude:: /../examples/flat/demo_helloworld.py

So what did that code do?

We use the :meth:`~say` make Cozmo saying "hello".

Note that we didn't even have to import the library. This is because we run our code with the :file:`pycozmo.py` tool that takes care of all that.

Just save it as :file:`hello.py` or something similar and run it like this::

  pycozmo.py hello.py
