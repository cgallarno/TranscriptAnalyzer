import sys
import json
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from nltk.metrics import edit_distance


def normalize_levenshtein_distance(s1, s2):
    distance = edit_distance(s1, s2)
    max_len = max(len(s1), len(s2))
    similarity = 1 - (distance / max_len) 
    return similarity

def fetch_transcript(video_ids):
    try:
        transcripts, _ = YouTubeTranscriptApi.get_transcripts(video_ids)
        return transcripts
    except Exception as e:
        print(f"Error fetching transcripts: {e}")
        return {}

def find_common_chunks(transcripts):
    try:
        [video_id_1, video_id_2] = list(transcripts.keys())

        transcript_1 = transcripts[video_id_1]
        transcript_2 = transcripts[video_id_2]

        print(f"Given videos in this order: {video_id_1}, {video_id_2}")

        # Ensure the shorter transcript is used on the outerloop,
        # creating (somewhat) consistent runtimes for very differently lengthed transcripts
        if len(transcript_1) > len(transcript_2):
            transcript_1, transcript_2 = transcript_2, transcript_1
            video_id_1, video_id_2 = video_id_2, video_id_1

        print(f"Determined video_id {video_id_1} is shorter")

        matched_chunks = []
        for chunk_1 in transcript_1:
            # skip comparing one word transcripts, also remove "[Music]", and explecitves placeholder.
            if ' ' not in chunk_1['text']:
                continue
            for chunk_2 in transcript_2:
                if ' ' not in chunk_2['text']:
                    continue

                # Using levenshtein distance to account for minor variances in YouTubes automatic captioning
                # This is an expensive operation inside of doubly nested loop.
                # Consider other algorithims such as LCS or n-gram, and hashing to avoid multiple loops    
                similarity = normalize_levenshtein_distance(chunk_1['text'], chunk_2['text'])
                if similarity > 0.6: 
                    chunk_1['video_id'] = video_id_1
                    chunk_2['video_id'] = video_id_2
                    # TODO: Refactor into a MatchResult class
                    yield (chunk_1, chunk_2, f"{similarity:.2f}")

        return matched_chunks
    except Exception as e:
        print(f"Error finding common chunks: {e}")
        return []


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0 or not args:
        print("No video IDs provided")
        exit()

    # returns a dict of { video_id: transcript_chunks }
    transcripts = fetch_transcript(args)
    print("Successfully fetched transcripts")

    matched_chunks = 0
    for chunk in find_common_chunks(transcripts):
        matched_chunks += 1
        print(f'===== Similarity {chunk[2]} ======')
        print(f"({chunk[0]['start']}) {chunk[0]['text']} - https://www.youtube.com/watch?v={chunk[0]['video_id']}&t={chunk[0]['start']}s")
        print(f"({chunk[1]['start']}) {chunk[1]['text']} - https://www.youtube.com/watch?v={chunk[1]['video_id']}&t={chunk[1]['start']}s")
        print("===================================") 

    print(f"Matched Chunks: {matched_chunks}")
    print(f"Similarity across entire video: {matched_chunks / min(len(transcripts[args[0]]), len(transcripts[args[1]]))}")

   # print(json.dumps(common_chunks))
# End of file
