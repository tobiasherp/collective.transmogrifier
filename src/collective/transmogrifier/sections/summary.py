from zope.interface import classProvides, implements

from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.sections.pathresolver import boolean


class SummarySection(object):
    """
    For development: print a summary of items seen by every section
    (which creates a count function, see below)
    """
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        """
        options:
        verbose -- print summary even when no counters found
        count -- make this section count its items as well
        """

        self.previous = previous
        self.verbose = boolean(options.get('verbose', 'false'))
        self.print_sections = boolean(options.get('print-sections', 'false'))
        self.transmogrifier = transmogrifier
        if boolean(options.get('count', 'false')):
            # create the counter:
            self.count = transmogrifier.create_itemcounter(name)
        else:
            self.count = None

    def __iter__(self):
        """
        Forward any items, and finally print a summary
        """
        count = self.count
        if count is None:
            for item in self.previous:
                yield item
        else:
            # if this section sees any items, the summary below won't be empty
            for item in self.previous:
                yield item
                count('passed-through')

        self.transmogrifier.print_itemcounters(self.verbose)
        if self.print_sections:
            from pdb import set_trace
            set_trace()
            dic = dict(transmogrifier)
