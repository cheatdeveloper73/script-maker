file = open("cpp.txt", "r")

iterator = 0

name_of_class = ""
class_properties = []

things_to_remove = ["struct", "__declspec(align(8))", "{", "};", ";"]
valid_types = ["bool", "float", "int", "int32_t", "uint16_t", "double", "System_String_o&"]

register_object_type = r'CHECK(scriptengine->RegisterObjectType("REPLACEME", sizeof(REPLACEME), asOBJ_VALUE | asOBJ_POD));'
register_object_property = r'CHECK(scriptengine->RegisterObjectProperty("CLASS", "TYPE NAME", asOFFSET(CLASS, CLASS::NAME)));'

for line in file:

    for word in things_to_remove:

        n = line.replace(word, "")
        line = n.strip()

    iterator += 1

    if (iterator == 1):
        name_of_class = line.split()[0]
        continue

    if (line == ""):
        continue
    
    line = line.replace("*", "&")

    strings = line.split()
    if (strings[0] not in valid_types): continue
    strings[0] = strings[0].replace("uint16_t", "uint")
    strings[0] = strings[0].replace("int32_t", "int")
    
    class_properties.append({"type" : strings[0], "name" : strings[1]})

print("{")

print(register_object_type.replace("REPLACEME", name_of_class))

for property in class_properties:
    registered_property = ""
    registered_property = register_object_property.replace("CLASS", name_of_class)
    registered_property = registered_property.replace("NAME", property["name"])
    registered_property = registered_property.replace("TYPE", property["type"])
    print(registered_property)

print(register_object_type.replace("REPLACEME", name_of_class.replace("_Fields", "_o")))
fields = register_object_property
fields = fields.replace("CLASS", name_of_class.replace("_Fields", "_o"))
fields = fields.replace("NAME", "fields")
fields = fields.replace("TYPE", name_of_class)
print(fields)



print("}")