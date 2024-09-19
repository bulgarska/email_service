
def get_embed_link_google_drive(google_drive_link):
    
    splice_start = 0
    splice_end = -0
    for i in range(0, len(google_drive_link)):
        if google_drive_link[i] == '/' and google_drive_link[i-1] == 'd':
            splice_start = i + 1
        if google_drive_link[i] == 'v' and google_drive_link[i-1] == '/':
            splice_end = -(len(google_drive_link) - (i - 1))

    unique_id_image = google_drive_link[splice_start:splice_end]

    embed_link = f'https://drive.google.com/thumbnail?id={unique_id_image}'
    
    return embed_link

if __name__ == "__main__":
    links = ['list of google drive links to generate embed links for',]
    for link in links:
        print(get_embed_link_google_drive(link))

