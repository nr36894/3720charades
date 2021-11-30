from datamuse import datamuse
api = datamuse.Datamuse()

countries = api.words(rel_jja='activity')
print(countries)