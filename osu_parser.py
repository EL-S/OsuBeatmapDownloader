def parse(location):
    global inforamtion, sections, hit_objects
    with open(location, "r", encoding="utf8") as osu_file:
        map_data = False
        information = {}
        sections = []
        hit_objects = []
        for line in osu_file:
            if "[" in line:
                sections.append(line.strip())
                if line.strip() == "[HitObjects]":
                    map_data = True
            elif map_data:
                hit_objects.append(line.strip())
            if ":" in line:
                line_array = line.split(":")
                if not map_data: #a number means it is a hit object
                    information[line_array[0].strip()] = ":".join(line_array[1:]).strip()
        return information,sections,hit_objects

##for i,y in information.items():
##    print(i,y)
##for i in sections:
##    print(i)

##print("FilePath:",file_path)
##print("FileName:",file_name)
##print(" Title:",information['Title'])
##print(" TitleUnicode:",information['TitleUnicode'])
##print(" Artist:",information['Artist'])
##print(" ArtistUnicode:",information['ArtistUnicode'])
##print(" Creator:",information['Creator'])
##print(" Version:",information['Version'])
##print(" AudioFilename:",information['AudioFilename'])
##print(" BeatmapID:",information['BeatmapID'])
##print(" BeatmapID:","unknown")
##print(" BeatmapSetID:",information['BeatmapSetID'])
