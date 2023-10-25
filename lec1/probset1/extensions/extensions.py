name = input("File name: ").strip()

# Extract extensions
ext = name[name.rfind('.')+1:].lower()

# Match media type
match ext:
    case 'gif':
        mt = 'image/gif'
    case 'jpg' | 'jpeg':
        mt = 'image/jpeg'
    case 'png':
        mt = 'image/png'
    case 'pdf':
        mt = 'application/pdf'
    case 'txt':
        mt = 'text/plain'
    case 'zip':
        mt = 'application/zip'
    case _:
        mt = 'application/octet-stream'

print(mt)