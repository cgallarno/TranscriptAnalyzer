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

def find_common_chunks(transcript1, transcript2):
    try:
        matched_chunks = []
        for chunk1 in transcript1:
            # skip comparing one word transcripts
            if ' ' not in chunk1['text']:
                continue
            for chunk2 in transcript2:
                if ' ' not in chunk2['text']:
                    continue
                # Using levenshtein distance to account for minor variances in YouTubes automatic captioning
                similarity = normalize_levenshtein_distance(chunk1['text'], chunk2['text'])
                if similarity > 0.7: 
                    matched_chunks.append((chunk1, chunk2, f"{similarity:.2f}"))

        return matched_chunks
    except Exception as e:
        print(f"Error finding common chunks: {e}")
        return []


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0 or not args:
        print("No video IDs provided")
        exit()

    transcripts = fetch_transcript(args)
    print("Successfully fetched transcripts")

    #print(transcripts)
    common_chunks = find_common_chunks(transcripts[args[0]], transcripts[args[1]])
    print(f"Matched Chunks: {len(common_chunks)}")

    # TODO: Normalize common chunks against total chunks

    print(json.dumps(common_chunks))
# End of file
