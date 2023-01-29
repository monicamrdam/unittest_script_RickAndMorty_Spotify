from app.RickAndMortyPopulator.character.character_repository import CharacterRepository


class DbRickAndMortySpotify:

    def __init__(self):
        pass

    @staticmethod
    def create_table_characters():
        CharacterRepository.create_tables()

