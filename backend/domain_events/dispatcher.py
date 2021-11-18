class Dispatcher:
    def __init__(self):
        self._handlers = {}

    def register(self, event_type, handler):
        if event_type in self._handlers:
            self._handlers[event_type].append(handler)
        else:
            self._handlers[event_type] = [handler]

    def handle(self, event):
        event_type = type(event)

        for handler in self._handlers[event_type]:
            # Good place to sends metrics like how much time it takes to execute
            # catch some exceptions emitted by the Handler...
            handler()(event)
