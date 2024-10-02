# TranscriptAnalyzer

Compare the transcripts of two or more YoutTube videos and determine if the creators are having conversations available in both videos.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/cgallarno/TranscriptAnalyzer.git
cd TranscriptAnalyzer
```

2. Create / activate virtual envrionment (optional)

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Use it!

#### Videos in common:

##### Minecraft (lots of identical matches)

```bash
python3 main.py gam8OM_7Wn8 VPZlLr3hkd4
```

##### Among us

```bash
python3 main.py VeH1fynKu6w 6KxT-yGbvBo
```

#### Minecraft

They're not playing together, but there's a shared audio recording.
The script struggles with these, with a false positive with a 62% similarity
but the way the transscript are broken up, it does't catch the overlapping audio unless threshold is lowered to 5.5, which causes even more false positives, but only one chunk of the overlapping audio (761.0), although there should be more matches.

```bash
python3 main.py HNEw7bZy8hc hKOFewS0JW0
```

#### Videos NOT in common:

```bash
python3 main.py VeH1fynKu6w 5pUCF6RQa50
```
