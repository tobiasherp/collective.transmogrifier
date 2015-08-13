import transaction
from zope.interface import classProvides, implements
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection


class SavepointSection(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.every = int(options.get('every', 1000))
        self.previous = previous
        self.count = transmogrifier.create_itemcounter(name)

    def __iter__(self):
        count_ = self.count
        count = 0
        for item in self.previous:
            count_('got')
            count = (count + 1) % self.every
            if count == 0:
                count_('commits')
                transaction.savepoint(optimistic=True)
            count_('forwarded')
            yield item
