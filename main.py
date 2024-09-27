import sys
import sqlite3
from youtube_transcript_api import YouTubeTranscriptApi

def fetch_transcript(video_ids):
    try:
        transcripts = YouTubeTranscriptApi.get_transcripts(video_ids)[0]
        print("Transcript fetched successfully.")

        # Insert all transcripts into the database
        for video_id, transcript in transcripts.items():
            cursor.execute("INSERT INTO transcripts (tokenized_text, video_id) VALUES (?, ?)", (f"{transcript}", video_id))
            
        # print(transcripts[0]['VeH1fynKu6w'])
        # print(transcripts[0]['6KxT-yGbvBo'])
        #for video_id, transcript in transcripts.items():
            #for entry in transcript:
                # print(f"{entry['start']}: {entry['text']}")
    except Exception as e:
        print(f"Error fetching transcript: {e}")

    print('listing contents of database:')
    rows = cursor.execute("SELECT * FROM transcripts").fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    connection = sqlite3.connect("parsed_video_transcripts.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS transcripts (tokenized_text TEXT, video_id TEXT)")

    args = sys.argv[1:]
    if len(args) == 0 or not args:
        print("No video IDs provided")
        exit()


    fetch_transcript(args)

    connection.commit()
    connection.close()
# End of file

 
