import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('movies.xml')
root = tree.getroot()

# Using iter() to list all child tags of the movie element
print("Child tags of the movie elements:")
for movie in root.iter('movie'):
    for child in movie:
        print(child.tag)

# Using itertext() to print out the movie descriptions
print("\nMovie descriptions:")
for movie in root.iter('movie'):
    description = movie.find('description').itertext()
    print(''.join(description).strip())

# Counting favorite and non-favorite movies
fav_count = 0
non_fav_count = 0

for movie in root.iter('movie'):
    if movie.attrib.get('favorite') == 'True':
        fav_count += 1
    else:
        non_fav_count += 1

print(f"\nNumber of favorite movies: {fav_count}")
print(f"Number of non-favorite movies: {non_fav_count}")
