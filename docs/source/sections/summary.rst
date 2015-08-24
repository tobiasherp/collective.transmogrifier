Summary section
===============

A summary pipeline section doesn't change the pipeline data in any way; it
simply prints the counters of the previous sections.  If those sections didn't
use the counting facility, it doesn't do much apart from the mandatory
forwarding of items.
The summary section blueprint name is
``collective.transmogrifier.sections.summary``.

The correctness of the summary depends on the correct usage of the counting
function, created by each section using the ``create_itemcounter`` method of
the ``Transmogrifier`` class.
An example output could look like this::

    [section1]
    created:    42
    [section2]
    got:          42
    forwarded:    42
