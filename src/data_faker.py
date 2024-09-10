from faker import Faker



def generator_name_list ( n: int, localization: str = 'en_US' ) -> list[ str ]:
  # possible locales: [ en_US, it_IT, ja_JP, es_ES, ... ]
  fake = Faker ( locale=localization )
  l = [ ]
  for _ in range ( 0, n ):
    l.append ( fake.name( ) )
  return l

def generator_tokens_unique_list ( word_list: set[ str ], n: int = -1 ) -> set [ str ]:
  fake = Faker ( )

  if n == -1:
    n = fake.random_int ( min=0, max=len(word_list)-1 )

  tokens = fake.random_elements ( elements=word_list, length=n, unique=True )
  return tokens

