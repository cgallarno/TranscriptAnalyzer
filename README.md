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

#### Videos NOT in common:

```bash
python3 main.py VeH1fynKu6w 5pUCF6RQa50
```
