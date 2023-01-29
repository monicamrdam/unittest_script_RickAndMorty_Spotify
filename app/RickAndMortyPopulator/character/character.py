class Character:
    def __init__(self, id, name, location, episode: []):
        self.id = id
        self.name = name
        self.location = location
        self.episode = episode

    def __str__(self):
        return "Id {},Name {}, Location {}, Episode {}".format(
            self.id, self.name, self.location, self.episode
        )

    def serialize(self):
        return {
            'Id': self.id,
            'Name': self.name,
            'Location': self.location,
            'Episode': self.episode,
        }
