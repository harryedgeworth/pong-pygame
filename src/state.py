class State():
    def handleEvents(self, events):
        pass

    def tick(self, clock):
        pass

    def blit(self, surface):
        pass

    def join(self, old_state=None):
        '''Runs when the user navigates to the state'''
        pass

    def leave(self, new_state=None):
        '''Runs when the user moves to a new state'''
        pass